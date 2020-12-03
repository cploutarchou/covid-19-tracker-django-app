import logging
from datetime import datetime
from app.redis.redis_client import RedisClient

redis = RedisClient(0)
client = redis.client
"""
Setup the logger
"""
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

"""
All the messages will store here
"""
messages = {}


def save_log_message(msg, msg_type):
    """
    Store logs in message variable
    :param msg
    :param msg_type
    """
    data = {
        'msg': msg,
        'type': msg_type,
        'created_at': datetime.now().__str__()
    }
    res = client.hset(key=msg_type, data=data)
    if res:
        print("Log message saved successfully")


def info(msg, *args, **kwargs):
    """
    Info logging
    :param msg
    """
    save_log_message(msg, 'info')
    logger.info(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    """
    Error logging
    :param msg
    """
    save_log_message(msg, 'error')
    logger.error(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    """
    Warning logging
    :param msg
    """
    save_log_message(msg, 'warning')
    logger.warning(msg, *args, **kwargs)


def warn(msg, *args, **kwargs):
    """
    Warning logging
    :param msg
    """
    save_log_message(msg, 'warning')
    logger.warning(msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    """
    Debug logging
    :param msg
    """
    save_log_message(msg, 'debug')
    logger.debug(msg, *args, **kwargs)


def get_all_info_logs():
    """
    Return all message of type info
    """
    res = redis.get(redis_key="info")
    if res and isinstance(res, dict):
        return messages
    else:
        raise Exception("Error : Unable to retrieve messages")


def reset():
    redis.client.flushall()
