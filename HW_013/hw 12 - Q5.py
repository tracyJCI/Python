# Problem 5: Which months have dates?
# Create a dictionary that counts how many dates within each month were mentioned
# The month should be the key and the count should be the value. Example:
# {"January": 10, "February": 10...} data completely made up

import re

with open('dracula.txt', 'r') as fin:
	drac = fin.read()

dates = re.compile('(_[0-9]{1,2}\s[A-Z][a-z]+)')

found_dates = re.findall(dates, drac)


counts = dict()

for date in found_dates:
	if date[3:].lstrip() not in counts:
		counts[date[3:].lstrip()] = 1
	else:
		counts[date[3:].lstrip()] += 1

print(counts)
