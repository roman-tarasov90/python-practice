import requests

new_post = {"title": "Изучаю Python", "body": "Мой первый POST-запрос", "userId": 1}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts", json=new_post, timeout=10
)

print(response.status_code)
print(response.json())