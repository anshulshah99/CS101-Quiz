'''
Created on Oct 5, 2019

@author: Alexander
'''
import os, random

fname = os.path.join("files", "jacobs.txt")

with open(fname) as f:
    wholeFile = f.read()

wholeFile = wholeFile.replace('"', "")
wholeFile = wholeFile.replace("'", "")
sentences = [s.strip() for s in wholeFile.split(".") if s.strip() != ""]

random.seed(14)
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

print()
b = random.choice([True, False])
b2 = not b
i = random.randint(0,1)
if i == 0:
    print("((%s or 1/0) and %s)" % (str(b), str(b2)))
    try:
        ans = ((b or 1/0) and b2)
    except:
        ans = "Error"
if i == 1:
    print("((%s and 1/0) or %s)" % (str(b), str(b2)))
    try:
        ans = ((b and 1/0) or b2)
    except:
        ans = "Error"
if showAns:
    print("Answer: %s" % ans)
    
#print(eval("True and False"))