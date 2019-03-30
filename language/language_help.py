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

# Holds information about the possible words given a set of
# 	numbers
class corpus:

	def __init__(self, fname):
		wordlist = []
		with open(fname) as f:
			wordlist = f.readlines()
		self.words = [w.strip().upper() for w in wordlist]

		# Remove trivial words of individual letters, except for 'A' and 'I' 
		#	as well as words longer than 10 characters (our maximum length)
		self.words = list(filter(lambda w: (len(w) > 1) and (len(w) < 11), 
			self.words) )
		self.words += ['A', 'I']
		
		word_nums = set([C_to_N(w) for w in self.words])
		self.N_to_C_dict = dict.fromkeys(word_nums)

		for k in self.N_to_C_dict.keys():
			self.N_to_C_dict[k] = set([k])

		for w in self.words:
			key = C_to_N(w)
			self.N_to_C_dict[key].add(w)

	def __call__(self, number):
		if len(number) == 0: 
			return set([])
		
		if not(number in self.N_to_C_dict.keys()):
			self.N_to_C_dict[number] = set([number])

		return self.N_to_C_dict[number]