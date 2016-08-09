"""
1. Get total number of available tags.
2. print first 15 web title for tags of type 'contributor'
"""
from theguardian import theguardian_tag


# 1.
tag = theguardian_tag.Tag(api="test")
tag_response_headers = tag.response_headers()
print("Total number of tags: {tags_count}."
      .format(tags_count=tag_response_headers["total"]))

# 2.
headers = {
    "type": "contributor",
    "order-by": "newest",
    "page-size": 15,
}
tag_contributor = theguardian_tag.Tag(api="test", **headers)
tag_contributor_data = tag_contributor.get_content_response()
results = tag_contributor.get_results(tag_contributor_data)

webTitles = [result["webUrl"] for result in results]
print("Web Tiles {title}." .format(title=webTitles))
