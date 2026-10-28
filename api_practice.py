import requests

headers = {
    "Accept": "application/json"
}

response = requests.get("https://jsonplaceholder.typicode.com/posts/1", headers=headers, timeout=10)

print(response.json()["title"])
print(response.status_code)
print(response.headers["Content-Type"])