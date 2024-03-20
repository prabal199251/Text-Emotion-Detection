import requests
import json


def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    formatted_response = json.loads(response.text)
    
    # Initialize emotion scores
    emotion_scores = {
        'anger': 0,
        'disgust': 0,
        'fear': 0,
        'joy': 0,
        'sadness': 0
    }
    
    # Extract emotion scores from nested structure
    if 'emotionPredictions' in formatted_response:
        predictions = formatted_response['emotionPredictions']
        if predictions:
            emotions = predictions[0]['emotion']
            for emotion_label, score in emotions.items():
                if emotion_label in emotion_scores:
                    emotion_scores[emotion_label] = score
    
    # Find dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Format output
    output = {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
    }
    
    return output
