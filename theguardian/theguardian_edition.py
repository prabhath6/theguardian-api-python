"""
The edition endpoint returns all editions in the API.
"""
from theguardian import theguardian_section


class Edition(theguardian_section.Section):

    def __init__(self, api, **kwargs):

        """
        :param api: api-key
        :param kwargs: optional headers
        :return:
        """
        base_url = "https://content.guardianapis.com/editions"
        super(Edition, self).__init__(api, base_url, **kwargs)
