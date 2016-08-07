from theguardian import theguardian_content

# create content
content = theguardian_content.Content(api='test')
ids = "technology/2014/feb/17/flappy-bird-clones-apple-google"

res = content.find_by_id(ids)
result = content.get_results(res)

print("Result: {result}" .format(result=result))

# create content with filters
# for more filters refer
# http://open-platform.theguardian.com/documentation/search

headers = {
    "q": "12 years a slave",
    "tag": "film/film,tone/reviews",
    "from-date": "2010-01-01",
    "order-by": "relevance",
    "show-fields": "starRating,headline,thumbnail,short-url",
}
content = theguardian_content.Content(api='test', **headers)

res = content.get_content_response()
result = content.get_results(res)

print("Result: {result}" .format(result=result))
