#!/usr/bin/python

import sys

year9 = 0
year10 = 0
year11 = 0

for line in sys.stdin:
	file_hits = line.strip()	

	if "2009" in line:
		year9 += 1

	if "2010" in line:
		year10 += 1

	if "2011" in line:
		year11 += 1

print "2009 "+str(year9)
print "2010 "+str(year10)
print "2011 "+str(year11)
