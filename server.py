"""
Emotion Detector Server

This module implements a Flask server for emotion detection.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Detect emotion from the given text.

    Returns:
        str: System response including emotion scores and dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    response_message = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}"
    )

    return response_message

@app.route("/")
def render_index_page():
    """
    Render the index page.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
