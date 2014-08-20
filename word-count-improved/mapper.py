#!/usr/bin/env python
import sys

def read_input(file):
	for line in file:
		yield line.split()

def main(separator = '\t'):
	for words in read_input(sys.stdin):
		for word in words:
			print("%s%s%d" % (word, separator, 1))

if __name__ == '__main__':
	main()
