#!/usr/bin/env python
import sys

def read_from(file, seg = ","):
	for line in file:
		yield line.split(seg)

def main():
	for mark,uid,card,_ in read_from(sys.stdin):
		print("%s\t%s" % (":".join([uid,card]), mark))

if __name__ == '__main__':
	main()
