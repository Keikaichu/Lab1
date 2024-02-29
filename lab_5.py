import re
f = open('row.txt','r', encoding='utf-8')
date = f.read()
x=re.findall("о.?п", date) # работает
print(x)

#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
''' 
?	Zero or one occurrences	"he.?o"
\S Returns a match where the string DOES NOT contain a white space character
'''
test1 ="aqua abobus abbus abberation"
x=re.findall(r"\S*a{1}b\S*", test1)
print(x)
print("-----------------------------")

#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
'''
{} Exactly the specified number of occurrences	"he.{2}o"	
\S Returns a match where the string DOES NOT contain a white space character
'''
test1 ="aaqua aaabobus aabbus aabbberation"
x=re.findall(r"\S*a{2,3}b\S*", test1)
print(x)
print("-----------------------------")

#Write a Python program to find sequences of lowercase letters joined with a underscore.

test1 ="Under_Score notunderscore"
x=re.findall(r"\S*_\S*", test1)
print(x)
print("-----------------------------")

#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

test1 ="Karlah gale"
x=re.findall(r"\S*[A-Z][a-z]\S*", test1)
print(x)
print("-----------------------------")


#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
test1 ="aqweb aqwea"
x=re.findall(r"a\w*b", test1)
print(x)
print("-----------------------------")

#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

test1 = "Rin pointed gun at him. Not gonna lie, he'll die tonight."
x = re.sub("[.,\s]", ":", test1)
print(x)
print("-----------------------------")

#Write a python program to convert snake case string to camel case string.

test1 = "Snake_people"
x = re.sub(r'_([\w])', lambda x: x.group(1).upper(), test1)
print(x)
print("-----------------------------")

#Write a Python program to split a string at uppercase letters.
test1 = "Rin Not."
x = list(filter(None, re.split("[A-Z]", test1)))
print(x)
x = re.findall(r'[A-Z][^A-Z]*', test1)
print(x)
print("-----------------------------")

#Write a Python program to insert spaces between words starting with capital letters.

test1 = "NeverGonnaGiveYouUp"
x = re.sub(r'(\w)([A-Z])', lambda x: x. group(1) + " " + x.group(2), test1)
print(x)
print("-----------------------------")

#Write a Python program to convert a given camel case string to snake case.

test1 = "NeverGonnaGiveYouUp"
x = re.sub(r'(\w)([A-Z])', lambda x: x. group(1) + "_" + x.group(2), test1)
print(x)
print("-----------------------------")
