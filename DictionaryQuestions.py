'''
Created on DATE

@author: Anshul Shah

Module description
'''
import random

def counter():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rand_list = [(random.choice(alphabet),[random.randint(1, 10) for i in range(random.randint(3, 5))]) for i in range(random.randint(3, 5))]
    d = {}
    for k, v in rand_list:
        d[k] = v
    question = fr"d = {d}\nprint(sorted(d.items()))"
    correct = sorted(d.items())
    wrong1 = sorted([[k] + v for k, v in d.items()])
    wrong2 = d
    wrong3 = sorted(d.items(), key = lambda x: x[1])
    while wrong1 == wrong3:
        random.shuffle(wrong3)
    qid = random.randint(10000, 20000)
    return ("INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(qid, question.replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))

def missing_line_reverse():
    colors = ["red", "blue", "orange", "green", "white"]
    colleges = ["Duke", "Louisville", "UNC", "Clemson", "Kentucky", "Michigan State", "Syracuse", "Texas Tech"]
    missing = random.choice([1, 2, 3])
#for k, v in d.items(): #for k in d.keys() # for k in d
    #for col in v: #for col in d[k]
        #if col not in new_d:
        #    new_d[col] = [k] #new_d[col] = []

        #else:
         #   new_d[col].append(k)

if __name__ == '__main__':
    for i in range(50):
        print(counter())


