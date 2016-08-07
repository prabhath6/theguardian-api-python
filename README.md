# theguardian-api-python
This is a simple and lightweight Python client for thegaurdian api.

### theguardian Documentation
1. [Overview](http://open-platform.theguardian.com/documentation/)
2. [Content](http://open-platform.theguardian.com/documentation/search)
3. [Tags](http://open-platform.theguardian.com/documentation/tag)
4. [Section](http://open-platform.theguardian.com/documentation/section)
5. [Edition](http://open-platform.theguardian.com/documentation/edition)
6. [Single Item](http://open-platform.theguardian.com/documentation/item)

##### theguardian provides several endpoints to retrieve different items:

* Content
* Tags
* Sections
* Editions
* Single item

##### For each endpoint:

* results can be filtered using parameters.
* response contains minimal detail by default but more data can be exposed using parameters.
* results are returned as paginated list of containing, by default, 10 entries per page.

### Python Content endpoint
This Content module can be used as an interface for the content endpoint provided
by theguardian.
```python
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
```
For more examples refer the [examples](https://github.com/prabhath6/theguardian-api-python/tree/master/examples) folder.
