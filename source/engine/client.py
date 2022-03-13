import requests


class Client():
    def __init__(self, token):
        self.token = token
        self.server = "https://api.telegram.org/"

    def request(self, method, parameters={}):
        response = requests.post(
            self.server + "bot" + self.token + "/" + method, parameters)
        return response.json()

    def listen(self, handle, parameters={}):
        while True:
            try:
                updates = self.request("getUpdates", parameters)
                if updates["result"] == []:
                    continue
                handle(updates)
                parameters["offset"] = updates["result"][0]["update_id"] + 1
            except:
                print("Unexpected interruption. Forced exit...")
                break

    def handle(self, updates):
        print(updates)
        try:
            response = self.request("sendMessage", {
                "chat_id": updates["result"][0]["message"]["chat"]["id"],
                "text": updates["result"][0]["message"]["text"],
            })
        except:
            print("Unexpected interruption. Forced exit...")
        return response

    def log(self):
        pass
