"""
The tags endpoint (/tags) returns all tags in the API.
All Guardian content is manually categorised using these
tags, of which there are more than 50,000
"""
from theguardian import theguardian_section


class Tag(theguardian_section.Section):

    def __init__(self, api, **kwargs):

        """
        :param api: api-key
        :param kwargs: optional headers
        :return:
        """
        base_url = "http://content.guardianapis.com/tags"
        super(Tag, self).__init__(api, base_url, **kwargs)

    def get_references_in_page(self, page_number=1):

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
