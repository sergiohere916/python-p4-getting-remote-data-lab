import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # content_list = []
        contents = json.loads(self.get_response_body())
        # content_list = [content["agency"] for content in contents]
        return contents

