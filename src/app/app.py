from fastapi import FastAPI
from src.model.agent_history_model import *
from src.component import *


app = FastAPI()


@app.post("/v1/chat")
def v1_chat_handler(item: ChatRequestModel):
    return chat_handler(item)


@app.post("/v1/create-session")
def v1_create_session_handler(item: CreateSessionRequestModel):
    return create_chat_session_handler(item)


@app.get("/v1/get-all-sessions")
def v1_get_all_sessions_handler(request_id = ''):
    item = GetAllSessionsRequestModel(request_id=request_id)
    return get_all_sessions_handler(item)


@app.get("/v1/get-history")
def v1_get_history_handler(session_id: str, request_id = ''):
    item = GetHistoryRequestModel(request_id=request_id, session_id=session_id)
    return get_history_handler(item)


@app.get("/health-check")
def health_check_handler():
    return {
        'status': True,
        'version': 'mar-16-2025'
    }
