import re

url_list = [
    "http://twitter.com/wiltonpaulo",
    "http://www.twitter.com/wiltonpaulo",
    "https://twitter.com/wiltonpaulo",
    "https://www.twitter.com/wiltonpaulo",
    "twitter.com/wiltonpaulo",
    "www.twitter.com/wiltonpaulo",
    "www.google.com/wiltonpaulo",
]


for url in url_list:
    if username := re.search(
        "^(?:^https?://)?(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE
    ):
        print(username.group(1))
    else:
        print("invalid string")
