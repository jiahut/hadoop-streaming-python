#!/usr/bin/env python

from itertools import groupby, chain
from operator import itemgetter
from collections import Counter
import sys

def read_mapper_output_from(file, separator = '\t'):
	for line in file:
		yield line.rstrip().split(separator, 2)	

def main(separator = '\t'):
	data = read_mapper_output_from(sys.stdin, separator=separator)
	for uid_with_last4, group in groupby(data, itemgetter(0)):
		try:
			cards = ( "_".join([card,area]) for uid_with_last4, card, area in group)
			bigest,bigger = Counter(chain(cards,"0")).most_common(2)
			if bigest[0] == "0":
				uid,_ = uid_with_last4.split(":")
				card, area = bigger[0].split("_")
				print("%s%s%s%s%s" % (uid, separator, card, separator,area))
			elif bigger[0] == "0":
				uid,_ = uid_with_last4.split(":")
				card, area = bigest[0].split("_")
				print("%s%s%s%s%s" % (uid, separator, card, separator,area))
			elif not bigest[1] == bigger[1]:
				uid,_ = uid_with_last4.split(":")
				card, area = bigest[0].split("_")
				print("%s%s%s%s%s" % (uid, separator, card, separator,area))
		except ValueError:
			pass

if __name__ == '__main__':
	main()
