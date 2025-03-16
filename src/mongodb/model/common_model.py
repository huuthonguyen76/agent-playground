from mongoengine import Document, StringField, DateTimeField, ListField, BooleanField, FloatField, IntField
from src.bucket.enum import ALIAS_INGESTION_DB, MONGODB_CHAT_SESSION_COL, MONGODB_CHAT_HISTORY_COL
from src.bucket.mongo import *


class ChatSessionMongo(Document):
    meta = {'db_alias': ALIAS_INGESTION_DB, 'collection': MONGODB_CHAT_SESSION_COL}

    session_id = StringField(min_length=1)
    created_at = DateTimeField()


class ChatHistoryMongo(Document):
    meta = {'db_alias': ALIAS_INGESTION_DB, 'collection': MONGODB_CHAT_HISTORY_COL}

    session_id = StringField(min_length=1)

    user_input = StringField(min_length=1)
    ai_output = StringField(min_length=1)
    info_output = StringField(min_length=1)

    created_at = DateTimeField()
