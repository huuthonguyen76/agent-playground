from pydantic_settings import BaseSettings

class SettingModel(BaseSettings):
    MONGODB_INGESTION_DB: str
    MONGODB_URI: str
    HTML_EXECUTOR_URL: str
    OPENAI_API_KEY: str
    N8N_CHAT_WEBHOOK_URL: str

    class Config:
        env_file = ".env"
