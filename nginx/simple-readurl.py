import urllib.request
import re

user_agent = \
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = 'http://localhost:8080/nginx.log'
headers = {'User-Agent': user_agent}

request = urllib.request.Request(url, None, headers)
response = urllib.request.urlopen(request)
data = response.read()
data = data.decode('ISO-8859-1')
lines = data.splitlines(True)

count = 0
pattern = '.*Mozilla.*'
for line in lines:
    for match in re.finditer(pattern, line):
        count += 1

print(count)
# print(data)
