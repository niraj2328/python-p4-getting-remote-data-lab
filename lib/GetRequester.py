import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_json(self):
        response = requests.get(self.url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx errors
        return response.json()
