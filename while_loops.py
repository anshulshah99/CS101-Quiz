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

(1 == 1) and (2 != 3 or 1/0 == 0)
#How to get out of a while loop

def while_true():
    stop = ["continue", "break", "break", "return", "return", "print", "print"]
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
            question = f"What will the value of i be when the code below is done executing?\ni = 0\nwhile True:\n\ti += {i_incr}\n\tif i == {check}:\n\t\tcontinue"
            correct_ans = "The code above creates an infinite loop"
            wrong1 = check//i_incr
            wrong2 = check
            if wrong2 == wrong1:
                wrong2 = check - 1
            wrong3 = "Error: Invalid stopping condition"
            print(question)
        if s == "break":
            position = random.choice(["before", "after"])
            i_incr = random.choice([1, 2, 3])
            if i_incr == 1:
                check = random.randint(1, 50) * -1
            if i_incr in (2, 3):
                check = i_incr * random.randint(10, 25) + 1
            if hit_cond == 0 and position == "before":
                question = f"What will the value of i be when the code below is done executing?\ni = 0\nwhile True:\n\tif i == {check}:\n\t\tbreak\n\ti += {i_incr}"
                correct_ans = "The code above creates an infinite loop"
                wrong1 = check // i_incr
                wrong2 = check + i_incr
                wrong3 = check
                if wrong3 == wrong1:
                    wrong3 = check - i_incr
            if hit_cond == 0 and position == "after":
                question = f"What will the value of i be when the code below is done executing?\ni = 0\nwhile True:\n\ti += {i_incr}\n\tif i == {check}:\n\t\tbreak"
                correct_ans = "The code above creates an infinite loop"
                wrong1 = check // i_incr
                wrong2 = check + i_incr
                wrong3 = check
                if wrong3 == wrong1:
                    wrong3 = check - i_incr

            if hit_cond:
                check = i_incr * random.randint(10, 25)
            if hit_cond == 1 and position == "before":
                question = f"What will the value of i be when the code below is done executing?\ni = 0\nwhile True:\n\tif i == {check}:\n\t\tbreak\n\ti += {i_incr}"
    return question

if __name__ == '__main__':
    print(while_true())