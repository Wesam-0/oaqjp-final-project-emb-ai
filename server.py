from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    text_to_analyze = request.form.get('text')
    
    if not text_to_analyze:
        return jsonify({
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': 'Invalid text! Please try again!'
        })
    
    response = emotion_detector(text_to_analyze)
    
    if response['dominant_emotion'] == 'Invalid text! Please try again!':
        return jsonify(response)

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
