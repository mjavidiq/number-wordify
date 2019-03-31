# Construct two dictionaries: one mapping characters to their number
#   and one mapping numbers to possible characters
_ordered_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
_ordered_numbers = list("22233344455566677778889999")

_C_to_N = {k:v for (k,v) in zip(_ordered_alphabet, _ordered_numbers)}
_N_to_C = {k:[] for k in _ordered_numbers}
for (k,v) in zip(_ordered_numbers, _ordered_alphabet):
    _N_to_C[k] += v

# Map a string of characters to the numbers on the keypad
def C_to_N(s):
    for k in _C_to_N.keys():
        s = s.replace(k, _C_to_N[k])
    return s

# Given a dictionary file (text file with one word per line)
#   return the list of words as a list of strings
def import_dictionary(fname):
    wordlist = []
    with open(fname) as f:
        wordlist = f.readlines()
    words = [w.rstrip().upper() for w in wordlist]

    return words

# Characters used for reformatting strings to phone number format
_relevant_nums = list("0123456789")
_relevant_chars = _ordered_alphabet + _relevant_nums

# Given a list of wordified numbers, fix each string so that:
#   1. Each sub-word begins and ends with a single dash
#   2. The wordified number does not begin or end with a dash '-'
#   3. In places where dashes were before (as counted by number of digits
#       and letters) we place a dash if one does not exist (e.g. the 1-800 dash)
def fix_dashes(words, number):
    new_words = []
    for w in words:
        new_w = w.replace('--','-')
        if new_w[0] == '-':
            new_w = new_w[1::]
        if new_w[-1] == '-':
            new_w = new_w[0:-1]

        digit_count = 0
        for digit in number:
            if digit == '-':
                curr_idx = find_nth_character(new_w, digit_count-1)
                if new_w[curr_idx+1] == '-' or new_w[curr_idx+2] in _ordered_alphabet:
                    pass
                else:
                    new_w = new_w[:curr_idx+1] + '-' + new_w[curr_idx+1:]
            else:
                digit_count += 1

        new_words += [str(new_w)]

    return set(new_words)

# Returns the index of the nth non-dash character in a string s
#   where n starts from 0
def find_nth_character(s,n):
    idx = 0
    char_count = -1
    for char in s:
        if char != '-':
            char_count += 1
        if char_count == n:
            return idx
        else:
            idx += 1