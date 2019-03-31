import wordifier
from language.language_help import fix_dashes

# Given a phone number, finds all possible wordifications of it
#   according to the specified dictionary and returns a possible
#   wordification.
def number_to_words(number, fname = "./language/words_alpha.txt"):
    worder = wordifier.wordifier(number, fname)
    wordified = set(worder(number.replace('-','')))

    words = list(fix_dashes(wordified, number))
    
    retval = words[0]
    if retval == number and len(words) > 1:
        retval = words[1]

    return retval