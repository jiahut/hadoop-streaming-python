#!/usr/bin/env python
import sys

def read_from(file, seg = ","):
	for line in file:
		yield line.split(seg)

def main(separator = '\t'):
	for uid,card,area in read_from(sys.stdin):
		print("%s%s%s%s%s" % (":".join([uid, card[-4:]]), separator, card, separator, area.strip()))

if __name__ == '__main__':
	main()
