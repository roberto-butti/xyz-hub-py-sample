import requests
import json
import logging


class Api:

    def get_json(self, url, token=None, content_type=None):
        logging.basicConfig(filename='example.log', level=logging.DEBUG)

        headers = {}

        if token:
            headers['Authorization'] ='Bearer ' + token
        if content_type:
            headers['accept'] = content_type
        logging.info('Calling: ' + url)
        try:
            with requests.get(url, headers=headers) as response:
                data = json.loads(response.text)
            logging.info(json.dumps(data, indent=4))
            return data
        except requests.exceptions.RequestException as e:
            print(e)
        return None
