"""
Query for a single content item and print its web title
"""
from theguardian import theguardian_content


ids = "commentisfree/2013/jan/16/vegans-stomach-unpalatable-truth-quinoa"
content = theguardian_content.Content(api="test")

single_id_content = content.find_by_id(ids)
results = content.get_results(single_id_content)

print("web url for {id}: {url}\n"
      .format(id=results[0]["id"], url=results[0]["webUrl"]))

"""
Print web title for a tag
"""

header = {
    "tag": "music/metal",
}
tag_content = theguardian_content.Content(api="test")

tag_content_response = content.get_content_response(header)
results = content.get_results(tag_content_response)

print("web title for {id}: {url}\n"
      .format(id=results[0]["id"], url=results[0]["webTitle"]))

"""
print web title for a section
"""

section_header = {
    "section": "environment"
}

section_content = theguardian_content.Content(api="test")

section_content_response = content.get_content_response(section_header)
results = content.get_results(section_content_response)

print("web title for {id}: {url}\n"
      .format(id=results[0]["id"], url=results[0]["webTitle"]))
