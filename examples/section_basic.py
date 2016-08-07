from theguardian import theguardian_section

# create section
section = theguardian_section.Section(api='test')

# gets raw_response
raw_section_content = section.get_request_response()
print("Request Response status code {status}." .format(status=raw_section_content.status_code))
print("Request Response headers {header}." .format(header=raw_section_content.headers))

# content
print("Section Response headers {}." .format(section.response_headers()))

# get all results of a page
json_content = section.get_content_response()
all_results = section.get_results(json_content)
print("All results {}." .format(all_results))

# actual response
print("Response {response}" .format(response=json_content))
