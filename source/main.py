from engine.client import Client


token = open(".token", "r").readline()[:-1]
bot = Client(token)


def handle(update):
    print(update)


bot.listen(handle, {
    "limit": 1,
    "offset": 0,
    "timeout": 30,
    "allowed_updates": ["message"],
})
