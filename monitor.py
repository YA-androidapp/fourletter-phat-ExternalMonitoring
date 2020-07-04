#!/usr/bin/env python
import fourletterphat
import requests


def monitor(url):
    response = requests.get(url)
    status_code = response.status_code

    fourletterphat.clear()
    fourletterphat.scroll_print(str(status_code) + ' ' + url, 0.1 if (200 == status_code) else 1 )

with open('urls.txt') as f:
    line = f.readline()
    while line:
        if line.startswith('http'):
            monitor(line.rstrip())
        line = f.readline()
