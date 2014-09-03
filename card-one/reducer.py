#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
from collections import Counter
import sys

def read_mapper_output_from(file, separator = '\t'):
	for line in file:
		yield line.rstrip().split(separator, 2)	

def main(separator = ','):
	data = read_mapper_output_from(sys.stdin)
	for uid_with_last4, group in groupby(data, itemgetter(0)):
		try:
			cards = ( "_".join([card,area]) for uid_with_last4, card, area in group)
			top2 = Counter(cards).most_common(2)
			if len(top2) > 1:
				bigest,bigger = top2
				if not bigest[1] == bigger[1]:
					uid,_ = uid_with_last4.split(":")
					card, area = bigest[0].split("_")
					print("%s%s%s%s%s" % (uid, separator, card, separator,area))
			else:
				bigest = top2[0]
				uid,_ = uid_with_last4.split(":")
				card, area = bigest[0].split("_")
				print("%s%s%s%s%s" % (uid, separator, card, separator,area))
				
		except ValueError:
			pass

if __name__ == '__main__':
	main()
