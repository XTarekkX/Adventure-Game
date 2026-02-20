# 🧙 AI Adventure Story Backend

An AI-powered adventure game backend built with **FastAPI** where users generate interactive stories based on a chosen theme.

The backend sends the theme to an LLM, receives a structured story tree, validates it using Pydantic, and stores the branching story nodes in the database.

Users progress by selecting choices until they reach either a **winning** or **losing** ending.

---

## ⚙️ Tech Stack

- **FastAPI** – API framework  
- **SQLite** – Database  
- **SQLAlchemy** – ORM  
- **Pydantic** – Schema validation  
- **LangChain + OpenAI** – Structured story generation  
- **Uvicorn** – ASGI server  
- **uv** – Python package manager  

---

## 🏗️ How It Works

1. User sends a story theme.
2. Backend sends a structured prompt to the LLM.
3. LLM returns a JSON story tree (root node + branches).
4. Response is validated using Pydantic schemas.
5. Nodes are recursively stored in the database.
6. Client navigates the story via node options.

Each node contains:
- Story content  
- 2–3 choices (if not an ending)  
- `is_ending`  
- `is_winning_ending`  

Story depth is limited to keep gameplay controlled and token usage predictable.

---

## 🚀 Setup & Usage

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/ai-adventure-backend.git
cd ai-adventure-backend
```

### 2️⃣ Install dependencies

Using **uv**:

```bash
uv sync
```

Or with pip:

```bash
pip install -r requirements.txt
```

### 3️⃣ Set environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key
```

### 4️⃣ Run the server

```bash
uvicorn main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Swagger docs:

```
http://localhost:8000/docs
```

## 🎯 Project Purpose

This project demonstrates:

- Structured LLM output control  
- Recursive database modeling  
- Clean backend architecture  
- AI + API integration  
