#!/usr/bin/env python
import fourletterphat
import requests
import time


def monitor(url):
    response = requests.get(url)
    status_code = response.status_code

    fourletterphat.clear()

    fourletterphat.print_str(str(status_code))
    fourletterphat.show()
    time.sleep(5)

    fourletterphat.scroll_print(str(status_code) + ' ' + url + ' ' + str(status_code), 0.1 if (200 == status_code) else 1 )

    fourletterphat.print_number_str(str(status_code))
    fourletterphat.show()
    time.sleep(5)

    fourletterphat.clear()

with open('urls.txt') as f:
    line = f.readline()
    while line:
        if line.startswith('http'):
            monitor(line.rstrip())
        line = f.readline()
