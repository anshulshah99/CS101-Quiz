'''
Created on DATE

@author: Anshul Shah

Module description
'''
import random
import copy

def list_append():
    rand_lists = []
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in range(8):
        tmp = [ "{}".format(random.choice(alphabet)*random.randint(2, 4)) for j in range(random.choice([1, 2, 2, 3, 3]))]
        rand_lists.append(tmp)
    rand_nums = []
    rand_deep = rand_lists[6] + [[random.randint(1, 4), random.randint(1, 4)]]
    for i in range(7):
        tmp = random.randrange(11, 100, 11)
        rand_nums.append(tmp)
    rand_len = random.randint(3, 5)
    final_lst = [random.choice([rand_nums[i], rand_lists[i]]) for i in range(rand_len)]
    final_lst.append(rand_deep)
    depth = random.choice([1, 2, 2, 3, 3])
    depth = 1
    #depth = 3
    #print(final_lst)
    index = 2
    if depth == 3:
        index = rand_len
        second_ind = len(rand_deep) - 1
    else:
        for i in range(len(final_lst)):
            if depth == 2 and type(final_lst[i]) is list:
                index = i
                break
    to_append = random.choice([rand_nums[6], rand_lists[7]])

    if depth == 1:
        question = r"lst = {}\nlst.append({})".format(final_lst, to_append).replace("'", "''")
        correct = final_lst + [to_append]
        if type(to_append) is int:
            wrong1 = final_lst + [[to_append]]
            wrong2 = 'TypeError: Can''t append int to type list'
            final_lst[-1].append(to_append)
            wrong3 = copy.deepcopy(final_lst)
        if type(to_append) is list:
            wrong1 = final_lst + to_append
            wrong2 = 'TypeError: Can''t append list to type list'
            final_lst[-1].append(to_append)
            wrong3 = copy.deepcopy(final_lst)
    if depth == 2:
        question = r"lst = {}\nlst[{}].append({})".format(final_lst, index, to_append).replace("'", "''")
        c = copy.deepcopy(final_lst)
        c[index].append(to_append)
        correct = c
        if type(to_append) is int:
            wrong1 = final_lst + [to_append]
            wrong2 = 'TypeError: Can''t append int to type list'
            tmp = copy.deepcopy(final_lst)
            tmp[index] = to_append
            wrong3 = tmp
        if type(to_append) is list:
            wrong1 = final_lst + to_append
            wrong2 = 'TypeError: Can''t append list to type list'
            final_lst[index].extend(to_append)
            wrong3 = final_lst
    if depth == 3:
        question = r"lst = {}\nlst[{}][{}].append({})".format(final_lst, index, second_ind, to_append).replace("'", "''")
        c = copy.deepcopy(final_lst)
        c[index][second_ind].append(to_append)
        correct = c
        if type(to_append) is int:
            tmp = copy.deepcopy(final_lst)
            wrong1 = tmp + [to_append]
            wrong2 = 'TypeError: Can''t append int to type list'
            final_lst[index].append(to_append)
            wrong3 = final_lst
        if type(to_append) is list:
            wrong1 = final_lst + to_append
            tmp = copy.deepcopy(final_lst)
            tmp[index][second_ind].extend(to_append)
            wrong2 = tmp
            final_lst[index] = to_append
            wrong3 = final_lst
    qid = random.randint(400, 10000)
    return(r"INSERT INTO questions VALUES({}, 'Lists', 'Appending', '{}', '{}', '{}', '{}', '{}');".format(qid, question, str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))

def list_add():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    tmp = [random.randint(1, 10) for j in range(random.choice([3, 4, 5]))]
    type_append = random.choice(["int", "lst", "sublst"])
    if type_append == "int":
        to_append = random.randint(5, 70)
        correct = 'TypeError. Can''t add type int to list'
    else:
        to_append = [random.randint(1, 9) for i in range(random.choice([1, 1, 2, 3]))]
        if type_append == "sublst":
            to_append.append(["{}".format(random.choice(alphabet)),  "{}".format(random.choice(alphabet)) , "{}".format(random.choice(alphabet))])
        correct = tmp + to_append
    question = r'lst = {}\ntmp = {}\nfinal = lst + tmp\nWhat is the value of final after the above code runs?'.format(tmp, to_append).replace("'", "''")
    if type_append == "int":
        wrong1 = tmp + [to_append]
        c = copy.deepcopy(tmp)
        wrong2 = [c[i] + to_append for i in range(len(c))]
        c[-1] += to_append
        wrong3 = c
    if type_append == "lst":
        c = copy.deepcopy(tmp)
        c.append(to_append)
        wrong1 = c
        wrong2 = 'TypeError: Can''t add a list to type list'
        new = copy.deepcopy(tmp)
        for i in range(len(to_append)):
            new[i]+= to_append[i]
        wrong3 = new
    if type_append == "sublst":
        c = copy.deepcopy(tmp)
        c.append(to_append)
        wrong1 = c
        wrong2 = 'TypeError: Can''t add a list to type list'
        wrong3 = 'TypeError: Can''t add type string to type list'
    qid = random.randint(500, 12000)
    return("INSERT INTO questions VALUES({}, 'Lists', 'Adding', '{}', '{}', '{}', '{}', '{}');".format(qid, question, str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))

def rand_string():
    s = ""
    num = random.randint(2, 4)
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in range(num):
        s += random.choice(alphabet)
    return s

def pointers():
    sublst = [rand_string() if random.randint(1, 2) == 1 else random.randint(2, 12) for i in range(3)]
    rand_len = random.choice([3, 4, 5])
    a = [rand_string() if random.randint(1, 2) == 1 else random.randint(2, 9) for i in range(rand_len)]
    a.append(sublst)
    copytype = random.choice(["slice", "equals"])
    if copytype == "slice":
        rand_ind = random.choice(list(range(rand_len)))
        to_sub = random.choice([rand_string(), random.randint(1, 80)])
        to_sub2 = random.choice([rand_string(), random.randint(1, 80)])
        rand_subind = random.randint(0, 2)
        inner = random.choice(["append", "change"])
        if inner == "append":
            if type(to_sub) is int and type(to_sub2) is int:
                question = r"a = {}\nb = a[:]\na[{}] = {}\na[-1].append({})\nprint(a)\nprint(b)".format(a, rand_ind, to_sub, to_sub2)
            if type(to_sub) is str and type(to_sub2) is int:
                question = r"a = {}\nb = a[:]\na[{}] = '{}'\na[-1].append({})\nprint(a)\nprint(b)".format(a, rand_ind, to_sub, to_sub2)
            if type(to_sub) is int and type(to_sub2) is str:
                question = r"a = {}\nb = a[:]\na[{}] = {}\na[-1].append('{}')\nprint(a)\nprint(b)".format(a, rand_ind, to_sub, to_sub2)
            if type(to_sub) is str and type(to_sub2) is str:
                question = r"a = {}\nb = a[:]\na[{}] = '{}'\na[-1].append('{}')\nprint(a)\nprint(b)".format(a, rand_ind, to_sub, to_sub2)
            correcta = copy.deepcopy(a)
            correctb = copy.deepcopy(a)
            wronga = copy.deepcopy(a)
            wrongb = copy.deepcopy(a)
            correcta[rand_ind] = to_sub
            correcta[-1].append(to_sub2)
            correctb[-1].append(to_sub2)
            wronga[rand_ind] = to_sub
            wrongb[rand_ind] = to_sub
            wrongb[-1].append(to_sub2)
            correct = str(correcta) + r"\n" + str(correctb)
            wrong1 = str(correcta) + r"\n" + str(wrongb)
            wrong2 = str(wronga) + r"\n" + str(correctb)
            wrong3 = str(wronga) + r"\n" + str(wrongb)
            qid = random.randint(700, 14000)
            return ("INSERT INTO questions VALUES({}, 'Lists', 'Pointers', '{}', '{}', '{}', '{}', '{}');".format(qid, question.replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'","''"),str(wrong2).replace("'","''"), str(wrong3).replace("'","''")))

        if inner == "change":
            if type(to_sub) is int and type(to_sub2) is int:
                question = r"a = {}\nb = a[:]\na[{}] = {}\na[-1][{}] = {}\nprint(a)\nprint(b)".format(a, rand_ind,
                                                                                                      to_sub,
                                                                                                      rand_subind,
                                                                                                      to_sub2)
            if type(to_sub) is str and type(to_sub2) is int:
                question = r"a = {}\nb = a[:]\na[{}] = '{}'\na[-1][{}] = {}\nprint(a)\nprint(b)".format(a, rand_ind,
                                                                                                      to_sub,
                                                                                                      rand_subind,
                                                                                                      to_sub2)
            if type(to_sub) is int and type(to_sub2) is str:
                question = r"a = {}\nb = a[:]\na[{}] = {}\na[-1][{}] = '{}'\nprint(a)\nprint(b)".format(a, rand_ind,
                                                                                                      to_sub,
                                                                                                      rand_subind,
                                                                                                      to_sub2)
            if type(to_sub) is str and type(to_sub2) is str:
                question = r"a = {}\nb = a[:]\na[{}] = '{}'\na[-1][{}] = '{}'\nprint(a)\nprint(b)".format(a, rand_ind,
                                                                                                      to_sub,
                                                                                                      rand_subind,
                                                                                                      to_sub2)
            correcta = copy.deepcopy(a)
            correctb = copy.deepcopy(a)
            wronga = copy.deepcopy(a)
            wrongb = copy.deepcopy(a)
            correcta[rand_ind] = to_sub
            correcta[-1][rand_subind] = to_sub2
            correctb[-1][rand_subind] = to_sub2
            wronga[rand_ind] = to_sub
            wrongb[rand_ind] = to_sub
            wrongb[-1].append(to_sub2)
            correct = str(correcta) + r"\n" + str(correctb)
            wrong1 = str(correcta) + r"\n" + str(wrongb)
            wrong2 = str(wronga) + r"\n" + str(correctb)
            wrong3 = str(wronga) + r"\n" + str(wrongb)
            qid = random.randint(700, 14000)
            return ("INSERT INTO questions VALUES({}, 'Lists', 'Pointers', '{}', '{}', '{}', '{}', '{}');".format(qid, question.replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace( "'","''"), str(wrong2).replace("'", "''"), str(wrong3).replace( "'", "''")))
    if copytype == "equals":
        rand_ind = random.choice(list(range(rand_len)))
        to_sub = random.choice([rand_string(), random.randint(1, 80)])
        to_sub2 = random.choice([rand_string(), random.randint(1, 80)])
        rand_subind = random.randint(0, 2)
        inner = random.choice(["append", "reassign"])
        b_add = random.randint(1, 45)
        if inner == "reassign":
            if type(to_sub) is int and type(to_sub2) is int:
                question = r"a = {}\nb = a\na = a + [{}]\na[-2].append({})\nb.append({})\nprint(a)\nprint(b)".format(a, to_sub, to_sub2, b_add)
            if type(to_sub) is str and type(to_sub2) is int:
                question = r"a = {}\nb = a\na = a + ['{}']\na[-2].append({})\nb.append({})\nprint(a)\nprint(b)".format(a, to_sub, to_sub2, b_add)
            if type(to_sub) is int and type(to_sub2) is str:
                question = r"a = {}\nb = a\na = a + [{}]\na[-2].append('{}')\nb.append({})\nprint(a)\nprint(b)".format(a, to_sub, to_sub2, b_add)
            if type(to_sub) is str and type(to_sub2) is str:
                question = r"a = {}\nb = a\na = a + ['{}']\na[-2].append('{}')\nb.append({})\nprint(a)\nprint(b)".format(a, to_sub, to_sub2, b_add)
            correcta = copy.deepcopy(a)
            correctb = copy.deepcopy(a)
            wronga = copy.deepcopy(a)
            wrongb = copy.deepcopy(a)
            correcta = correcta + [to_sub]
            correcta[-2].append(to_sub2)
            correctb[-1].append(to_sub2)
            correctb.append(b_add)
            wronga = wronga + [b_add]
            wrongb = wrongb + [to_sub]
            wrongb[-2].append(to_sub2)
            correct = str(correcta) + r"\n" + str(correctb)
            wrong1 = str(correcta) + r"\n" + str(wrongb)
            wrong2 = str(wronga) + r"\n" + str(correctb)
            wrong3 = str(wronga) + r"\n" + str(wrongb)
            qid = random.randint(700, 14000)
        if inner == "append":
            if type(to_sub) is int and type(to_sub2) is int:
                question = r"a = {}\nb = a\na[{}] = {}\na[-1].append({})\nprint(a)\nprint(b)".format(a, rand_ind, to_sub, to_sub2)
            if type(to_sub) is str and type(to_sub2) is int:
                question = r"a = {}\nb = a\na[{}] = '{}'\na[-1].append({})\nprint(a)\nprint(b)".format(a, rand_ind, to_sub, to_sub2)
            if type(to_sub) is int and type(to_sub2) is str:
                question = r"a = {}\nb = a\na[{}] = {}\na[-1].append('{}')\nprint(a)\nprint(b)".format(a, rand_ind, to_sub, to_sub2)
            if type(to_sub) is str and type(to_sub2) is str:
                question = r"a = {}\nb = a\na[{}] = '{}'\na[-1].append('{}')\nprint(a)\nprint(b)".format(a, rand_ind, to_sub, to_sub2)
            correcta = copy.deepcopy(a)
            original = copy.deepcopy(a)
            wrongb1 = copy.deepcopy(a)
            wrongb2 = copy.deepcopy(a)
            correcta[rand_ind] = to_sub
            correcta[-1].append(to_sub2)
            correctb = correcta
            wrongb1[rand_ind] = to_sub
            wrongb2[-1].append(to_sub2)
            correct = str(correcta) + r"\n" + str(correctb)
            wrong1 = str(correcta) + r"\n" + str(wrongb1)
            wrong2 = str(correcta) + r"\n" + str(wrongb2)
            wrong3 = str(correcta) + r"\n" + str(original)
            qid = random.randint(700, 14000)

        return ("INSERT INTO questions VALUES({}, 'Lists', 'Pointers', '{}', '{}', '{}', '{}', '{}');".format(qid, question.replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace( "'","''"), str(wrong2).replace("'", "''"), str(wrong3).replace( "'", "''")))

def create():
    return

#Types of questions

## Appending/Concatenating Lists
#.append()
# [x] + [y]

## List comprehension- DONE
# What list is outputted by the following comprehension
# Is this the correct format for list comprehension

## Strings
    # join ( ' '.join('h     th'.split())
    # slicing + indexing
    # strip (\n is also removed)
    # find + index


## Memory and pointers
    # inner list
        # concatenation
    # reassignment
    # clone (a = b, a = b[:])
        # cloning with an inner list too! + mutations
## .index()



if __name__ == '__main__':
    for i in range(150):
        print(pointers())
    for i in range(70):
        print(list_add())
    print(list_append())

