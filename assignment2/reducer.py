#!/usr/bin/python

import sys

hits = 0
for line in sys.stdin:
	path = line.strip()
	if path == "/assets/js/the-associates.js":
		hits += 1
print "hits were made to /assets/js/the-associates.js: "+str(hits)
