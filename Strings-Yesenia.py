'''
Created on DATE

@author: Yesenia Velasco

Module description: Generate String questions regarding join, split, strip, find, slicing, and indexing
'''
import random
import copy
import nltk #used to get words in English dictionary



def string_join(word_list):
    """
      Returns a question template based on the join() function in strings
    """
    #problem types
    type_join = random.choice(["int", "str", "str", "str", "str", "lst", "sublst"])
    join_by = random.choice([",", " ", ":", "."])
    
    #If joining an integer
    if type_join == "int":
        to_join = random.randint(10, 99)
        question = r"tmp = {}\nfinal = '{}'.join(tmp)\nWhat is the value of final after the above code runs?".format(
            to_join, join_by)
        correct = "TypeError: can only join an iterable"
        wrong1 = str(to_join)
        wrong2 = [to_join]
        wrong3 = wrong1[0] + join_by + wrong1[1]
        
    #If joining a string
    elif type_join == "str":
        to_join = " ".join([random.choice(word_list) for i in range(random.choice([2, 3, 4, 5]))])
        question = r"tmp = '{}'\nfinal = '{}'.join(tmp)\nWhat is the value of final after the above code runs?".format(
            to_join, join_by)
        correct = join_by.join(to_join)
        wrong1 = to_join.split(" ")
        wrong2 = join_by.join(wrong1)
        wrong3 = "TypeError: can only join an iterable"
           
    else:
        to_join = [random.choice(word_list) for i in range(random.choice([2, 3, 4]))]

        question = r"tmp = {}\nfinal = '{}'.join(tmp)\nWhat is the value of final after the above code runs?".format(to_join, join_by)
        correct = join_by.join(to_join)
        wrong1 = to_join
        
        wrong2 = "".join(to_join)
        wrong2 = join_by.join(wrong2)
        
        wrong3 = "TypeError: expected str instance, list found"
        
        #If joining a list of lists
        if type_join == "sublst":
            rand_lst = [random.choice(word_list), random.choice(word_list)]

            correct = "TypeError: sequence item " + str(len(to_join)-1) + ": expected str instance, list found"
            wrong1 = join_by.join(to_join) + join_by.join(rand_lst)
            wrong2 = join_by.join(to_join)
            wrong3 = " ".join(to_join) + str(to_join[-1])
            to_join.append(rand_lst)
            question = r"tmp = {}\nfinal = '{}'.join(tmp)\nWhat is the value of final after the above code runs?".format(to_join, join_by)

    #Create the question

    
    #Put it all together
    qid = random.randint(500, 12000)
    return("INSERT INTO questions VALUES({}, 'Strings', 'Join', '{}', '{}', '{}', '{}', '{}');".format(qid, str(question).replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))


def string_split(word_list):
    """
      Returns a question template based on the split() function in strings
    """
    #problem types
    type_split = random.choice(["int", "str", "str", "str","lst"])
    split_by = random.choice([",", " ", ":", "."])

    #If splitting an integer
    if type_split == "int":
        to_split = random.randint(10, 99)
        question = r"tmp = {}\nfinal = tmp.split('{}')\nWhat is the value of final after the above code runs?".format(to_split, split_by)
        correct = "SyntaxError: invalid syntax"
        wrong1 = str(to_split)
        wrong2 = [wrong1[0], wrong1[1]]
        wrong3 = wrong1[0] + split_by + wrong1[1]

    #If splitting a string
    elif type_split == "str":
        to_split = split_by.join([random.choice(word_list) for i in range(random.choice([2, 3, 4, 5]))])
        question = r"tmp = '{}'\nfinal = tmp.split('{}')\nWhat is the value of final after the above code runs?".format(to_split, split_by)
        if split_by != "":
            correct = to_split.split(split_by)
            wrong1 = "".join([char for char in to_split if char != split_by])
            
            if split_by != " ":
                wrong2 = to_split.split(" ")
            else:
                wrong2 = " ".join(correct)
            
            wrong3 = "AttributeError: 'str' object has no attribute 'split'"
        else:
            correct = "ValueError: empty separator"
            wrong1 = "".join([char for char in to_split if char != split_by])
            wrong2 = to_split.split(" ")
            wrong3 = to_split
           
    else:
        #If splitting a list
        to_split = [random.choice(word_list) for i in range(random.choice([2, 3, 4]))]
        question = r"tmp = {}\nfinal = tmp.split('{}')\nWhat is the value of final after the above code runs?".format(to_split, split_by)
        correct = "AttributeError: 'list' object has no attribute 'split'"
        wrong1 = " ".join(to_split)
        wrong2 = split_by.join(to_split)
        if wrong2 == wrong1:
            wrong2 = "".join(to_split)
        wrong3 = to_split
        
    
    #Create the question

    if type_split == "int":
        question = r"tmp = {}\nfinal = tmp.split('{}')\nWhat is the value of final after the above code runs?".format(to_split, split_by)

    #
    qid = random.randint(500, 12000)
    return("INSERT INTO questions VALUES({}, 'Strings', 'Split', '{}', '{}', '{}', '{}', '{}');".format(qid, str(question).replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))



def string_slice(word_list):
    """
      Returns a question template based on string slicing
    """
    #problem types
    problem_type = random.choice(["indexing", "first slice", "middle slice", "last slice"])
    s = " ".join([random.choice(word_list) for i in range(random.choice([1, 2]))])
    
    #Indexing Problem Type
    if problem_type == "indexing":
        index = random.randint(-len(s)-1, len(s)+1)
        
        #If index is out of bounds
        if index < -len(s) or index >= len(s):
            correct = "IndexError: string index out of range"
            wrong1 = s[-1]
            wrong2 = s[0]
            wrong3 = "None"
        elif index != 0 or index != -len(s) and index < len(s) - 2:
            correct = s[index]
            wrong1 = s[index + 1]
            wrong2 = "IndexError: string index out of range"
            wrong3 = "None"
        else:
            correct = s[index]
            wrong1 = s[1]

            wrong2 = "IndexError: string index out of range"
            wrong3 = "None"
            
        #Create the Indexing question
        question = r"s = '{}'\nfinal = s[{}]\nWhat is the value of final after the above code runs?".format(s, index)
    else:   
        
        #First Slice Problem Type
        if problem_type == "first slice":
            slice_end = random.randint(-len(s) + 1, len(s)+3)
            correct = s[:slice_end]
            #Create the Slice question
            question = r"s = '{}'\nfinal = s[:{}]\nWhat is the value of final after the above code runs?".format(s, slice_end)
        
        #Middle Slice Problem Type
        if problem_type == "middle slice":

            slice_start = random.randint(-len(s), len(s)+1)
            while slice_start == -2 or slice_start == -1 or slice_start != 0 or slice_start > len(s)-2:
                slice_start = random.randint(-len(s), len(s) + 1)
            if slice_start < 0:
                slice_end = random.randint(slice_start, -1)
            else:
                slice_end = random.randint(slice_start, len(s) - 1)
            correct = s[slice_start:slice_end]
            #Create the Slice question
            question = r"s = '{}'\nfinal = s[{}:{}]\nWhat is the value of final after the above code runs?".format(s, slice_start, slice_end)
        
        #Last Slice Problem Type
        if problem_type == "last slice":
            slice_start = random.randint(-len(s)-1, len(s)-1)
            correct = s[slice_start:]
            #Create the Slice question
            question = r"s = '{}'\nfinal = s[{}:]\nWhat is the value of final after the above code runs?".format(s, slice_start)
        
            
        wrong1 = "IndexError: string index out of range"
            
        if correct != s[0]:
            wrong2 = s[0]
        else:
            wrong2 = s[-1]
        
        if correct != "":
            wrong3 = "None"
        else:
            wrong3 = s
        
    
    #Put it all together
    qid = random.randint(500, 12000)
    return("INSERT INTO questions VALUES({}, 'Strings', 'Index/Slice', '{}', '{}', '{}', '{}', '{}');".format(qid, str(question).replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), wrong3.replace("'", "''")))


def string_strip(word_list):
    """
      Returns a question template based on the strip() function in strings
    """
    tmp = [random.choice(word_list) for i in range(random.choice([1, 2, 2, 3, 3]))]
    
    #50% chance of string containing a newline character
    num = random.randint(0, 10)
    if num > 5:
        index = random.randint(0, len(tmp)-1)
        tmp[index] = tmp[index] + r"\n"
    
    #50% chance of string containing space characters at the beginning of the string  
    num = random.randint(0, 10)
    if num > 3:
        tmp[0] = "  " + tmp[0]
        
    #50% chance of string containing space characters at the end of the string  
    num = random.randint(0, 10)
    if num > 3:
        tmp[-1] = tmp[-1] + "  "
    
    s = "  ".join(tmp)
    
    correct = s.strip()
    wrong1 = "".join([word.strip() for word in tmp])
    if wrong1 == correct:
        wrong1 = "Error: Found no whitespace to strip"
    
    wrong2 = s.lstrip()
    if wrong2 == correct:
        wrong2 = "  " + wrong2
        
    wrong3 = s.rstrip()
    if wrong3 == correct:
        wrong3 = wrong3 + r"\n"
    if wrong3 == wrong2:
        wrong3 = wrong3 + r"\n"
      
    #Create the question  
    question = r"s = '{}'\nfinal = s.strip()\nWhat is the value of final after the above code runs?".format(s)
    
    #Put it all together
    qid = random.randint(500, 12000)
    return("INSERT INTO questions VALUES({}, 'Strings', 'Strip', '{}', '{}', '{}', '{}', '{}');".format(qid, str(question).replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))


def string_find(word_list):
    """
      Returns a question template based on the find() function in strings
    """
    s = " ".join([random.choice(word_list) for i in range(random.choice([1, 2, 3]))])
    char = s[random.randint(0, len(s)-1)]
    
    #40% chance of char not being in the string
    num = random.randint(0, 10)
    if num > 6:
        c = -1
        while c == -1:
            char = random.choice("abcdefghijklmnopqrstuvwxyz,:-+=!*&@#$%_")
            if char in s:
                c = 1
    correct = s.find(char)
    
    wrong1 = s.rfind(char)
    while wrong1 == correct:
        wrong1 += 1
    
    wrong2 = s.count(char)
    while wrong2 == correct or wrong2 == wrong1:
        wrong2 += 1
        
    wrong3 = -1
    while wrong3 == correct or wrong3 == wrong1 or wrong3 == wrong2: #ran out of ideas xP
        wrong3 += 1
      
    #Create the question  
    question = r"s = '{}'\nfinal = s.find('{}')\nWhat is the value of final after the above code runs?".format(s, char)
    
    #Put it all together
    qid = random.randint(500, 12000)
    #print(question)
    return("INSERT INTO questions VALUES({}, 'Strings', 'Find', '{}', '{}', '{}', '{}', '{}');".format(qid, str(question).replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))

def get_words():
    f = open("lowerwords.txt")
    lowerwords = f.read().split()
    return([word for word in lowerwords])


if __name__ == '__main__':

    #import all the words in English dictionary
    #nltk.download()
    #from nltk.corpus import words
    word_list = get_words()
    #keep only words of length 5
    word_list = [word for word in word_list if len(word) == 5]

    for i in range(80):
        print(string_join(word_list))
        #print(string_split(word_list))
        #print(string_slice(word_list))
        #print(string_find(word_list))

        #select q.concept, q.function, count(*) as num from responses r, questions q where q.qid = r.qid and r.semester = 'Spring 20' group by q.concept, q.function order by num desc;
 

