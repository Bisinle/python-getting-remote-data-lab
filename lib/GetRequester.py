import requests
import json

# class GetRequester:

#     def __init__(self, url):
#         self.url = url

#     def get_response_body(self):
#         pass

#     def load_json(self):
#         pass


class GetRequester:
    def __init__(self, url):
        self.url=url

    # ge the response body 
    def get_response_body(self):
        return requests.get(self.url).content

        
    # use get_response_body, load it and return a python list of dict
    def load_json(self):
        json_content = json.loads(self.get_response_body())
        return json_content