#Solver

def sort(_list):
    _list.sort()
    return _list

def each(_list):
    return range(len(_list))

file = open('dictionary.txt','r')
dictionary = file.readlines()
file.close()

searching_dict = [sort(list(dictionary[i])[:-1]) for i in each(dictionary)]
letters = sort(list(input('What letters would you like? ').lower()))

def minimise_dictionary():
    to_pop = []
    
    for i in each(searching_dict):
        temp = [letters[i] for i in each(letters)]
        for j in searching_dict[i]:
            if j in temp:
                temp.remove(j)
            else:
                to_pop.append(i)
                break
            
    to_pop.reverse()
    for i in to_pop:
        dictionary.pop(i)
        searching_dict.pop(i)

    for i in each(dictionary):
        dictionary[i] = dictionary[i][:-1]

    return dictionary


def get_best_word():
    len_best = 0
    for i in each(dictionary):
        if len(dictionary[i]) > len_best:
            len_best = len(dictionary[i])
            best_i = i
    return dictionary[best_i]

minimise_dictionary()
print(get_best_word())
get_best_word
