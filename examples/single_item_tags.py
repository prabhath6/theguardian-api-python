"""
Print the web title of every tag a content item has
for a single item.
"""
from theguardian import theguardian_content


headers = {
    "ids": "environment/2014/sep/14/invest-in-monitoring-and-tagging-sharks-to-prevent-attacks",
    "show-tags": "all",
}

content = theguardian_content.Content(api="test", **headers)
content_response = content.get_content_response()
results = content.get_results(content_response)
tags = results[0]["tags"]
webTitles = [tag["webTitle"] for tag in tags]

print("Title of tags {titles}" .format(titles=webTitles))

"""
Print the web title of each content item in the
editor's picks for the film tag.
"""

tag_headers = {
    "tag": "film/film"
}

tag_content = theguardian_content.Content(api="test", **tag_headers)
tag_content_response = tag_content.get_content_response()
results = tag_content.get_results(tag_content_response)
webTitles = [result["webTitle"] for result in results]

print("Title of content {titles}" .format(titles=webTitles))

"""
Print

1. the total number of content items.
2. web titles of 15 most recent items.

"""

olympic_header = {
    "q": "olympic",
    "from-date": "2010-08-08",
    "order-by": "newest"
}

olympic_content = theguardian_content.Content(api="test", **olympic_header)
olympic_response_headers = olympic_content.response_headers()

print("Total number of content items {total}."
      .format(total=olympic_response_headers["total"]))
