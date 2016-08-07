from theguardian import theguardian_content


# create content
headers = {
    "page-size": 5,
    "order-by": "newest",
}
content = theguardian_content.Content(api='test', **headers)

# looping through pages
response_headers = content.response_headers()
total_pages = response_headers["pages"]

# print apiUrls for all the results in first 5 pages
required_pages = 5
required_urls = []

if total_pages > required_pages:

    headers = {
        "page-size": 5,
        "order-by": "newest",
    }
    content2 = theguardian_content.Content(api='test', **headers)

    for page in range(1, required_pages+1):
        res = content2.get_content_response(headers={"page": page})
        page_results = res['response']['results']
        for result in page_results:
            required_urls.append(result["apiUrl"])

for url in required_urls:
    print(url)
