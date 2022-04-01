import urllib.request
import re
import sys

url = sys.argv[1]
# https://storage.googleapis.com/nginx_log_parsing.interviews.barefootcoders.com/example_case_1.access.log
# https://storage.googleapis.com/nginx_log_parsing.interviews.barefootcoders.com/example_case_2.access.log


def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)
    for number in unique_numbers:
        list_of_unique_numbers.append(number)
    return list_of_unique_numbers


def solution(access_log_uri):
    user_agent = \
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    headers = {'User-Agent': user_agent}

    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    data = data.decode('ISO-8859-1')
    lines = data.splitlines(True)

    authenticated_addr = set()
    sensitive_request_addr = set()
    # pattern = '.*POST /login HTTP/1.1" 200.*'
    pattern_authentication = '.*\s/login\sHTTP/.*"\s200.*'
    pattern_sensitive = '.*/sensitiveAction.*'
    for line in lines:
        # print(line)
        for match in re.finditer(pattern_authentication, line):
            faddr = re.findall(
                r"^\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)
            addr = str(faddr).replace(
                '[', '').replace(']', '').replace('\'', '')
            authenticated_addr.add(addr)
            #print(f"auth_list: {authenticated_addr}")
        for match in re.finditer(pattern_sensitive, line):
            faddr = re.findall(
                r"^\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)
            addr = str(faddr).replace(
                '[', '').replace(']', '').replace('\'', '')
            if (addr not in authenticated_addr):
                sensitive_request_addr.add(addr)
                #print(f"addr not in list: {addr}")

    data = get_unique_numbers(sensitive_request_addr)
    count = len(data)
#    for element in data:
#        count += 1
#        print(element)
#    print(int(count))
    print(len(data))


solution(url)
