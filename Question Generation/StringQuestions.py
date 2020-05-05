'''
Created on Oct 5, 2019

@author: Alexander
'''
import os, random

fname = "jacobs.txt"

with open(fname) as f:
    wholeFile = f.read()

wholeFile = wholeFile.replace('"', "")
wholeFile = wholeFile.replace("'", "")
sentences = [s.strip() for s in wholeFile.split(".") if s.strip() != ""]

#random.seed(14)
sentence = ""
while len(sentence) == 0 or len(sentence) < 30 or len(sentence) > 50:
    i = random.randint(0, len(sentences)-1)
    sentence = sentences[i]
say = sentence + "."
#print(sentences[0:5])
print("say = '" + say + "'")

#print(len('Old McDonald had a farm. Ee-igh, ee-igh, oh!'))
showAns = True
i = random.randint(-5, -2)
print("\nsay[%0.0d:]" % i)
ans = say[i]
if showAns:
    print("Answer: '%s'" % ans)
    
d = {}
for ltr in say:
    if ltr not in "!. ?":
        d[ltr] = say.count(ltr)
#print(d)

splitChar = ""
while len(splitChar) == 0 or d[splitChar] < 3:
    splitChar = list(d.keys())[random.randint(0, len(d)-1)]
print("\nlen(say.split('%s'))" % splitChar)
ans = len(say.split(splitChar))
if showAns:
    print("Answer: %s" % ans)
