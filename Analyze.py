'''
Created on DATE

@author: Anshul Shah

Module description
'''
def get_data():
    f = open("rolling_algorithm.txt")
    all_data = []
    for l in f:
        vals = [x.strip() for x in l.split('|')]
        all_data.append(vals)
    return all_data

def rolling_avg(alpha, data):
    for i in range(1, len(data)):
        percent_before = sum([int(x[3]) for x in data[:i]])/sum([int(x[4]) for x in data[:i]])
        mastery = percent_before * (1 - alpha) + (alpha) * int(data[i][3])/int(data[i][4])
        print(mastery)

def distribution():

if __name__ == '__main__':
    d = get_data()
    rolling_avg(0.3, d)

