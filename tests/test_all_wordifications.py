from all_wordifications import *

def test_no_words():
	numbers = ["1-111-111-1111", "0-000-000-0000", "0-101-011-0010"]

	for n in numbers:
		all_words = all_wordifications(n)
		assert len(all_words) == 1
		assert all_words[0] == n.replace('-','')

def test_existence_of_word():
    numbers = ["18007246837", "1800724683790"]
    words = ["1800PAINTER","1800PAINTER90"]
    for n,w in zip(numbers,words):
    	all_words = all_wordifications(n)
    	assert len(set([w]).intersection(set(all_words))) == 1

def test_small_words():
	small_words = "./language/words_short.txt"
	assert all_wordifications("4", fname = small_words) == set(['I','4'])
	assert corpus("43", fname = small_words) == set(['HE','43'])
	assert corpus("4355", fname = small_words) == set(['4355','HELL','GELL'])