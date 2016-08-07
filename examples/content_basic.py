from theguardian import theguardian_content

# create content
content = theguardian_content.Content(api='test')

# gets raw_response
raw_content = content.get_request_response()
print("Request Response status code {status}." .format(status=raw_content.status_code))
print("Request Response headers {header}." .format(header=raw_content.headers))

# content
print("Content Response headers {}." .format(content.response_headers()))

# get all results of a page
json_content = content.get_content_response()
all_results = content.get_results(json_content)
print("All results {}." .format(all_results))

# actual response
print("Response {response}" .format(response=json_content))
