import requests # used for getting definitions

#### Useful functions ####
def sort(_list):
    _list.sort()
    return _list

def each(_list):
    return range(len(_list))

# Grabbing dictionary from text file and getting letters from user
with open('dictionary.txt','r') as file:
    dictionary = file.readlines()

searching_dict = [sort(list(dictionary[i])[:-1]) for i in each(dictionary)]

#### Program functions ####
def minimise_dictionary(letters):
    '''Removing words that cannot be made'''
    # words aren't removed instanty as that changes size of list
    minimised_dictionary = dictionary[:]
    to_pop = []
    
    for i in each(searching_dict):
        # creating a temporary list of letters to avoid counting repeats
        temp = [letters[i] for i in each(letters)]
        for j in searching_dict[i]:
            if j in temp:
                temp.remove(j)
            else:
                to_pop.append(i)
                break

    # removing in reverse order so indexes don't change
    to_pop.reverse()
    for i in to_pop:
        minimised_dictionary.pop(i)

    # removing the \n from reading the text file
    for i in each(minimised_dictionary):
        minimised_dictionary[i] = minimised_dictionary[i][:-1]

    return minimised_dictionary


def get_best_words(dictionary):
    '''Picking the best 5 words from the new narrowed down dictionary'''
    length = [0,0,0,0,0]
    index = []

    for i in each(dictionary):
        # checking against each of the top 5 in order
        for j in range(5):
            if len(dictionary[i]) > length[j]:
                length.insert(j,len(dictionary[i]))
                index.insert(j,i)
                break # so it's not inserted more than once

    # returns top 5 unless there aren't 5 possible words
    if len(dictionary) >=5:
        return [dictionary[index[i]] for i in range(5)]
    else:
        return [dictionary[index[i]] for i in each(dictionary)]


##def get_definition(word):
##    '''Grabs the definition of a word from dictionary.com'''
##    link = 'https://www.dictionary.com/browse/' + word
##    f = requests.get(link)
##    html = f.text
##    definition = html.split(' See more.">')[0].split(word.title() + ' definition, ')[1]

##    link = 'https://en.oxforddictionaries.com/definition/hokkie'
##    f = requests.get(link)
##    html = f.text
##    print(html)


##    return definition
    
if __name__ == "__main__":
    letters = sort(list(input('What letters would you like? ').lower()))
    d = minimise_dictionary(letters)
    words = get_best_words(d)
    for i in words:
        print(i)
    #print(words[0].title() + ' - ' + get_definition(words[0]))
