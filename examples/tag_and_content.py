"""
This example deals with returning content of specific tags.
"""
from theguardian import theguardian_tag
from theguardian import theguardian_content


# get the apple tags
headers = {
    "q": "apple",
    "section": "technology",
    "show-references": "all",
}
tag = theguardian_tag.Tag(api='test', **headers)

# get the results
tag_content = tag.get_content_response()
results = tag.get_results(tag_content)

# get results for specific tag
first_tag_apiUrl = results[0]["apiUrl"]

# use this api url to content
content = theguardian_content.Content(api='test', url=first_tag_apiUrl)

# get content response
content_response = content.get_content_response()
print(content_response)
