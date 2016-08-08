"""
This example deals with returning references of specific tags.
"""
from theguardian import theguardian_tag

header = {
        "q": "apple",
        "section": "technology",
    }
t = theguardian_tag.Tag("test", **header)
print(t.get_references_in_page(1))
