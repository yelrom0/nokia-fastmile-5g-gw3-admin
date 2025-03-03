from functools import lru_cache
from dotenv import dotenv_values

FOLDER_PREFIX = "/usr/local/bin/restart-modem"

class Settings():

    def __init__(self):
        _config = dotenv_values(f"{FOLDER_PREFIX}/.env")
        self.router_ip = _config["ROUTER_IP"]
        self.username = _config["USERNAME"]
        self.password = _config["PASSWORD"]

@lru_cache
def get_settings() -> Settings:
    return Settings()