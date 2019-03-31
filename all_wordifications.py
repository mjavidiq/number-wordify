import wordifier
from language.language_help import fix_dashes

# Given a phone number, finds all possible wordifications of that number
#   according to the specified dictionary and returns a list of
#   all possible wordifications.
def all_wordifications(number, fname = "./language/words_alpha.txt"):
    worder = wordifier.wordifier(number, fname)
    wordified = set(worder.wordify(number.replace('-','')))

    wordified_l = list(fix_dashes(wordified, number))
    wordified_l = sorted(wordified_l, key = lambda s: s.count('-'))

    return wordified_l
