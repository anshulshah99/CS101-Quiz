'''
Created on Oct 5, 2019

@author: anshul
'''
import random

def get_words():
    f = open("lowerwords.txt")
    lowerwords = f.read().split()
    return([word for word in lowerwords if len(word) > 6])
    
def create(text_list):
    all_concepts = ["find", "count", "starts", "ends", "upper", "lower"]
    concept = random.choice(all_concepts)
    word = random.choice(text_list)
    letters = set()
    alphabet = set([c for c in "abcdefghijklmnopqrstuvwxyz"])
    for let in word:
        letters.add(let)
    remaining = alphabet.difference(letters)
    for i in range(2):
        letters.add(random.choice(list(remaining)))
    if concept == "find":
        character= random.choice(list(letters))
        question = "%s.find('%s')" %(word, character)
        answer = word.find(character)
        return (question, answer)
    if concept == "count":
        character= random.choice(list(letters))
        question = "%s.count('%s')" %(word, character)
        answer = word.count(character)
        return (question, answer)
    if concept == "starts":
        correct = word[:3]
        wrong_1 = word[1:3]
        wrong_2 = word[-3:]
        substr = random.choice([correct, wrong_1, wrong_2])
        question = "%s.startswith('%s')" %(word, substr)
        answer = word.startswith(substr)
        return (question, answer)
    if concept == "ends":
        wrong_1 = word[:3]
        wrong_2 = word[1:3]
        correct = word[-3:]
        substr = random.choice([correct, wrong_1, wrong_2])
        question = "%s.endswith('%s')" %(word, substr)
        answer = word.endswith(substr)
        return (question, answer)
    if concept == "upper":
        word = change_case(word)
        question = "%s.upper()" %(word)
        answer = word.upper()
        return (question, answer)
    if concept == "lower":
        word = change_case(word)
        question = "%s.lower()" %(word)
        answer = word.lower()
        return (question, answer)
    return

def change_case(word):
    ret = ""
    for ch in word:
        val = random.randint(0, 2)
        if val == 0:
            ret += ch.upper()
        if val == 1:
            ret += ch
    ret += "123"
    return ret
    
    
if __name__ == '__main__':
    x = get_words()
    q, a = create(x)
   # print(q)
    #print(a)
    