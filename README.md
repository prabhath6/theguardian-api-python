# theguardian-api-python
This is a simple and lightweight Python client for thegaurdian api.

[![GNU license](https://camo.githubusercontent.com/940baba6e10de9f9bd8616bf42804619f2fb07fc/687474703a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d474e5576332d627269676874677265656e2e737667)](https://github.com/prabhath6/theguardian-api-python/blob/master/LICENSE) [![Gitter chat](https://badges.gitter.im/USER/REPO.png)](https://gitter.im/theguardian-api-python/developers_contributers_users)


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
### Tag endpoint
The tags endpoint returns all tags in the API. All Guardian content
is manually categorised using these tags, of which there are more than 50,000.
```python
"""
This example deals with returning references of specific tags.
"""
from theguardian import theguardian_tag

header = {
        "q": "apple",
        "section": "technology",
    }
t = theguardian_tag.Tag(api="test", **header)
print(t.get_references_in_page(1))

```
For more examples refer the [examples](https://github.com/prabhath6/theguardian-api-python/tree/master/examples) folder.
### Install
1. Create a virtual environment.
2. Clone or download the repo.
3. Pip install requirements.
4. Run the tests
5. Copy theguardian folder into virtual environment.

```
mkdir sample_folder
cd sample_folder
virtualenv -p /usr/bin/python3 guardian

git clone https://github.com/prabhath6/theguardian-api-python.git
cd theguardian-api-python

source ../guardian/bin/activate
pip install -r requirements.txt

python test.py

cp -r theguardian ../guardian/lib/python3.5
```
#### Notes
1. Requires python3.
2. Designed to work with only json data.
3. Built as a simple weekend project.
4. Refer examples for better understanding.

### Notes on Patches/Pull requests
* Fork the repo.
* Add features or fix bugs.
* Add tests to features or bug fixes.
* Send pull requests once done building.

