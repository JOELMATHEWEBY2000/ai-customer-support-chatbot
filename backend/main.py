from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from starlette.concurrency import run_in_threadpool

from chatbot import generate_response

app = FastAPI(title="AI Customer Support API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


class ChatMessage(BaseModel):
    role: str
    content: str = Field(min_length=1, max_length=4000)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
    history: list[ChatMessage] = Field(default_factory=list, max_length=20)


@app.get("/")
def home():
    return {
        "message": "AI Customer Support API is running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/chat")
async def chat(request: ChatRequest):

    message = request.message.strip()

    if not message:
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty."
        )

    if any(item.role not in ("user", "model")
           for item in request.history):
        raise HTTPException(
            status_code=400,
            detail="Invalid conversation history."
        )

    history = [
        item.model_dump()
        for item in request.history
    ]

    try:
        answer = await run_in_threadpool(
            generate_response,
            message,
            history
        )

        return {
            "reply": answer
        }

    except Exception as e:
        print("GEMINI ERROR:", repr(e))
        raise HTTPException(
            status_code=502,
            detail=str(e)
              )