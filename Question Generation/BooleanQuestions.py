'''
Created on Oct 5, 2019

@author: Alexander
'''
import os, random
showAns = True
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
    