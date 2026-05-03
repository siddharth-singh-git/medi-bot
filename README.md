# 🧠 MediBot – AI-Powered Medical Chatbot (RAG + Pinecone + Gemini)

MediBot is an AI-powered chatbot that answers medical queries using a Retrieval-Augmented Generation (RAG) pipeline. It uses Pinecone as a vector database and Google Gemini as the LLM for generating responses.

---

## 🚀 Features

- Chat-based medical Q&A
- Document-based retrieval (PDF support)
- Semantic search using vector database (Pinecone)
- Powered by Gemini LLM
- Fast API using Flask
- Deployable on Vercel (lightweight setup)

---

## 🏗️ Tech Stack

- Backend: Flask
- LLM: Google Gemini
- Vector Database: Pinecone
- Framework: LangChain
- Embeddings: Google Generative AI Embeddings
- Document Processing: PyPDF

---

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone https://github.com/your-username/medibot.git  
cd medibot

---

### 2. Create Virtual Environment

python -m venv venv

Activate:  
Windows → venv\Scripts\activate  
Mac/Linux → source venv/bin/activate

---

### 3. Install Dependencies

pip install -r requirements.txt

---

### 4. Setup Environment Variables

Create a .env file:

PINECONE_API_KEY=your_pinecone_api_key  
gemini_api_key=your_gemini_api_key

---

## 🧠 How It Works

1. Documents are indexed into Pinecone (one-time process)
2. User sends query
3. Similar chunks retrieved from Pinecone
4. Gemini generates final answer

---

## ▶️ Run Locally

python app.py

Open: http://localhost:8080

---

## 🌐 Deployment (Vercel)

- Remove heavy libraries (torch, sentence-transformers)
- Add env variables in Vercel dashboard
- Deploy

---

## 📌 API Endpoints

GET / → Load UI

POST /get → Chat

Request: msg=your question  
Response: AI answer

---

## ⚠️ Key Optimizations

- Removed heavy ML libraries
- Using API-based embeddings
- Pre-built Pinecone index
- Optimized for serverless

---

## 🔒 Security

- Do not commit .env
- Keep API keys private

---

## 📈 Future Improvements

- Chat memory
- Better UI
- Authentication
- Streaming

---

## 👨‍💻 Author

Siddharth Singh

---

## ⭐ Support

Star the repo if helpful!
