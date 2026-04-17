# 🏥 Clinic Chatbot — Bilingual AI Customer Support

An Arabic/English AI-powered customer service chatbot built for Egyptian medical clinics. Designed to help local businesses serve patients 24/7 in both languages without hiring additional staff.

![Demo](assets/demo.gif) -->

---

## Why This Exists

Most Egyptian clinics handle patient inquiries manually — phone calls, WhatsApp messages, and walk-ins. This chatbot automates common questions (clinic hours, location, available services, appointment info) in both Arabic and English, detecting the patient's language automatically and responding accordingly.

---

## Features

- **Bilingual support** — responds in Arabic or English based on patient input, with seamless language switching mid-conversation
- **Clinic-specific knowledge** — answers questions about hours, location, services, doctors, and policies
- **Instant responses** — handles patient inquiries 24/7 with no wait time
- **Simple web interface** — clean chat UI that can be embedded in any clinic website
- **Powered by Google Gemini AI** — uses gemini-2.5-flash for fast, accurate responses

---


## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Backend logic |
| Flask | Web server & routing |
| Google Gemini AI (gemini-2.5-flash) | LLM for generating responses |
| python-dotenv | Environment variable management |
| HTML/CSS/JS | Chat interface frontend |

---

## Setup

```bash
# 1. Clone the repo
git clone https://github.com/patrickamin/clinic-chatbot.git
cd clinic-chatbot

# 2. Create and activate a virtual environment
python3.11 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install flask google-genai python-dotenv

# 4. Create your .env file
echo "GEMINI_API_KEY=your_key_here" > .env

# 5. Run the app
python3 app.py

# 6. Open in browser
# http://127.0.0.1:5000
```

> **Note:** You'll need a Google Gemini API key. Get one free at [ai.google.dev](https://ai.google.dev/).

---

## Project Structure

```
clinic-chatbot/
├── app.py           # Flask server + Gemini AI integration
├── .env             # API key (not committed)
├── .gitignore       # Excludes .env and venv
└── README.md
```

---

## Demo

![Demo](assets/demo.gif) -->

Built for Egyptian businesses — a bilingual AI assistant that handles customer inquiries 24/7.

*Demo video coming soon.*

---

## What I Learned

- Integrating Google Gemini AI (gemini-2.5-flash) into a Python Flask application
- Designing bilingual prompts that handle Arabic/English code-switching naturally
- Structuring AI system prompts with domain-specific knowledge (clinic context)
- Building a clean chat UI with real-time message handling

---

## Future Improvements

- [ ] Deploy to a public URL (Railway or Render)
- [ ] Add WhatsApp integration via Twilio
- [ ] Support multiple clinic profiles from a single deployment
- [ ] Add appointment booking functionality

---

## Author

**Patrick Amin** — AI Engineer & Computer Science Graduate (2026)

- [LinkedIn](https://linkedin.com/in/patrickamin)
- [GitHub](https://github.com/patrickamin)

---

*Built as part of an AI automation portfolio — targeting prompt engineering and AI integration roles.*