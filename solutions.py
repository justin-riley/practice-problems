

def is_isogram(string):
    '''
    function to determine where there are any repeated letters 
    present in a given string.
    '''
    return sum([string.lower().count(letter.lower()) 
                        for letter in string]) == len(string)


def strip_comments(string,markers):
    r = string.split('\n')
    for i in range(len(markers)):
        for j in range(len(r)):
            if markers[i] in r[j]:
                r[j] = r[j].split(markers[i])[0].strip()
    return '\n'.join(r)
