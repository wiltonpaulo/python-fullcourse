import urllib.request
import re


def get_logs(url):
    logs = urllib.request.urlopen(url)
    logs_html = logs.read()
    logs = logs_html.read().decode('utf-8')
    result = {}

    match_mozilla = re.search(r'.*', logs)
    result['mozilla'] = int(match_mozilla.group(1))
    return result


def main():
    # url = sys.argv[1]
    url = "http://localhost:8080/nginx.log"
    Total = None
    count = 0

    while True:
        logs = get_logs(url)
        result = print_stat(prev, data)
        if total is None:
            total = list(result)
        else:
            for i, v in enumerate(result):
                total[i] += v
        count += 1


main()
