"""
The sections endpoint(/sections) returns all sections in the API.
"""
import requests
import copy


class Section:

    def __init__(self, api, url=None, **kwargs):

        """
        :param api: api-key
        :param kwargs: optional headers
        :return:
        """

        self.__request_response = None
        self.__headers = {
            "api-key": api,
            "format": "json"
        }

        if not url:
            self.base_url = "https://content.guardianapis.com/sections"
        else:
            self.base_url = url

        if kwargs:
            for key, value in kwargs.items():
                self.__headers[key] = value

    def __response(self, header=None):

        """
        :param header: optional headers
        :return: raw request response
        """

        if header is None:
            header = self.__headers
        else:
            header.update(self.__headers)
        res = requests.get(self.base_url, header)

        return res

    def get_request_response(self, headers=None):

        """
        :param headers: optional headers
        :return: raw section request response
        """

        self.__request_response = self.__response(headers)
        return self.__request_response

    def get_content_response(self, headers=None):

        """
        :param headers: optional headers
        :return: dict of response
        """

        if self.__request_response is None or headers:
            self.__request_response = self.get_request_response(headers)

        return self.__request_response.json()

    @staticmethod
    def get_results(section_content):

        """
        :param section_content: dict of response received
        :return: list of results in that page
        """

        if isinstance(section_content, dict):
            results = section_content["response"]["results"]
        else:
            raise TypeError("Section content of type dictionary required as input.")

        return results if results else []

    def response_headers(self, headers=None):

        """
        :param headers: optional header
        :return: dict of header contents in the response
        """

        if self.__request_response:
            response_content = copy.deepcopy(self.__request_response.json())
        else:
            self.get_request_response(headers)
            response_content = copy.deepcopy(self.__request_response.json())

        headers_content = response_content['response']
        headers_content.pop("results")

        return headers_content
