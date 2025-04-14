"""Flask server to detect emotions from a given text input."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Render the homepage with the input form."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Handle POST request from the form.
    Process the input text and display emotion detection results.
    """
    text_to_analyze = request.form['text']
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return render_template('index.html', message="Invalid text! Please try again!")

    result_message = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}."
    )
    return render_template('index.html', message=result_message)

if __name__ == '__main__':
    app.run(debug=True)
