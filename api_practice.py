import requests

post_id = 5
url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

response = requests.get(url, timeout=10)

post = response.json()

print(response.status_code)
print(post["title"])
print(post["body"])