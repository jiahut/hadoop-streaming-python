#!/usr/bin/env python

from itertools import groupby, chain
from operator import itemgetter
from collections import Counter
import sys

def read_mapper_output_from(file, separator = ','):
	for line in file:
		yield line.rstrip().split(separator, 2)	

def main():
	data = read_mapper_output_from(sys.stdin)
	for uid_card, group in groupby(data, itemgetter(0)):
		marks = [ mark for mark in group ]
		if len(marks) == 1:
			uid_card, mark = marks[0]	
			uid, card = uid_card.split("_")
			if mark is 'A':
				print("%s,%s" %(uid, card))

if __name__ == '__main__':
	main()
