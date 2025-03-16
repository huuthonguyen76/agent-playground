import hashlib
import re

from datetime import datetime
from src.mongodb.model.common_model import ChatSessionMongo, ChatHistoryMongo
from typing import List
from mongoengine import *


def create_chat_session(session_id: str, created_at: datetime):
    ChatSessionMongo.objects(session_id=session_id).update_one(
        set__session_id=session_id,
        set__created_at=created_at,
        upsert=True,
    )


def insert_chat_history(session_id: str, user_input: str, ai_output: str, info_output: str, created_at: datetime):
    ChatHistoryMongo(
        session_id=session_id,
        user_input=user_input,
        ai_output=ai_output,
        info_output=info_output,
        created_at=created_at,
    ).save()


def get_all_sessions():
    return ChatSessionMongo.objects()


def get_history(session_id: str):
    return ChatHistoryMongo.objects(session_id=session_id).order_by('-created_at')
