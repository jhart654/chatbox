import os
from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    try:
        # Call the OpenAI API for chat completions
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or another model like "gpt-4" if available
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        # Extract the response text
        response_text = response.choices[0].message['content'].strip()
    except Exception as e:
        response_text = "An error occurred: " + str(e)

    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
