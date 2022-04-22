import re


mypattern = ".*\[(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\]\s([a-z]+).*"  # full regex and get values
# mypattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
mytext = "Number is [192.168.0.250] house 5"
search = re.search(mypattern, mytext)

# print(search[0], search.group())
print(search[1])
