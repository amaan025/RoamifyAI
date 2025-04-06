from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

my_api_key="AIzaSyDn6j_ABPjd2udehdTqSvXwvjZv5hEgais"
genai.configure(api_key=my_api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="You are a outing planner...",  # Your existing instruction
)

# Store conversation history per session (in-memory, consider Redis for production)
conversations = {}

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    session_id = data.get('session_id', 'default')
    user_input = data['message']
    
    # Get or initialize conversation history
    if session_id not in conversations:
        conversations[session_id] = []
    
    chat_session = model.start_chat(history=conversations[session_id])
    response = chat_session.send_message(user_input)
    
    # Update history
    conversations[session_id].append({"role": "user", "parts": [user_input]})
    conversations[session_id].append({"role": "model", "parts": [response.text]})
    
    return jsonify({
        "response": response.text,
        "session_id": session_id
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Run on different port if needed