import os
import sys
import time
import eventlet
from eventlet.green import urllib2

def fetch(url):
    try:
        print(url)
        response = urllib2.urlopen(url, timeout=15)
    except Exception as error:
        return url, ""
    return url, response.read()

def check_line(line):
    ip = line.replace('\n', '')
    if not ip_is_checked(ip):
        return "http://" + ip + "/"
    return ""

def ip_is_checked(ip):
    return os.path.isfile("./html/" + ip + ".html")

with open("80_results_ip_only.log") as file:
    urls = []
    if len(sys.argv) != 2:
        print("python http_test.py 91.153.81.15")
        sys.exit()
    skip_until = sys.argv[1] # ls -l html/ | tail -1
    if len(skip_until) < 7 or len(skip_until.split(".")) != 4:
        print("python http_test.py 91.153.81.15")
        sys.exit()
    print("Skip IP list until " + skip_until)
    # rm html/62.80.155.125.html
    for line in file:
        url = check_line(line)
        if skip_until and skip_until in url:
            print("Continue from IP=%s" % skip_until)
            skip_until = ""
        if skip_until:
            continue
        if url:
            urls.append(url)

pool = eventlet.GreenPool(size=10)

for url, body in pool.imap(fetch, urls):
    if body:
        ip = url.replace("http://", "").replace("/", "")
        text_file = open("./html/" + ip + ".html", "w")
        text_file.write(url + "\n\n" + body)
        text_file.close()
