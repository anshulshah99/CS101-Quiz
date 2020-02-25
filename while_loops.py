'''
Created on DATE

@author: Anshul Shah

Module description
'''
i = 0
while i < len(lst):
    if lst[i] == el:
        lst = lst[:i] + lst[i+1:]
    else:
        i += 1
#this is correct!^

#make it incorrect by removing the else statement and having i always increment

#error, true, or false

(1 == 1) and (2 != 3 or 1/0 == 0)

if __name__ == '__main__':
    pass