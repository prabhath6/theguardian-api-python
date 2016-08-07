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

### Content endpoint
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
### Section endpoint
This Section module can be used as an interface for the sections endpoint provided
by theguardian. This can be used to access various sections within the theguardian's
data. Some example of sections query parameters(q) are business, sports and technology.
```python
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
```
### Edition endpoint
The editions endpoint returns all editions in the API.
Editions are the different front main pages of the Guardian site we have.
At current thguardian supports editions for the United Kingdom(uk), the United States(us) and Australia(au).
```python
from theguardian import theguardian_edition

# create edition
edition = theguardian_edition.Edition(api='test')

# get all results of a page
json_content = edition.get_content_response()
all_results = edition.get_results(json_content)

# get all the sections webUrl
for result in all_results:
    print("{id} - {url}" .format(id=result["id"], url=result["webUrl"]))

```
For more examples refer the [examples](https://github.com/prabhath6/theguardian-api-python/tree/master/examples) folder.
