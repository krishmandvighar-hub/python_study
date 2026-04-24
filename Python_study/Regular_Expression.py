##RegEx Functions
##The re module offers a set of functions that allows us to search a string for a match:

##"Function"	"Description"
##findall   :Returns a list containing all matches
##search    :Returns a Match object if there is a match anywhere in the string
##split	    :Returns a list where the string has been split at each match
##sub	    :Replaces one or many matches with a string

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)#findall()
print(x)

import re

txt = "The rain in Spain"
x = re.search("\s", txt)#search()

print("The first white-space character is located in position:", x.start())

import re

txt = "The rain in Spain"
x = re.split("\s", txt)#split()"""we also use maxsplit ("\s", txt,1)"""
print(x)

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)#sub()"similarly count parameter("\s", "9", txt, 2)"
print(x)



##The Match object has properties and methods used to retrieve information about the search, and the result:
##
##.span()  :returns a tuple containing the start-, and end positions of the match.
##.string  :returns the string passed into the function
##.group() :returns the part of the string where there was a match

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())#span()
txt = "The rain in Spain"

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)#string()

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())#group()

