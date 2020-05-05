'''
Created on DATE

@author: Anshul Shah

Module description
'''
import random
import copy

def append():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    sublst = random.choice([True, True])
    length = random.randint(3, 5)
    tup_lst = [random.choice(alphabet) for i in range(length)]
    to_append = random.randint(15, 45)
    if sublst:
        sub = [random.randint(1, 20) for i in range(random.randint(1, 3))]
        ind = random.randint(0, length-1)
        tup_lst[ind] = sub

    tup = tuple(tup_lst)
    tup_lst = copy.deepcopy(tup_lst)
    if sublst:
        work = random.choice([True, False])

        if work:
            question = rf"t = {tup}\nt[{ind}].append({to_append})\nprint(t)"
            tup[ind].append(to_append)
            correct = tup
            wrong1 = r"AttributeError: 'tuple' object has no attribute 'append'"
            tup_lst.append(to_append)
            wrong2 = tuple(tup_lst)
            wrong3 = tup_lst
            qid = random.randint(1000, 15000)
            return ("INSERT INTO questions VALUES({}, 'Tuples', 'Appending', '{}', '{}', '{}', '{}', '{}');".format(qid, question.replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))

        if not work:
            question = rf"t = {tup}\nt.append({to_append})\nprint(t)"
            tup[ind].append(to_append)
            correct = r"AttributeError: 'tuple' object has no attribute 'append'"
            wrong1 = tup
            tup_lst.append(to_append)
            wrong2 = tuple(tup_lst)
            wrong3 = tup_lst
            qid = random.randint(1000, 15000)
            return ("INSERT INTO questions VALUES({}, 'Tuples', 'Appending', '{}', '{}', '{}', '{}', '{}');".format(qid, question.replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))
    return None

def reassign_sub():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    length = random.randint(3, 5)
    tup_lst = [random.choice(alphabet) for i in range(length)]
    to_append = random.choice([random.randint(15, 45), [random.randint(1, 20) for i in range(random.randint(1, 3))]])

    sub = [random.randint(1, 20) for i in range(random.randint(1, 3))]
    ind = random.randint(0, length - 1)
    tup_lst[ind] = sub
    new_ind = random.choice([random.randint(0, length - 1), random.randint(0, length - 1), ind])
    tup = tuple(tup_lst)
    tup_lst = copy.deepcopy(tup_lst)
    question = rf"t = {tup}\nt[{new_ind}] = {to_append}\nprint(t)"
    correct = r"TypeError: 'tuple' object does not support item assignment"
    tup_lst[new_ind] = to_append
    wrong1 = tuple(tup_lst)
    wrong2 = to_append
    wrong3 = tup_lst
    qid = random.randint(1000, 15000)
    return ("INSERT INTO questions VALUES({}, 'Tuples', 'Reassignment', '{}', '{}', '{}', '{}', '{}');".format(qid, question.replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))

    #Reassign a sublist, doesn't work
    #Reassign value in a sublist, works
    #Reassign another value, doesn't work
    #Reassign entire tuple, works


def reassign_val():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    length = random.randint(3, 5)
    tup_lst = [random.choice(alphabet) for i in range(length)]
    to_append = random.randint(5, 25)
    sublst_len = random.choice([1, 1, 2, 3])
    sub = [random.randint(1, 20) for i in range(sublst_len)]
    ind = random.randint(0, length - 1)
    tup_lst[ind] = sub
    tup = tuple(tup_lst)
    tup_lst = copy.deepcopy(tup_lst)
    sec_ind = random.randint(0, sublst_len)
    question = rf"t = {tup}\nt[{ind}][{sec_ind}] = {to_append}\nprint(t)"
    tup_lst[ind] = to_append
    if sec_ind == sublst_len:
        correct = "IndexError: Index out of bounds"
        tup[ind][-1] = to_append
        wrong2 = tup
    else:
        tup[ind][sec_ind] = to_append
        correct = tup
        wrong2 = tuple(tup_lst)
    wrong1 = r"TypeError: 'tuple' object does not support item assignment"
    wrong3 = tup_lst
    qid = random.randint(1000, 15000)
    return ("INSERT INTO questions VALUES({}, 'Tuples', 'Reassignment', '{}', '{}', '{}', '{}', '{}');".format(qid, question.replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))


def reassign_tup():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    length = random.randint(3, 5)
    tup_lst = [random.choice(alphabet) for i in range(length)]
    new_tup = [random.choice(alphabet) for i in range(length)]
    sub = [random.randint(1, 20) for i in range(random.randint(1, 2))]
    ind = random.randint(0, length - 1)
    tup_lst[ind] = sub
    tup = tuple(tup_lst)
    new_ind = random.randint(0, length-1)
    part_ques = random.choice(["t", f"t[{new_ind}]"])
    question = rf"t = {tup}\ns = {part_ques}\nt = {tuple(new_tup)}\nprint(t)"
    correct = tuple(new_tup)
    if part_ques == "t":
        wrong1 = r"TypeError: 'tuple' object does not support item assignment"
        wrong2 = tup
        wrong3 = sub
    else:
        wrong1 = r"TypeError: 'tuple' object does not support item assignment"
        wrong2 = tup
        wrong3 = tup[new_ind]
    qid = random.randint(1000, 15000)
    return ("INSERT INTO questions VALUES({}, 'Tuples', 'Reassignment', '{}', '{}', '{}', '{}', '{}');".format(qid, question.replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))




    #nested lists
    #give part of code, and an output. say how to get to a certain output
if __name__ == '__main__':
    for i in range(50):
        print(append())
        print(reassign_sub())
        print(reassign_val())
        print(reassign_tup())

