"# ai-customer-support-chatbot" 
AI Customer Support Chatbot
An AI-powered customer support chatbot built with React, Python,
FastAPI, and Google Gemini.
Features
- AI-powered customer conversations
- Conversation context
- Responsive React interface
- FastAPI REST API
- Error handling
Tech Stack
React · Python · FastAPI · Gemini API · Axios
Project Structure
ai-customer-support-chatbot/
├── backend/
│   ├── main.py
│   ├── chatbot.py
│   ├── .env
│   └── requirements.txt
├── frontend/
└── README.md
Setup
Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Create backend/.env:
GEMINI_API_KEY=your_api_key
GEMINI_MODEL=your_available_model
Run:
uvicorn main:app --reload
Frontend
In a second terminal:
cd frontend
npm install
npm install axios lucide-react
npm run dev
Open http://localhost:5173. API docs: http://127.0.0.1:8000/docs.
API Endpoints
- GET / --- API status
- GET /health --- Health check
- POST /chat --- Generate a chatbot response
Security
Get your API key from https://aistudio.google.com/apikey. Keep it in
.env and never commit that file to GitHub. Use a Gemini model
available to your API key that supports generateContent