import requests
import json
import re

response = requests.get(
    "https://api.stackexchange.com/2.3/questions?page=4&pagesize=100&order=desc&sort=activity&site=stackoverflow"
)

count = 0
for data in response.json()["items"]:
    if re.search("python", data["title"]):
        print(data["title"])
        print(data["link"])
        print("")
        count += 1
print(count)
