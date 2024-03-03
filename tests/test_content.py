"""
Tests for the theguardian_content.py
"""

import unittest
from theguardian import theguardian_content


class TestContent(unittest.TestCase):

    """
    Mainly built to test the functionality
    of the theguardian_content module.
    """

    def test_content_response_success_correct_details(self):

        api_key = "test"
        res = theguardian_content.Content(api_key).get_request_response()
        self.assertEqual(res.status_code, 200)

    def test_content_response_failure_incorrect_api_key(self):

        api_key = "tests"
        res = theguardian_content.Content(api_key).get_request_response()
        self.assertEqual(res.status_code, 401)

    def test_content_response_header(self):

        api_key = "test"
        res = theguardian_content.Content(api_key).response_headers()

        self.assertIs(type(res), dict)
        self.assertIn("pageSize", res.keys())
        self.assertIn("currentPage", res.keys())
        self.assertIn("pages", res.keys())
        self.assertNotIn("results", res.keys())

    def test_contents_find_by_id_correct_url(self):

        api_key = "test"
        ids = "technology/2014/feb/17/flappy-bird-clones-apple-google"
        res = theguardian_content.Content(api_key).find_by_id(ids)

        self.assertIs(type(res), dict)
        self.assertEqual(res['response']['results'][0]["id"], ids)

    def test_contents_find_by_id_incorrect_url(self):

        api_key = "test"
        ids = "technology/2014/feb/17/flappy-bird-clones-apple"
        res = theguardian_content.Content(api_key).find_by_id(ids)

        self.assertEqual(res['response']['results'], [])
        self.assertEqual(res['response']['pages'], 0)
        self.assertEqual(res['response']['total'], 0)

    def test_content_results(self):

        api_key = "test"
        ids = "technology/2014/feb/17/flappy-bird-clones-apple-google"
        content = theguardian_content.Content(api_key)
        res = content.find_by_id(ids)
        result = content.get_results(res)

        self.assertIs(type(result), list)
        self.assertEqual(result[0]['id'], ids)

    def test_content_with_headers(self):

        headers = {
            "q": "12 years a slave",
            "tag": "film/film,tone/reviews",
            "from-date": "2010-01-01",
            "order-by": "relevance",
            "show-fields": "starRating,headline,thumbnail,short-url",
        }
        content = theguardian_content.Content(api='test', **headers)
        res = content.get_content_response()
        result = content.get_results(res)

        self.assertIs(type(result), list)

    def test_content_get_result_with_exception(self):

        api_key = "test"
        section = theguardian_content.Content(api_key)

        self.assertRaises(TypeError, section.get_results, "some random text")

    def test_section_get_references_correct_pages(self):

        api_key = "test"
        content = theguardian_content.Content(api_key, **{
            "q": "apple",
            "section": "technology",
        })
        refs = content.get_references_in_page(page_number=1)
        refs2 = content.get_references_in_page()

        self.assertIs(type(refs), list)
        self.assertIs(type(refs2), list)

    def test_section_get_references_incorrect_pages(self):

        api_key = "test"
        content = theguardian_content.Content(api_key, **{
            "q": "apple",
            "section": "technology",
        })

        head = content.response_headers()

        self.assertRaises(ValueError, content.get_references_in_page, page_number=head["pages"] + 1)

if __name__ == "__main__":
    unittest.main()
