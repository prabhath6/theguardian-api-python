"""
Tests for the theguardian_tag.py
"""
import unittest
from theguardian import theguardian_tag


class TestTag(unittest.TestCase):

    """
    Mainly built to test the functionality
    of the theguardian_tag module.
    """

    def test_tag_response_success_correct_details(self):

        api_key = "test"
        res = theguardian_tag.Tag(api_key).get_request_response()

        self.assertEqual(res.status_code, 200)

    def test_tag_response_failure_incorrect_api_key(self):

        api_key = "tests"
        res = theguardian_tag.Tag(api_key).get_request_response()

        self.assertEqual(res.status_code, 403)

    def test_tag_get_direct_content(self):

        api_key = "test"
        res = theguardian_tag.Tag(api_key).get_content_response()

        self.assertIn("response", res.keys())

    def test_tag_get_indirect_content(self):

        api_key = "test"
        tag = theguardian_tag.Tag(api_key)
        res = tag.get_request_response()
        tag_content = tag.get_content_response()

        self.assertEqual(res.status_code, 200)
        self.assertIn("response", tag_content.keys())

    def test_tag_get_indirect_content_invalid_credentials(self):

        api_key = "tests"
        tag = theguardian_tag.Tag(api_key)
        res = tag.get_request_response()
        tag_content = tag.get_content_response()

        self.assertEqual(res.status_code, 403)
        self.assertIn("message", tag_content.keys())
        self.assertEqual("Invalid authentication credentials", tag_content["message"])

    def test_tag_get_result_without_exception(self):

        api_key = "test"
        tag = theguardian_tag.Tag(api_key)
        tag_content = tag.get_content_response()
        results = tag.get_results(tag_content)

        self.assertIs(type(results), list)

    def test_tag_get_result_with_exception(self):

        api_key = "test"
        tag = theguardian_tag.Tag(api_key)

        self.assertRaises(TypeError, tag.get_results, "some random text")

    def test_tag_url(self):

        api_key = "test"
        tag = theguardian_tag.Tag(api_key)
        tag_request_content = tag.get_request_response()

        self.assertEqual(tag.base_url, tag_request_content.url.split("?")[0])

    def test_section_get_references_correct_pages(self):

        api_key = "test"
        tag = theguardian_tag.Tag(api_key, **{
            "q": "apple",
            "section": "technology",
        })
        refs = tag.get_references_in_page(page_number=1)
        refs2 = tag.get_references_in_page()

        self.assertIs(type(refs), list)
        self.assertIs(type(refs2), list)

    def test_section_get_references_incorrect_pages(self):

        api_key = "test"
        tag = theguardian_tag.Tag(api_key, **{
            "q": "apple",
            "section": "technology",
        })

        head = tag.response_headers()

        self.assertRaises(ValueError, tag.get_references_in_page, page_number=head["pages"] + 1)

if __name__ == '__main__':
    unittest.main()
