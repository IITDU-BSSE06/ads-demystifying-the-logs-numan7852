#!/usr/bin/python

from urlparse import urlparse
import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        print urlparse(data[6]).path
