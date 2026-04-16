from flask import Flask, request, jsonify, render_template_string
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

SYSTEM_PROMPT = """You are a helpful customer service assistant for Nour Medical Clinic in Cairo, Egypt. 
You speak both Arabic and English fluently. 
Always respond in the same language the patient uses.
You can help with: appointment booking inquiries, clinic hours, services offered, location, and general medical questions.
Clinic hours: Saturday to Thursday, 9am to 9pm.
Location: 15 Tahrir Square, Cairo.
Services: General medicine, pediatrics, dermatology, cardiology.
Be warm, professional and concise."""

chat_history = []

HTML_TEMPLATE = """
<!DOCTYPE html>
<html dir="auto">
<head>
    <title>Nour Medical Clinic</title>
    <meta charset="UTF-8">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: Arial, sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; }
        .chat-container { width: 420px; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }
        .header { background: #2E7D32; color: white; padding: 16px 20px; }
        .header h2 { font-size: 16px; }
        .header p { font-size: 12px; opacity: 0.8; margin-top: 2px; }
        .messages { height: 400px; overflow-y: auto; padding: 16px; display: flex; flex-direction: column; gap: 10px; }
        .message { max-width: 80%; padding: 10px 14px; border-radius: 18px; font-size: 14px; line-height: 1.5; }
        .user { background: #2E7D32; color: white; align-self: flex-end; border-bottom-right-radius: 4px; }
        .bot { background: #f0f2f5; color: #333; align-self: flex-start; border-bottom-left-radius: 4px; }
        .input-area { display: flex; padding: 12px; border-top: 1px solid #eee; gap: 8px; }
        input { flex: 1; padding: 10px 14px; border: 1px solid #ddd; border-radius: 20px; font-size: 14px; outline: none; }
        button { background: #2E7D32; color: white; border: none; padding: 10px 18px; border-radius: 20px; cursor: pointer; font-size: 14px; }
        button:hover { background: #1B5E20; }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="header">
            <h2>🏥 Nour Medical Clinic</h2>
            <p>عيادة نور الطبية • Online Assistant</p>
        </div>
        <div class="messages" id="messages">
            <div class="message bot">Welcome! How can I help you today? مرحباً، كيف يمكنني مساعدتك؟</div>
        </div>
        <div class="input-area">
            <input type="text" id="userInput" placeholder="Type in English or Arabic..." onkeypress="if(event.key==='Enter') sendMessage()">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>
    <script>
        async function sendMessage() {
            const input = document.getElementById('userInput');
            const messages = document.getElementById('messages');
            const text = input.value.trim();
            if (!text) return;
            messages.innerHTML += `<div class="message user">${text}</div>`;
            input.value = '';
            messages.scrollTop = messages.scrollHeight;
            const res = await fetch('/chat', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({message: text}) });
            const data = await res.json();
            messages.innerHTML += `<div class="message bot">${data.response}</div>`;
            messages.scrollTop = messages.scrollHeight;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    chat_history.append({"role": "user", "parts": [user_message]})
    full_prompt = SYSTEM_PROMPT + "\n\nConversation:\n" + "\n".join([f"{m['role']}: {m['parts'][0]}" for m in chat_history])
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )
    bot_reply = response.text
    chat_history.append({"role": "model", "parts": [bot_reply]})
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)