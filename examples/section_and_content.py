"""
This example deals with returning content of section.
"""
from theguardian import theguardian_section
from theguardian import theguardian_content


# get the sports sections
headers = {"q": "sports"}  # q=query parameter/search parameter
section = theguardian_section.Section(api='test', **headers)

# get the results
section_content = section.get_content_response()
results = section.get_results(section_content)

# get different editions from the results
editions = results[0]['editions']

# get uk/sports edition apiUrl
uk_sports = [edi["apiUrl"] for edi in editions if edi["id"] == "uk/sport"][0]

# use this api url to sports content
content = theguardian_content.Content(api='test', url=uk_sports)

# get section response
content_response = content.get_content_response()
print(content_response)
