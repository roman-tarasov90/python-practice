import requests

with requests.get("https://jsonplaceholder.typicode.com/posts/2", timeout=10) as response:
    print("Статус:", response.status_code)
    data = response.json()
    print(data["title"])
