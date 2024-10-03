from flask import Flask, render_template, request, jsonify
from chatbot import SegmentationChatbot

app = Flask(__name__)
chatbot = SegmentationChatbot('user_segments_with_time.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['message']
    response = chatbot.process_input(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)