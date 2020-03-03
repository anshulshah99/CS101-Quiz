'''
Created on DATE

@author: Anshul Shah

Module description
'''
import random
import copy

def append():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    sublst = random.choice([True, False])
    length = random.randint(3, 5)
    tup_lst = [random.choice(alphabet) for i in range(length)]
    to_append = random.randint(15, 45)
    if sublst:
        sub = [random.randint(1, 20) for i in range(random.randint(2, 4))]
        ind = random.randint(0, length-1)
        tup_lst[ind] = sub

    tup = tuple(tup_lst)
    tup_lst = copy.deepcopy(tup_lst)
    if sublst:
        work = random.choice([True, False])

        if work:
            question = rf"t = {tup}\ntup[{ind}].append({to_append})\nprint(t)"
            tup[ind].append(to_append)
            correct = tup
            wrong1 = r"AttributeError: ''tuple'' object has no attribute ''append''"
            tup_lst.append(to_append)
            wrong2 = tuple(tup_lst)
            wrong3 = tup_lst
            print(question, correct, wrong1, wrong2, wrong3)

    #For tuples have a reassignment
        have reassignment that work
        have reassignment that doesnt work, maybe have a list of len 1 like [1].


    #nested lists
    give part of code, and an output. say how to get to a certain output
if __name__ == '__main__':
    append()

