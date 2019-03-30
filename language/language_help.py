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

	def __init__(self, fname, number):
		self.phone_number = number.replace('-','')

		wordlist = []
		with open(fname) as f:
			wordlist = f.readlines()
		self.words = [w.strip().upper() for w in wordlist]

		# Keep only words which could appear SOMEWHERE in the string
		#	as well as A and I (exclude other letters as "words", e.g. 'F')
		self.words = list(filter(lambda w: len(w) > 1, self.words))
		self.words += ['A', 'I']
		self.words = list(
			filter(lambda w: C_to_N(w) in self.phone_number, self.words) 
			)
		self.words = sorted(self.words, key = lambda w: len(w))

		# Pre-allocate the dictionary for speed
		length = len(number)	
		dict_nums = set([
			self.phone_number[i:j+1] for i in xrange(length) for j in xrange(i,length)
			])
		self.N_to_C_dict = dict.fromkeys(dict_nums)

		for k in self.N_to_C_dict.keys():
			self.N_to_C_dict[k] = set([])

		for w in self.words:
			key = C_to_N(w)
			self.add_number_word(key, w)
			

	def __call__(self, number):
		if len(number) == 0: 
			return set([])
		
		if self.N_to_C_dict[number] == set([]):
			return self.add_number_word(number, number)

		return self.N_to_C_dict[number]

	def add_number_word(self, number, word):
		if len(number) == 0:
			return set([])
		self.N_to_C_dict[number].add(word)
		self.N_to_C_dict[number].add(number)
		if len(number) > 1:
			for j in range(len(number)):
				pivot_char = number[j]
				lower = self(number[:j])
				upper = self(number[j+1:])
				if len(lower) == 0:
					for suffix in upper:
						self.N_to_C_dict[number].add(pivot_char + suffix)
				elif len(upper) == 0:
					for prefix in lower:
						self.N_to_C_dict[number].add(prefix + pivot_char)
				else:
					for prefix in lower:
						for suffix in upper:
							self.N_to_C_dict[number].add(
								prefix + pivot_char + suffix
								)
		return self.N_to_C_dict[number]
