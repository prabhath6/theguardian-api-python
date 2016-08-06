# -*- coding: utf-8 -*-

"""
The content endpoint (/search) returns all pieces of content in the API.
"""
import requests


class Content:

    def __init__(self, url="", api=None, **kwargs):

        self.base_url = url
        self.headers = {"api-key": api}

        if kwargs:
            for key, value in kwargs.items():
                self.headers[str(key)] = value

    def response(self):
        res = requests.get(self.base_url, self.headers)
        return res
