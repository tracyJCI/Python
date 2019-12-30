#KJC4 4CREDITS
import re

# read in dracula

with open('dracula.txt', 'r') as fin:
	drac = fin.read()

# =======================================================
# Problem 1:
# write a regex that detects a tuple of (day_num, month_name)
# for our purposes, a date looks like:
# _24 July.
# _26 May._
# you'll need to explore the text to find these
# you may ignore any dates that are ranges or otherwise nonspecific
# You may also ignore any mentions of _later_ and not count those

# warning: some of these statements will be times
# instead of dates, and you'll need to figure out how to
# get rid of those


dates = re.compile('_([0-9]+) ([A-Z][a-z]+)')

found_dates = re.findall(dates, drac)

print(len(found_dates))  # you should find at least 165 dates

# If you find more, I want you to address that in your narrative
# and explore what extra you might be finding.  This means you need
# to look at the results in the context of the dracula.txt file.
# There isn't a specific 'right' answer here, but I want you to explain
# the types of dates that you're grabbing.


# =======================================================
# Problem 2: How many dates are repeated?
# Show how you determine this.

from collections import Counter

counted = Counter(found_dates)


# now you...

repeateddates=[]
for date, count in counted.items():
	if count>1:
		print(date,count)
		repeateddates.append(count) # or repeateddates+=1
print(len(repeateddates))

# =======================================================
# Problem 3: Which date is the most common?
# (There is only 1)
# determine this with code and show how
mostcommon=[]
for count in counted.most_common():
	if count[1]>1:
		mostcommon.append(count)
	else:break
print('This is the most common',mostcommon[0])


# =======================================================
# 4 CREDIT HOUR STUDENTS, YOUR FATE CONTINUES BELOW
# =======================================================

# Problem 4:
# Create a regular expression that finds all lines that begin and end with _
# tip: do not use .startswith or .endswith. You should use a regex
# Remember how lines are defined in text
# describe in your narrative what these appear to mean

underscores = re.compile('\n(_.*_)\n')

all_unders = re.findall(underscores, drac)
print(len(all_unders))

for unders in all_unders:
    print(unders)


# =======================================================
# Problem 5: Which months have dates?
# Create a dictionary that counts how many dates within each month were mentioned
# The month should be the key and the count should be the value. Example:
# {"January": 10, "February": 10...} data completely made up

dates_2 = re.compile('(_[0-9]{1,2}\s[A-Z][a-z]+)')

found_dates_2 = re.findall(dates_2, drac)


counts = dict()

for date in found_dates_2:
	if date[3:].lstrip() not in counts:
		counts[date[3:].lstrip()] = 1
	else:
		counts[date[3:].lstrip()] += 1

print(counts)

# =======================================================
# Problem 6:  One might define a pattern of a character's name being mentioned as
# [A-Z][a-z.]+\s[A-Z][a-z]+
# Run this pattern over the text and show the results.
# Write all the *unique* values out to a text file (one result per line).
# In your narrative, analyse both why/when it works and fails. This should
# be a substantive answer, as there's a lot to talk about.


names = re.compile('([A-Z][a-z.]+\s[A-Z][a-z]+)')

found_names = re.findall(names, drac)


counted_2 = Counter(found_names)

name_list = list(counted_2)

outfile = open('Hwk13_Q6.txt','w')
outfile.write('\n'.join(result for result in name_list))




