import wordifier
from language.language_help import fix_dashes

def all_wordifications(number, fname = "./language/words_alpha.txt"):
    worder = wordifier.wordifier(number, fname)
    wordified = set(worder(number.replace('-','')))

    return list(fix_dashes(wordified, number))