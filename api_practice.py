from urllib.request import urlopen
from urllib.error import HTTPError
import json

try:
    with urlopen("https://jsonplaceholder.typicode.com/posts/999999") as response:
        print("Статус:", response.status)
        data = json.loads(response.read().decode("utf-8"))
        print(data["title"])
except HTTPError as error:
    if error.code == 404:
        print("Публикация не найдена")
    else:
        print(error.code)
