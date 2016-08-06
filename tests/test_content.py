# -*- coding: utf-8 -*-

"""
Tests for the theguardian_content.py
"""

import unittest
from theguardian import theguardian_content


class TestContent(unittest.TestCase):

    """
    Mainly built to test the functionality of the theguardian_content module.
    """

    def test_content_response_success_correct_details(self):

        url = "https://content.guardianapis.com/search"
        api_key = "test"
        res = theguardian_content.Content(url, api_key).response()
        self.assertEqual(res.status_code, 200)

    def test_content_response_failure_incorrect_api_key(self):

        url = "https://content.guardianapis.com/search"
        api_key = "tests"
        res = theguardian_content.Content(url, api_key).response()
        self.assertEqual(res.status_code, 403)

    def test_content_response_failure_incorrect_url_endpoint(self):

        url = "https://content.guardianapis.com/searchwwqe"
        api_key = "test"
        res = theguardian_content.Content(url, api_key).response()
        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main()