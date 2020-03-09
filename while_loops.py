'''
Created on DATE

@author: Anshul Shah

Module description
'''
import random

'''i = 0
while i < len(lst):
    if lst[i] == el:
        lst = lst[:i] + lst[i+1:]
    else:
        i += 1'''
#this is correct!^

#make it incorrect by removing the else statement and having i always increment

#error, true, or false

#How to get out of a while loop

def while_true():
    stop = ["return"]#, "print"]
    for s in stop:
        hit_cond = random.choice([0, 1, 1])
        if s == "continue":
            i_incr = random.choice([1, 2, 3])
            if i_incr == 1:
                check = random.randint(1, 50) * -1
            if i_incr in (2, 3):
                check = i_incr * random.randint(10, 25) + 1
            if hit_cond:
                check = i_incr * random.randint(10, 25)
            question = rf"What will the value of i be when the code below is done executing?\ni = 0\nwhile True:\n\ti += {i_incr}\n\tif i == {check}:\n\t\tcontinue"
            correct = "The code above creates an infinite loop"
            wrong1 = check//i_incr
            wrong2 = check
            if wrong2 == wrong1:
                wrong2 = check - 1
            wrong3 = "Error: Invalid stopping condition"
            print(question, correct, wrong1, wrong2, wrong3)
        if s == "break":
            #position = random.choice(["before", "after"])
            i_incr = random.choice([1, 2, 3])
            if i_incr == 1:
                check = random.randint(1, 50) * -1
            if i_incr in (2, 3):
                check = i_incr * random.randint(5, 15) + 1
            if hit_cond == 0:
                question = rf"What will the value of i be when the code below is done executing?\ni = 0\nwhile True:\n\ti += {i_incr}\n\tif i == {check}:\n\t\tbreak"
                correct = "The code above creates an infinite loop"
                wrong1 = check // i_incr
                wrong2 = check + i_incr
                wrong3 = check
                if wrong3 == wrong1:
                    wrong3 = check - i_incr
            if hit_cond == 1:
                check = i_incr * random.randint(5, 15)
            if hit_cond == 1:
                question = rf"What will the value of i be when the code below is done executing?\ni = 0\nwhile True:\n\tif i == {check}:\n\t\tbreak\n\ti += {i_incr}"
                correct = check
                wrong1 = check - i_incr
                if wrong1 == correct:
                    wrong1 -= 1
                wrong2 = "The code above creates an infinite loop"
                wrong3 = check + i_incr
            print(question, correct, wrong1, wrong2, wrong3)
        if s == "return":
            i_incr = random.choice([1, 2, 3])
            add_more = random.choice([0,1])
            if hit_cond == 0:
                if i_incr == 1:
                    check = random.randint(1, 50) * -1
                if i_incr in (2, 3):
                    check = i_incr * random.randint(5, 15) + 1
                question = rf"What will the value of i be when the code below is done executing?\ni = 0\nwhile True:\n\ti += {i_incr}\n\tif i == {check}:\n\t\treturn i"
                if add_more:
                    question = rf"What will the value of i be when the code below is done executing?\ni = 0\nwhile True:\n\ti += {i_incr}\n\tif i == {check}:\n\t\ti += {i_incr}\n\t\treturn i"
                correct = "The code above creates an infinite loop"
                wrong1 = check // i_incr
                wrong2 = check + i_incr
                wrong3 = check
                if wrong3 == wrong1:
                    wrong3 = check - i_incr
            if hit_cond == 1:
                check = i_incr * random.randint(5, 15)
                question = rf"What will the value of i be when the code below is done executing?\ni = 0\nwhile True:\n\tif i == {check}:\n\t\treturn i\n\ti += {i_incr}"
                correct = check
                wrong1 = check + i_incr
                wrong2 = "The code above creates an infinite loop"
                wrong3 = i_incr
                if add_more:
                    question = rf"What will the value of i be when the code below is done executing?\ni = 0\nwhile True:\n\tif i == {check}:\n\t\ti+= {i_incr}\n\t\treturn i\n\ti += {i_incr}"
                    correct = check + i_incr
                    wrong1 = check
                    wrong2 = "The code above creates an infinite loop"
                    wrong3 = i_incr
            qid = random.randint(1000, 15000)
            return ("INSERT INTO questions VALUES({}, 'While Loops', 'Return/Print', '{}', '{}', '{}', '{}', '{}');".format(qid, question.replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))

        if s == "print":
            #have options about what will be printed and whether the loop will end
            if hit_cond:
                i_incr = random.choice([1, 2, 3])
                check = i_incr * random.randint(5, 15)
                question = rf"What will the value of i be when the code below is done executing?\ni = 0\nwhile True:\n\tif i == {check}:\n\t\tprint(i)\n\ti += {i_incr}"
                correct = f"The code will print {check} and be stuck in an infinite loop"
                wrong1 = f"The code will print {check} and terminate"
                wrong2 = f"The code won't print anything and will be stuck in an infinite loop"
                wrong3 = f"The code won't print anything and terminate"
                qid = random.randint(1000, 15000)
                return ("INSERT INTO questions VALUES({}, 'While Loops', 'Return/Print', '{}', '{}', '{}', '{}', '{}');".format(qid, question.replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))
            else:
                i_incr = random.choice([2, 3])
                check = i_incr * random.randint(5, 15) + 1
                question = rf"What will the value of i be when the code below is done executing?\ni = 0\nwhile True:\n\tif i == {check}:\n\t\tprint(i)\n\ti += {i_incr}"
                wrong2 = f"The code will print {check} and be stuck in an infinite loop"
                wrong1 = f"The code will print {check} and terminate"
                correct = f"The code won't print anything and will be stuck in an infinite loop"
                wrong3 = f"The code won't print anything and terminate"
                qid = random.randint(1000, 15000)
                return ("INSERT INTO questions VALUES({}, 'While Loops', 'Return/Print', '{}', '{}', '{}', '{}', '{}');".format(qid, question.replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))


def hailstone():
    return


if __name__ == '__main__':
    for i in range(60):
        print(while_true())