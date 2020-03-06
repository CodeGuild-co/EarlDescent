import requests # used for getting definitions

#### Useful functions ####
def each(_list):
    return range(len(_list))

# Grabbing dictionary from text file and getting letters from user
with open('dictionary.txt','r') as file:
    dictionary = file.readlines()

searching_dict = [list(dictionary[i])[:-1] for i in each(dictionary)]

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


def get_definition(word):
    '''Grabs the definition of a word from google'''
    # searching for the word on google
    link = 'https://www.google.com/search?q=define+' + word
    f = requests.get(link)
    # reading the html
    html = f.text
    # html depends on word type so try each of them
    word_type = ['verb','noun','pronoun','adjective','adverb','exclamation']
    for i in each(word_type):
        before = '<table style="font-size:14px;width:100%"><tr><td>'
        before += '<div style="color:#666;padding:5px 0">' + word_type[i] + '</div><ol><li>'
        try:
            definition = html.split(before)[1].split('</li>')[0].capitalize()[:-1]
            break
        except:
            pass

    try:
        return definition,word
    except:
        try:
            for i in each(word_type):
                before = '<table style="font-size:14px;width:100%"><tr><td>'
                before += '<div style="color:#666;padding:5px 0">' + word_type[i] + '</div>'
                before += '<ol style="padding-left:20px"><li style="list-style-type:decimal">'
                try:
                    definition = html.split(before)[1].split('</li>')[0].capitalize()[:-1]
                    break
                except:
                    pass
            return definition,word
        except:
            pass
        if word[-2:] == 'er':
            try:
                return get_definition(word[:-2])
            except:
                return get_definition(word[:-3])
        elif word[-3:] == 'ers':
            try:
                if get_definition(word[:-3]) == None:
                    return get_definition(word[:-4])
                return get_definition(word[:-3])
            except:
                pass
        elif word[-5:] == 'iness':
            return get_definition(word[:-5] + 'y')
        elif word[-4:] == 'ness':
            return get_definition(word[:-4])
        else:
            pass

    
if __name__ == "__main__":
    letters = list(input('What letters would you like? ').lower())
    d = minimise_dictionary(letters)
    words = get_best_words(d)
    for i in words:
        print(i)
    definition,word = get_definition(words[0])
    if word != words[0]:
        print(word.capitalize() + ' (' + words[0] + ') - ' + definition)
    else:
        print(word.capitalize() + ' - ' + definition)
