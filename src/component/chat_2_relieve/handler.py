import requests

from datetime import datetime
from src.bucket.setting import get_setting
from src.bucket.logging import get_logger
from src.bucket.enum import *
from src.model.agent_history_model import *
from src.model.api_model import APIReturnModel
from src.mongodb.crud.agent import *


_setting = get_setting()


def call_n8n_chat_webhook(session_id: str, message: str):
    url = f"{_setting.N8N_CHAT_WEBHOOK_URL}?sessionId={session_id}&chatInput={message}"
    response = requests.get(url)
    return response


def create_chat_session_handler(item: CreateSessionRequestModel):
    logger = get_logger(CREATE_SESSION_LOG_NAME, item.request_id)

    logger.info(f"Start to create chat session. Payload: {item}")

    try:
        create_chat_session(item.session_id, datetime.now())
    except Exception as e:
        logger.exception(f"Error when creating chat session: {e}.")
        return APIReturnModel(request_id=item.request_id, error_msg=f'{str(e)}. Request ID: {item.request_id}.')

    api_return_item = APIReturnModel(code=HTTP_STATUS_SUCCESSFUL, request_id=item.request_id, result={
        "status": "success",
        "session_id": item.session_id,
    })

    logger.info(f"Finished. Output: {api_return_item}")

    return api_return_item


def get_all_sessions_handler(item: GetAllSessionsRequestModel):
    logger = get_logger(GET_ALL_SESSIONS_LOG_NAME, item.request_id)

    logger.info(f"Start to get all sessions. Payload: {item}")

    try:
        d_response = get_all_sessions()
        print(d_response)
        l_response = [
            {
                "session_id": d_item.session_id,
                "created_at": d_item.created_at,
            } for d_item in d_response
        ]

    except Exception as e:
        logger.exception(f"Error when getting all sessions: {e}.")
        return APIReturnModel(request_id=item.request_id, error_msg=f'{str(e)}. Request ID: {item.request_id}.')

    api_return_item = APIReturnModel(code=HTTP_STATUS_SUCCESSFUL, request_id=item.request_id, result={
        'chat_sessions': l_response,
    })

    logger.info(f"Finished. Output: {api_return_item}")

    return api_return_item


def get_history_handler(item: GetHistoryRequestModel):
    logger = get_logger(GET_HISTORY_LOG_NAME, item.request_id)

    logger.info(f"Start to get history. Payload: {item}")

    try:
        d_response = get_history(item.session_id)
        l_response = [
            {
                "user_input": d_item.user_input,
                "ai_output": d_item.ai_output,
                "info_output": d_item.info_output,
                "created_at": d_item.created_at,
            } for d_item in d_response
        ]

    except Exception as e:
        logger.exception(f"Error when getting history: {e}.")
        return APIReturnModel(request_id=item.request_id, error_msg=f'{str(e)}. Request ID: {item.request_id}.')

    api_return_item = APIReturnModel(code=HTTP_STATUS_SUCCESSFUL, request_id=item.request_id, result={
        'chat_history': l_response,
    })

    logger.info(f"Finished. Output: {api_return_item}")

    return api_return_item


def chat_handler(item: ChatRequestModel):
    logger = get_logger(CHAT_LOG_NAME_V1, item.request_id)
    
    logger.info(f"Start to chat. Payload: {item}")
    try:
        raw_response = call_n8n_chat_webhook(item.session_id, item.message)
        logger.info(f"Raw response: {raw_response.text}")

        d_response = raw_response.json()[0]
        logger.info(f"Response: {d_response}")

        create_chat_session(item.session_id, datetime.now())
        insert_chat_history(item.session_id, d_response['user_input'], d_response['ai_output'], d_response['info_output'], datetime.now())

    except Exception as e:
        logger.exception(f"Error when calling n8n chat webhook: {e}.")
        return APIReturnModel(request_id=item.request_id, error_msg=f'{str(e)}. Request ID: {item.request_id}.')

    api_return_item = APIReturnModel(code=HTTP_STATUS_SUCCESSFUL, request_id=item.request_id, result=d_response)

    logger.info(f"Finished chat. Output: {api_return_item}")

    return api_return_item


if __name__ == "__main__":
    print(call_n8n_chat_webhook("1937270afdbb4e33b751f6efedccd4a7", "hello"))
