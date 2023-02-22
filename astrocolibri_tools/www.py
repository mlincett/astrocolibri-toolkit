import requests

class WebServer:
    def __init__(self, prefix : str = "") -> None:
        self.prefix = prefix
        pass

    def get(self, *query) -> str:
        result = requests.get(*query)
        return result