import wordifier
from language.language_help import fix_dashes

# Given a phone number, finds all possible wordifications of that number
#   according to the specified dictionary and returns a list of
#   all possible wordifications.
def all_wordifications(number, fname = "./language/words_alpha.txt"):
    worder = wordifier.wordifier(number, fname)
    wordified = set(worder(number.replace('-','')))

    return list(fix_dashes(wordified, number))