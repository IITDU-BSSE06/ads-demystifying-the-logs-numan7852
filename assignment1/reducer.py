#!/usr/bin/python

import sys

hits = 0
for line in sys.stdin:
	ip = line.strip()
	if ip == "10.99.99.186":
		hits += 1
print "hits were made to 10.99.99.186 is: "+str(hits)
