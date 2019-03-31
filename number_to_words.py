import wordifier
import language.language_help as lang

# Given a phone number, finds all possible wordifications of it
#   according to the specified dictionary and returns a possible
#   wordification.
def number_to_words(number, fname = "./language/words_alpha.txt"):
    corpus = lang.import_dictionary(fname)

    # Keep only words which could appear SOMEWHERE in the string
    words = list(
        filter(lambda w: lang.C_to_N(w) in number, corpus) 
        )
    # Sorting words is important so we know how all shorter numbers
    #   get wordified as we build up a set of wordifications
    words = sorted(words, key = lambda w: len(w))

    wordified = number
    for w in words:
        w_num = lang.C_to_N(w)
        wordified = number.replace(w_num, w)

    return wordified