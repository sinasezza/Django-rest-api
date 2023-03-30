import requests

endpoint = 'http://localhost:8000/api/'  # localhost <=> 127.0.0.1

get_response = requests.get(endpoint,json={'product_id':123}) # HTTP GET REQUEST

# print(get_response.headers)
print(get_response.text)
print(get_response.json())
# print(get_response.status_code)