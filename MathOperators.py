'''
Created on DATE

@author: Anshul Shah

Module description
'''

import psycopg2
import os
#from flask import Flask
#import datetime
import random

#app = Flask(__name__)
#date_time = datetime.datetime.today()

#app.secret_key = 's3cr3t'
#app.config.from_object('config')
#app.url_map.strict_slashes = False

#con = psycopg2.connect(dbname = "postgres", user = "postgres")
#https://pythonspot.com/flask-web-forms/

def floor():
    num = random.randint(5, 70)
    den = random.randint(2, num)
    correct = num // den
    inc1 = (num // den) - 1
    inc2 = (num // den) + 1
    inc3 = round((num / den), 2)
    return ("Math operators", "Floor Division", "What is outputted by " + str(num) + " // " + str(den), correct, inc1, inc2, inc3)

def mod():
    num = random.randint(5, 70)
    den = random.randint(2, num - 1)
    correct = num % den

    inc2 = (num % den) + 1
    inc3 = round((num / den), 2)
    inc1 = den/num * 100
    while inc1 in set([correct, inc2, inc3]):
        inc1 = random.randint(1, 10)
    if len([correct, inc1, inc2, inc3]) != len(set([correct, inc1, inc2, inc3])):
        return None
    return ("Math operators", "Mod", "What is outputted by " + str(num) + " % " + str(den), correct, inc1, inc2, inc3)


def exponent():
    num = random.randint(1, 5)
    exp = random.randint(-2, 3)
    if num == 2 and exp == 2:
        while exp == 2:
            exp = random.randint(-2, 3)
    correct = num ** exp
    inc1 = num * exp
    if inc1 == correct:
        inc1 += 2
    inc2 = num ** (exp + 1)
    inc3 = exp ** num
    if inc3 == correct:
        inc3 -= 2
    if len([correct, inc1, inc2, inc3]) != len(set([correct, inc1, inc2, inc3])):
        return None
    return ("Math operators", "Exponents", "What is outputted by " + str(num) + " ** " + str(exp), correct, inc1, inc2, inc3)

def concat():
    f = open("lowerwords.txt")
    lowerwords = f.read().split()
    wordlst = [word for word in lowerwords if len(word) > 6 and len(word) < 10]
    word = random.choice(wordlst)
    qtype = random.randint(1,8)
    if qtype > 2:
        substr_len = random.randint(2, 4)
        start = random.randint(0, len(word) - substr_len - 1)
        end = start + substr_len
        repeat = random.randint(1, 4)
        correct = word[start:end] * repeat
        inc1 = word[start:end + 1] * repeat
        inc2 = word[start + 1:end] * repeat
        inc3 = "TypeError"
        text = r"word = ''{}''\nWhat is the correct output for word[{}:{}] * {}?".format(word, start, end, repeat)
    else:
        start = random.randint(0, len(word) - 3)
        end = start + random.randint(1, 4)
        next_start = random.randint(1, len(word) - 3)
        next_end = next_start + random.randint(1, 4)
        text = r"word = ''{}''\nWhat is the correct output for word[{}:{}] * word[{}:{}]".format(word, start, end, next_start, next_end)
        correct = "TypeError"
        inc1 = word[start:end] + word[next_start:next_end]
        inc2 = word[start:end]
        inc3 = word[next_start:next_end]
    return("Strings", "Concatenation", text, correct, inc1, inc2, inc3)

def mult():
    num = random.randint(10,60)
    letters = str(num)
    repeat = random.randint(3, 6)
    text = 'What is the correct output for "{}" * {}?'.format(letters, repeat)
    correct = letters * repeat
    inc1 = num * repeat
    inc2 = "TypeError"
    inc3 = letters + str(repeat)
    return("Strings", "Concatenation", text, correct, inc1, inc2, inc3)



def create():
    questions = []
    for i in range(60):
        f = floor()
        m = mod()
        while m is None:
            m = mod()
        e = exponent()
        while e is None:
            e = exponent()
        c = concat()
        #questions.append(f)
        #questions.append(m)
        #questions.append(e)
        questions.append(c)
    for i in range(30):
        m = mult()
        questions.append(m)
    return questions

def insert():
    quests = create()
    for q in quests:
        i = random.randint(300, 100000)

        print("INSERT INTO questions VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}' );".format(i, q[0], q[1], q[2], q[3], q[4], q[5], q[6]))
    


if __name__ == '__main__':
    #if os.environ.get('GAE_ENV') == 'standard':
        # If deployed, use the local socket interface for accessing Cloud SQL
    #con = psycopg2.connect(os.environ['PSYCOPG2_POSTGRESQL_URI'])
    #else:
    #con = psycopg2.connect(dbname='postgres')

    #con.autocommit = True
    #cur = con.cursor()

    #cur.execute("""SELECT distinct(concept) from questions;""")
    #print(cur.fetchall())

    insert()
