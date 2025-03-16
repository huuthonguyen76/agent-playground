from src.model.api_model import APIStandardRequestModel, BaseModel


class CreateSessionRequestModel(APIStandardRequestModel):
    request_id: str = ''
    session_id: str


class ChatRequestModel(APIStandardRequestModel):
    request_id: str = ''
    session_id: str
    message: str


class GetHistoryRequestModel(APIStandardRequestModel):
    request_id: str = ''
    session_id: str


class GetAllSessionsRequestModel(APIStandardRequestModel):
    request_id: str = ''
