
# AI Automation Tool 🚀

This AI automation tool provides async backend communication, task processing with Celery, and image generation using Python and React.

## Features
- 🔹 Async Backend with FastAPI
- 🔹 GPT API Integration
- 🔹 Background Processing with Celery
- 🔹 Image Generation with Python (PIL)
- 🔹 React Frontend with Vite
- 🔹 PostgreSQL for Data Storage
- 🔹 Docker & CI/CD Deployment

## Tech Stack
- **Backend**: FastAPI, Celery, OpenAI GPT, PIL
- **Frontend**: React (Vite), Tailwind CSS
- **Database**: PostgreSQL
- **Message Broker**: Redis
- **Deployment**: Docker, CI/CD

## Project Structure
```
📂 ai-automation-tool
│── 📂 backend
│   ├── app.py (FastAPI app)
│   ├── tasks.py (Celery tasks)
│   ├── models.py (Database models)
│   ├── services.py (GPT & image generation)
│   ├── celery_worker.py
│── 📂 frontend
│   ├── src/
│   ├── components/
│   ├── App.tsx
│── 📂 database
│   ├── migrations/
│── docker-compose.yml
│── README.md
```

## Setup Instructions

### 1️⃣ Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
uvicorn src.main:app --reload
```

### 2️⃣ Start Celery Worker
```bash
celery -A tasks worker --loglevel=info
```

### 3️⃣ Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### 4️⃣ Run with Docker
```bash
docker-compose up --build
```

## API Endpoints
- `POST /generate-text` - Generate text using GPT API
- `POST /generate-image` - Generate images using Python
- `GET /tasks/{task_id}` - Get task status

---

## Future Improvements
- ✅ WebSockets for real-time updates
- ✅ Multi-user authentication
- ✅ Advanced AI model integration

## Contributions
Feel free to fork and contribute! 🚀


💡 **Built with ❤️ by Shubham**
