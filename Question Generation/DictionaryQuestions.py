'''
Created on DATE

@author: Anshul Shah

Module description
'''
import random
import copy

def counter():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rand_list = [(random.choice(alphabet),[random.randint(1, 10) for i in range(random.randint(2, 4))]) for i in range(random.randint(2, 4))]
    d = {}
    qid = random.randint(10000, 30000)
    for k, v in rand_list:
        d[k] = v
    poss_keys = list(d.keys())
    poss_keys.append(random.choice(list(alphabet)))
    poss_keys.append(random.choice(list(alphabet)))
    key_add = random.choice(poss_keys)
    print_values = ['print([v for k, v in d.items()])', 'print([d[k] for k, v in d.items()])', 'print([each[1] for each in d.items()])']
    print_keys = ['print([v[0] for v in d.items()])', 'print([k for k, v in d.items()])']
    print_items = ['print(list(d.items()))', 'print([(k, v) for (k, v) in d.items()])']
    print_error = ['print([d[k] for k in d.items()])']
    if key_add not in d:
        rand_int = random.randint(1, 10)
        value_add = [random.choice(list(alphabet)), random.choice(list(alphabet))]

        if rand_int > 7:
            to_add = f"d['{key_add}'].append({value_add})"
            print_statement = random.choice(["values", "keys", 'items'])
            if print_statement == "items":
                to_print = random.choice(print_items)
                question = fr"d = {d}\n{to_add}\n{to_print}"
                correct = "KeyError"
                d1 = copy.deepcopy(d)
                d1[key_add] = value_add
                options = [list(d1.items()), list(d1.keys()), list(d.items()), list(d.keys())]
                random.shuffle(options)
                wrong1, wrong2, wrong3 = options[0:3]
                return (
                    "INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(
                        qid, str(question).replace("'", "''"), str(correct).replace("'", "''"),
                        str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))
            if print_statement == "keys":
                to_print = random.choice(print_keys)
                question = fr"d = {d}\n{to_add}\n{to_print}"
                correct = "KeyError"
                d1 = copy.deepcopy(d)
                d1[key_add] = value_add
                options = [list(d1.items()), list(d1.keys()), list(d.items()), list(d.keys())]
                random.shuffle(options)
                wrong1, wrong2, wrong3 = options[0:3]
                return (
                    "INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(
                        qid, str(question).replace("'", "''"), str(correct).replace("'", "''"),
                        str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))

            if print_statement == "values":
                to_print = random.choice(print_values)
                question = fr"d = {d}\n{to_add}\n{to_print}"
                correct = "KeyError"
                d1 = copy.deepcopy(d)
                d1[key_add] = value_add
                options = [list(d1.values()), list(d1.items()), list(d.values()), list(d.items())]
                random.shuffle(options)
                wrong1, wrong2, wrong3 = options[0:3]
                return (
                    "INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(
                        qid, str(question).replace("'", "''"), str(correct).replace("'", "''"),
                        str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))
        else:
            print_statement = random.choice(["values", "keys", "values", "keys", 'items', 'error'])
            to_add = f"d['{key_add}'] = {value_add}"
            if print_statement == "values":
                to_print = random.choice(print_values)
                question = fr"d = {d}\n{to_add}\n{to_print}"
                d1 = copy.deepcopy(d)
                d1[key_add] = value_add
                correct = list(d1.values())
                wrong1 = "KeyError"
                wrong2 = list(d.values())
                wrong3 = list(d.keys())
                return (
                    "INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(
                        qid, str(question).replace("'", "''"), str(correct).replace("'", "''"),
                        str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))
            if print_statement == "keys":
                to_print = random.choice(print_keys)
                question = fr"d = {d}\n{to_add}\n{to_print}"
                d1 = copy.deepcopy(d)
                d1[key_add] = value_add
                correct = list(d1.keys())
                wrong1 = "KeyError"
                wrong2 = list(d.values())
                wrong3 = d
                return (
                    "INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(
                        qid, str(question).replace("'", "''"), str(correct).replace("'", "''"),
                        str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))
            if print_statement == "items":
                to_print = random.choice(print_items)
                question = fr"d = {d}\n{to_add}\n{to_print}"
                d1 = copy.deepcopy(d)
                d1[key_add] = value_add
                correct = list(d1.items())
                wrong1 = "KeyError"
                wrong2 = list(d1.values())
                wrong3 = d
                return (
                    "INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(
                        qid, str(question).replace("'", "''"), str(correct).replace("'", "''"),
                        str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))
            else:
                to_print = random.choice(print_error)
                question = fr"d = {d}\n{to_add}\n{to_print}"
                d[key_add] = value_add
                d1 = copy.deepcopy(d)
                correct = "KeyError"
                wrong1 = list(d1.items())
                wrong2 = list(d1.keys())
                wrong3 = list(d1.values())
                return ("INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(qid, str(question).replace("'", "''"), str(correct).replace("'", "''"), str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))

    else:
        new = random.choice([True, False])
        value_add = [random.choice(list(alphabet)), random.choice(list(alphabet))]

        if new:
            print_statement = random.choice(["values", "keys", 'items', 'error'])
            if print_statement == "values":
                to_print = random.choice(print_values)
                to_add = f"d['{key_add}'] = {value_add}"
                question = fr"d = {d}\n{to_add}\n{to_print}"
                d[key_add] = value_add
                correct = list(d.values())
                wrong1 = list(d.items())
                wrong2 = d
                wrong3 = random.choice(["ValueError", list(d.keys())])
                return (
                    "INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(
                        qid, str(question).replace("'", "''"), str(correct).replace("'", "''"),
                        str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))

            if print_statement == "keys":
                to_print = random.choice(print_keys)
                to_add = f"d['{key_add}'] = {value_add}"
                question = fr"d = {d}\n{to_add}\n{to_print}"
                d[key_add] = value_add
                correct = list(d.keys())
                wrong1 = list(d.items())
                wrong2 = d
                wrong3 = random.choice(["ValueError", list(d.values())])
                return (
                    "INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(
                        qid, str(question).replace("'", "''"), str(correct).replace("'", "''"),
                        str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))

            if print_statement == "items":
                to_print = random.choice(print_items)
                to_add = f"d['{key_add}'] = {value_add}"
                question = fr"d = {d}\n{to_add}\n{to_print}"
                d[key_add] = value_add
                correct = list(d.items())
                wrong1 = list(d.keys())
                wrong2 = d
                wrong3 = random.choice(["ValueError", list(d.values())])
                return (
                    "INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(
                        qid, str(question).replace("'", "''"), str(correct).replace("'", "''"),
                        str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))

            if print_statement == "error":
                to_print = random.choice(print_error)
                to_add = f"d['{key_add}'] = {value_add}"
                question = fr"d = {d}\n{to_add}\n{to_print}"
                d[key_add] = value_add
                correct = "KeyError"
                wrong1 = list(d.items())
                wrong2 = d
                wrong3 = random.choice([list(d.keys()), list(d.values())])
                return (
                    "INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(
                        qid, str(question).replace("'", "''"), str(correct).replace("'", "''"),
                        str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))

#====================================================
        else:
            print_statement = random.choice(["values", "values", "keys", 'items', 'error'])
            if print_statement == "values":
                to_print = random.choice(print_values)
                to_add = f"d['{key_add}'].append({value_add})"
                question = fr"d = {d}\n{to_add}\n{to_print}"
                d1 = copy.deepcopy(d)
                d1[key_add].extend(value_add)
                d[key_add].append(value_add)
                correct = list(d.values())
                wrong1 = list(d1.values())
                wrong2 = random.choice([d, list(d.keys())])
                wrong3 = random.choice(["ValueError", "KeyError"])
                return (
                    "INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(
                        qid, str(question).replace("'", "''"), str(correct).replace("'", "''"),
                        str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))
            if print_statement == "keys":
                to_print = random.choice(print_keys)
                to_add = f"d['{key_add}'].append({value_add})"
                question = fr"d = {d}\n{to_add}\n{to_print}"
                d1 = copy.deepcopy(d)
                d1[key_add].extend(value_add)
                d[key_add].append(value_add)
                correct = list(d.keys())
                wrong1 = list(d1.values())
                wrong2 = random.choice([d, list(d.values())])
                wrong3 = random.choice(["ValueError", "KeyError"])
                return (
                    "INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(
                        qid, str(question).replace("'", "''"), str(correct).replace("'", "''"),
                        str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))
            if print_statement == "items":
                to_print = random.choice(print_items)
                to_add = f"d['{key_add}'].append({value_add})"
                question = fr"d = {d}\n{to_add}\n{to_print}"
                d1 = copy.deepcopy(d)
                d1[key_add].extend(value_add)
                d[key_add].append(value_add)
                correct = list(d.items())
                wrong1 = list(d1.items())
                wrong2 = random.choice([d, list(d.values())])
                wrong3 = random.choice(["ValueError", "KeyError"])
                return (
                    "INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(
                        qid, str(question).replace("'", "''"), str(correct).replace("'", "''"),
                        str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))
            if print_statement == "error":
                to_print = random.choice(print_error)
                to_add = f"d['{key_add}'].append({value_add})"
                question = fr"d = {d}\n{to_add}\n{to_print}"
                d1 = copy.deepcopy(d)
                d1[key_add].extend(value_add)
                d[key_add].append(value_add)
                correct = "KeyError"
                wrong1 = list(d1.items())
                wrong2 = random.choice([d, list(d.items())])
                wrong3 = random.choice([list(d.values()), list(d1.values())])
                return (
                    "INSERT INTO questions VALUES({}, 'Dictionaries', 'Items', '{}', '{}', '{}', '{}', '{}');".format(
                        qid, str(question).replace("'", "''"), str(correct).replace("'", "''"),
                        str(wrong1).replace("'", "''"), str(wrong2).replace("'", "''"), str(wrong3).replace("'", "''")))

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


