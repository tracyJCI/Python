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


dates = re.compile('_[0-9]+ [A-Z][a-z]+')

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

print(counted) 
# now you...
repeateddates=[] #or repeateddates=0
for date, count in counted.items():
	if count>1:
		print(date,count)
		repeateddates.append(count) # or repeateddates+=1
print(repeateddates)
print(len(repeateddates))

# =======================================================
# Problem 3: Which date is the most common?
# (There is only 1)
# determine this with code and show how
mostcommon=[]
for count in counted.most_common():
	if count[1]>1:
		mostcommon.append(count)
	else :break
print("This is the most common",mostcommon[0])   # should be 1october 7

# =======================================================
# 4 CREDIT HOUR STUDENTS, YOUR FATE CONTINUES BELOW
# =======================================================

# Problem 4:
# Create a regular expression that finds all lines that begin and end with _
# tip: do not use .startswith or .endswith. You should use a regex
# Remember how lines are defined in text
# describe in your narrative what these appear to mean

underscores = re.compile('\n_.*_\n')

allunders = re.findall(underscores, drac)
print(allunders)

for unders in underscores:
	print(unders)

# =======================================================
# Problem 5: Which months have dates?
# Create a dictionary that counts how many dates within each month were mentioned
# The month should be the key and the count should be the value. Example:
# {"January": 10, "February": 10...} data completely made up

months = re.compile('''_[0-9]+ [A-Z][a-z]+|[0-9]+? [A-Z][a-z]+ [0-9]{2}''')

months_all = re.findall(months, drac)
print(months_all)

#for date in found_dates:
#	if date(3:).lstrip() not in

monthDict={}
for date in found_dates:
	month=re.compile('(January|February|....Dec)')
	found_month=re.findall(month,date)
	monthDict.setDefault()


# =======================================================
# Problem 6:  One might define a pattern of a character's name being mentioned as
# [A-Z][a-z.]+\s[A-Z][a-z]+
# Run this pattern over the text and show the results.
# Write all the *unique* values out to a text file (one result per line).
# In your narrative, analyse both why/when it works and fails. This should
# be a substantive answer, as there's a lot to talk about.






