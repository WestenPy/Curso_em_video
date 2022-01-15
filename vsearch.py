def search4letters(phrase, letters='aeiou'):
    """
    ->return a set of the 'letters' found in 'phrase'.
    :param phrase: phrase where the search will be made
    :param letters:set of letters that will be searched for in the sentence
    :return returns a set ()
    """
    return set(letters).intersection(set(phrase))


print(search4letters('return a set of the letters', 'aebcdgfou'))
