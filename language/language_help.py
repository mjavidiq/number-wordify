import itertools as it

# Construct two dictionaries: one mapping characters to their number
#	and one mapping numbers to possible characters
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

def import_dictionary(fname):
	wordlist = []
	with open(fname) as f:
		wordlist = f.readlines()
	words = [w.rstrip().upper() for w in wordlist]

	return words