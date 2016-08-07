from theguardian import theguardian_edition

# create edition
edition = theguardian_edition.Edition(api='test')

# gets raw_response
raw_content = edition.get_request_response()
print("Request Response status code {status}." .format(status=raw_content.status_code))
print("Request Response headers {header}." .format(header=raw_content.headers))

# content
print("Content Response headers {}." .format(edition.response_headers()))

# get all results of a page
json_content = edition.get_content_response()
all_results = edition.get_results(json_content)
print("All results {}." .format(all_results))

# actual response
print("Response {response}" .format(response=json_content))

# get all the sections webUrl
for result in all_results:
    print("{id} - {url}" .format(id=result["id"], url=result["webUrl"]))
