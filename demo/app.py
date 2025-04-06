from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

my_api_key = "AIzaSyBj96kR4HTakOCiZhCE0Sg14DiggfLxxo8"
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
    system_instruction="""You are a professional travel planning assistant. Your task is to:

1. Conversation Flow:
   - Begin with a warm but professional greeting
   - Sequentially request: current location, outing preferences, budget
   - Provide recommendations only after gathering all necessary information

2. Response Requirements:
   - Maintain a professional yet approachable tone (avoid slang)
   - Structure responses clearly with bullet points when listing options
   - Include estimated costs for each recommendation
   - Ensure locations are within close proximity (max 0.5 mile radius)
   - Verify recommendations meet the user's budget

4. Example Professional Response:
   \"Based on your £50 budget for dinner and arcade entertainment in <Location>, I recommend:
   - Dining: <Place_name> (Address) - <approx. cost>
   - Entertainment: <Place_name> (Address) - <approx. cost>

   Are you happy with this plan? If the user says yes, then reply I will now show you the map wit these locations."
"""
)

# Store conversations in memory (for production, use a database)
conversations = {}

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    session_id = data.get('session_id', 'default')
    user_input = data['message']
    
    # Initialize conversation history if new session
    if session_id not in conversations:
        conversations[session_id] = []
    
    # Start chat with existing history
    chat_session = model.start_chat(history=conversations[session_id])
    response = chat_session.send_message(user_input)
    
    # Update conversation history
    conversations[session_id].append({"role": "user", "parts": [user_input]})
    conversations[session_id].append({"role": "model", "parts": [response.text]})
    
    return jsonify({
        "response": response.text,
        "session_id": session_id
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)