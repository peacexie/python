#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

def getHtml(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    #page = urllib.urlopen(url)
    #html = page.read()
    return html

html = getHtml("http://txjia.com/")

print(html)

"""

import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.python.org/events/python-events/')
soup = BeautifulSoup(resp.text, 'html.parser')

for li in soup.select('.list-recent-events > li'):
    print('title:',li.find('a').text)
    print('time:', li.find('time').text)
    print('location:', li.select_one('.event-location').text)
    print('*' * 100)

"""