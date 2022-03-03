import requests
url_method = "https://playground.learnqa.ru/ajax/api/compare_query_type"

response1 = requests.post(url_method)
print(response1.text)
response2 = requests.head(url_method)
print(response2)
response3 = requests.get(url_method, params={"method": "GET"})
print(response3.text)

options = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]
get_lists = []
post_lists = []
put_lists = []
delete_lists = []
for option in options:
    get_response = requests.get(url_method, params=option)
    get_lists.append(get_response.text)

    post_response = requests.post(url_method, data=option)
    post_lists.append(post_response.text)

    put_response = requests.put(url_method, data=option)
    put_lists.append(put_response.text)

    delete_response = requests.delete(url_method, data=option)
    delete_lists.append(delete_response.text)

print(get_lists)
print(post_lists)
print(put_lists)
print(delete_lists)

