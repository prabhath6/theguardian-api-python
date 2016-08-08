"""
The content endpoint (/search) returns
all pieces of content in the API.
"""
import requests
import copy


class Content:

    def __init__(self, api, url=None, **kwargs):
        """
        :param api: api_key
        :param url: optional url to get the content.
        :param kwargs: optional header data
        :return: None
        """

        self.__headers = {
            "api-key": api,
            "format": "json"
        }
        self.__request_response = None

        if url is None:
            self.base_url = "https://content.guardianapis.com/search"
        else:
            self.base_url = url

        if kwargs:
            for key, value in kwargs.items():
                self.__headers[key] = value

    def __response(self, headers=None):

        """
        :param headers: optional header
        :return: returns raw response.
        """

        if headers is None:
            headers = self.__headers
        else:
            headers.update(self.__headers)

        res = requests.get(self.base_url, headers)

        return res

    def get_request_response(self, headers=None):

        """
        :param headers: optional headers
        :return: raw request response
        """

        self.__request_response = self.__response(headers)
        return self.__request_response

    def get_content_response(self, headers=None):

        """
        :param headers: optional header
        :return: json content of the response for the request
        """

        self.get_request_response(headers)
        return self.__request_response.json()

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

    def find_by_id(self, ids, **kwargs):

        """
        :param ids: Get the Content using its id. IDs are usually in the form
        of url/section/YYYY/month/DD/name-of-article/
        technology/2014/feb/17/flappy-bird-clones-apple-google

        :param kwargs: optional headers
        :return: dict
        """

        ids_and_options = self.__response_for_id(ids, **kwargs)
        ids_and_options.update(self.__headers)

        return self.__response(ids_and_options).json()

    @staticmethod
    def __response_for_id(ids, **kwargs):

        """
        :param ids: IDs are usually in the form
        of url/section/YYYY/month/DD/name-of-article/

        :param kwargs: optional headers
        :return: dict
        """

        headers = {}

        if ids and isinstance(ids, str):
            headers["ids"] = ids
        if kwargs:
            headers.update(kwargs)

        return headers

    @staticmethod
    def get_results(content):

        """
        :param content: response from url
        :return: list of results
        """

        if isinstance(content, dict):
            results = content["response"]["results"]
        else:
            raise TypeError("Content of type dictionary required as input.")

        return results if results else []

    def get_references_in_page(self, page_number=None):

        """
        :param page_number: optional
        :return:
        """

        head = self.response_headers()

        if page_number is None:
            content = self.get_content_response({
                "show-references": "all"
            })
            results = self.get_results(content)
            references = self.__get_references(results)
            return references
        elif page_number and page_number <= head["pages"]:
            content = self.get_content_response({
                "page": page_number,
                "show-references": "all"
            })
            results = self.get_results(content)
            references = self.__get_references(results)
            return references
        else:
            raise ValueError("Page number greater than available pages. Available pages {}."
                             .format(head["pages"]))

    @staticmethod
    def __get_references(results):

        """
        :param results: list of results
        :return: list of results
        """

        refs = [(result["id"], result["references"]) for result in results if result["references"]]

        return refs
