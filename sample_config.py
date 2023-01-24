import os
import time

class Config(object):

    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    DATABASE_URI = os.environ.get("DATABASE_URI", "")
    DATABASE_NAME = str(os.environ.get("DATABASE_NAME", "Cluster0"))
    AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())
    SAVE_USER = os.environ.get("SAVE_USER", "no").lower()
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")
    ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")
    DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMDD", "del")
    DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMDD", "delall")
    CONNECT_COMMAND = os.environ.get("CONNECT_COMMANDD", "connect")
    DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMANDD", "disconnect")
    BOT_START_TIME = time.time()
