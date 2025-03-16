from mongoengine import connect

from .setting import get_setting
from .enum import ALIAS_INGESTION_DB

_setting = get_setting()

connect(alias=ALIAS_INGESTION_DB, db=_setting.MONGODB_INGESTION_DB, host=_setting.MONGODB_URI)
