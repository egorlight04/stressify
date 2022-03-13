from engine.client import Client
from engine.localizator import Localizator
from engine.logger import Logger


class Main():
    def __init__(self):
        token = open(".token", "r").readline()[:-1]

        client = Client(token)
        logger = Logger()
        localizator = Localizator()

        client.listen(client.handle, {
            "limit": 1,
            "offset": 0,
            "timeout": 30,
            "allowed_updates": ["message"],
        })


Main()
