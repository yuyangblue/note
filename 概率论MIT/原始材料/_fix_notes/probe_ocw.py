# -*- coding: utf-8 -*-
"""探测 OCW 6.041SC 资源页 transcript PDF 链接结构"""
import urllib.request
import re
import sys

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=30).read().decode('utf-8', errors='replace')

url = sys.argv[1]
html = fetch(url)
pdfs = sorted(set(re.findall(r'href="([^"]*\.pdf[^"]*)"', html)))
print('PDF links on', url)
for p in pdfs:
    print(' ', p)
tr = re.findall(r'href="([^"]*transcript[^"]*)"', html, re.I)
print('transcript-ish:', tr)
