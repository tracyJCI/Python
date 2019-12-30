# Problem 6:  One might define a pattern of a character's name being mentioned as
# [A-Z][a-z.]+\s[A-Z][a-z]+
# Run this pattern over the text and show the results.
# Write all the *unique* values out to a text file (one result per line).
# In your narrative, analyse both why/when it works and fails. This should
# be a substantive answer, as there's a lot to talk about.

import re

with open('dracula.txt', 'r') as fin:
	drac = fin.read()

names = re.compile('([A-Z][a-z.]+\s[A-Z][a-z]+)')

found_names = re.findall(names, drac)

from collections import Counter
counted = Counter(found_names)
name_list = list(counted)

outfile = open('Hwk13_Q6_result.txt','w')
outfile.write('\n'.join(result for result in name_list))

