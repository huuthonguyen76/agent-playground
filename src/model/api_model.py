import uuid

from pydantic import BaseModel
from pydantic import BaseModel, validator, Field
from typing import List

from src.bucket.enum import *


class APIReturnModel(BaseModel):
    code: int = HTTP_STATUS_INTERNAL_ERROR
    error_msg: str = ''
    warn_msg: str = ''
    result: dict = {}
    request_id: str = ''


class APIStandardRequestModel(BaseModel):
    request_id: str = ''
    
    @validator('request_id')
    def validate_custom_instruction(cls, v):
        if v is None or v.strip() == '':
            v = str(uuid.uuid4())

        return v
