import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        resp_body = requests.get(self.url)
        return resp_body.content

    def load_json(self):
        info_in_json = json.loads(self.get_response_body())
        return info_in_json
