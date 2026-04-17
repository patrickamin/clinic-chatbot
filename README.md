# Clinic Chatbot 🏥

An Arabic/English AI-powered customer service chatbot for Egyptian medical clinics.

## Features
- Bilingual support — responds in Arabic or English based on patient input
- Answers questions about clinic hours, location, and services
- Built with Python, Flask, and Google Gemini AI

## Tech Stack
- Python 3.11
- Flask
- Google Gemini AI (gemini-2.5-flash)
- python-dotenv

## Setup
1. Clone the repo
2. Create a virtual environment: `python3.11 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install flask google-genai python-dotenv`
5. Create a `.env` file with your Gemini API key: `GEMINI_API_KEY=your_key_here`
6. Run: `python3 app.py`
7. Open `http://localhost:5000`

## Demo
Built for Egyptian businesses — bilingual AI assistant that handles customer inquiries 24/7.