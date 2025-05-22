


def search_for_letters(phrase:str, letters:str):
    '''Return a set of the 'letters' found in 'phrase'.'''
    return set(letters).intersection(set(phrase))
