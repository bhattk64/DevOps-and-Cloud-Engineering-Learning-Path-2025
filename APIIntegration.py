#API integration
#using request library to fetch data from API

import requests

response=requests.get('https://jsonplaceholder.typicode.com/todos/1')
data=response.json()
print(data)

response=requests.request('GET','https://jsonplaceholder.typicode.com/todos/1')
data=response.json()
print(data)

response=requests.post('https://jsonplaceholder.typicode.com/todos/1')
data=response.json()
print(data)

response=requests.put('https://jsonplaceholder.typicode.com/todos/1')
data=response.json()
print(data)

response=requests.delete('https://jsonplaceholder.typicode.com/todos/1')
data=response.json()
print(data)