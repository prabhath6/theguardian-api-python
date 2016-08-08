"""
Tests for the theguardian_section.py
"""

import unittest
from theguardian import theguardian_section


class TestSection(unittest.TestCase):

    """
    Mainly built to test the functionality
    of the theguardian_section module.
    """

    def test_section_response_success_correct_details(self):

        api_key = "test"
        res = theguardian_section.Section(api_key).get_request_response()

        self.assertEqual(res.status_code, 200)

    def test_section_response_failure_incorrect_api_key(self):

        api_key = "tests"
        res = theguardian_section.Section(api_key).get_request_response()

        self.assertEqual(res.status_code, 403)

    def test_section_get_direct_content(self):

        api_key = "test"
        res = theguardian_section.Section(api_key).get_content_response()

        self.assertIn("response", res.keys())

    def test_section_get_indirect_content(self):

        api_key = "test"
        section = theguardian_section.Section(api_key)
        res = section.get_request_response()
        section_content = section.get_content_response()

        self.assertEqual(res.status_code, 200)
        self.assertIn("response", section_content.keys())

    def test_section_get_indirect_content_invalid_credentials(self):

        api_key = "tests"
        section = theguardian_section.Section(api_key)
        res = section.get_request_response()
        section_content = section.get_content_response()

        self.assertEqual(res.status_code, 403)
        self.assertIn("message", section_content.keys())
        self.assertEqual("Invalid authentication credentials", section_content["message"])

    def test_section_get_result_without_exception(self):

        api_key = "test"
        section = theguardian_section.Section(api_key)
        section_content = section.get_content_response()
        results = section.get_results(section_content)

        self.assertIs(type(results), list)
        self.assertIn("editions", results[0].keys())

    def test_section_get_result_with_exception(self):

        api_key = "test"
        section = theguardian_section.Section(api_key)

        self.assertRaises(TypeError, section.get_results, "some random text")

if __name__ == "__main__":
    unittest.main()
