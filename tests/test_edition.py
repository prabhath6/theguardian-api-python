"""
Tests for the theguardian_edition.py
"""
import unittest
from theguardian import theguardian_edition


class TestEdition(unittest.TestCase):

    """
    Mainly built to test the functionality
    of the theguardian_edition module.
    """

    def test_edition_response_success_correct_details(self):

        api_key = "test"
        res = theguardian_edition.Edition(api_key).get_request_response()

        self.assertEqual(res.status_code, 200)

    def test_edition_response_failure_incorrect_api_key(self):

        api_key = "tests"
        res = theguardian_edition.Edition(api_key).get_request_response()

        self.assertEqual(res.status_code, 403)

    def test_edition_get_direct_content(self):

        api_key = "test"
        res = theguardian_edition.Edition(api_key).get_content_response()

        self.assertIn("response", res.keys())

    def test_edition_get_indirect_content(self):

        api_key = "test"
        edition = theguardian_edition.Edition(api_key)
        res = edition.get_request_response()
        edition_content = edition.get_content_response()

        self.assertEqual(res.status_code, 200)
        self.assertIn("response", edition_content.keys())

    def test_edition_get_indirect_content_invalid_credentials(self):

        api_key = "tests"
        edition = theguardian_edition.Edition(api_key)
        res = edition.get_request_response()
        edition_content = edition.get_content_response()

        self.assertEqual(res.status_code, 403)
        self.assertIn("message", edition_content.keys())
        self.assertEqual("Invalid authentication credentials", edition_content["message"])

    def test_edition_get_result_without_exception(self):

        api_key = "test"
        edition = theguardian_edition.Edition(api_key)
        edition_content = edition.get_content_response()
        results = edition.get_results(edition_content)

        self.assertIs(type(results), list)

    def test_edition_get_result_with_exception(self):

        api_key = "test"
        edition = theguardian_edition.Edition(api_key)

        self.assertRaises(TypeError, edition.get_results, "some random text")

    def test_edition_url(self):

        api_key = "test"
        edition = theguardian_edition.Edition(api_key)
        edition_request_content = edition.get_request_response()

        self.assertEqual(edition.base_url, edition_request_content.url.split("?")[0])

    def test_edition_get_response_section_count(self):

        api_key = "test"
        edition = theguardian_edition.Edition(api_key)
        edition_content = edition.get_content_response()
        total = edition_content['response']['total']
        result_len = len(edition_content['response']['results'])

        self.assertEqual(total, result_len)

if __name__ == '__main__':
    unittest.main()
