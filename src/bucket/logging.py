import os

from loguru import logger
from .enum import *


d_logger = {}
def prepare_logger() -> None:
    """
    Prepare the logger for K-Bot API.

    This function creates a log folder if it doesn't exist and sets up the logger to log messages to a file.

    Returns:
        None
    """
    # Create log folder if not exist
    if not os.path.exists('log'):
        os.makedirs('log')

    logger.add('log/ingestion.log', rotation="3000 MB", enqueue=True)


class APILogger():
    def __init__(self, logger, request_id='', component_name=''):
        self.__logger = logger
        self.component_name = component_name
        self.request_id = request_id

    def info(self, msg):
        self.__logger.info(' | Request ID: {request_id} | {component_name} | {msg}', component_name=self.component_name, request_id=self.request_id, msg=repr(msg))

    def error(self, msg):
        self.__logger.error(' | Request ID: {request_id} | {component_name} | {msg}', component_name=self.component_name, request_id=self.request_id, msg=repr(msg))

    def exception(self, msg):
        self.__logger.exception(' | Request ID: {request_id} | {component_name} | {msg}', component_name=self.component_name, request_id=self.request_id, msg=repr(msg))

    def warn(self, msg):
        self.__logger.warning(' | Request ID: {request_id} | {component_name} | {msg}', component_name=self.component_name, request_id=self.request_id, msg=repr(msg))


def get_logger(component_name, request_id='') -> APILogger:
    """
    Get a logger instance for the specified component name and request ID.

    Args:
        component_name (str): The name of the component.
        request_id (str, optional): The ID of the request. Defaults to ''.

    Returns:
        APILogger: A logger instance for the specified component and request.
    """
    api_logger = APILogger(logger)
    api_logger.component_name = component_name
    api_logger.request_id = request_id
    return api_logger

prepare_logger()
