import re
def specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(specific_char("ABCDEFabcdef123450")) 
print(specific_char("*&%@#!}{"))
"""
ouput
True
False"""

import re
def text(text):
	patterns='ab.*$'
	if re.search(patterns,text):
		return "This string matches the pattern"
	else:
		return "This string doesn't match"
print(text("cook"))
print(text("able"))
"""
output
This string doesn't match
This string matches the pattern"""

import re
def end_num(string):
	text=re.compile(r".*[0-9]$")
	if text.match(string):
		return "This string contains a number at end."
	else:
		return "This string doesn't contain a number at end."
print(end_num("kavya22"))
print(end_num("kavya"))
"""
output
This string contains a number at end.
This string doesn't contain a number at end."""

import re
results = re.finditer(r"([0-9]{1,3})", "the  numbers are  1, 12, 60, 956, 345 ")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))
"""
output
Number of length 1 to 3
1
12
60
956
345"""

import re
def text_match(text):
	pattern='^[A-Z]*$'
	if re.search(pattern,text):
		return "This string contains only Uppercase."
	else:
		return "This doesn't contain only uppercase."
print(text_match("PYTHON"))
print(text_match("programming"))
"""
output
This string contains only Uppercase.
This doesn't contain only uppercase."""



	 
