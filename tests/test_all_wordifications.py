from all_wordifications import *

def test_no_words():
	numbers = ["1-111-111-1111", "0-000-000-0000", "0-101-011-0010"]

	for n in numbers:
		all_words = all_wordifications(n)
		assert len(all_words) == 1
		assert next(iter(all_words)) == n.replace('-','')

def test_existence_of_word():
    numbers = ["1-800-724-6837", "1-800-724-6837-90"]
    words = ["1800PAINTER","1800PAINTER90"]
    for n,w in zip(numbers,words):
    	all_words = all_wordifications(n)
    	assert len(set([w]).intersection(set(all_words))) == 1

def test_small_words():
	small_words = "./language/words_short.txt"
	test_nums = ["4", "43", "4355"]
	test_wordifieds = [set(["I","4"]), set(["HE","43", "I3"]),
		set(["4355","HELL","GELL", "I355", "HE55"])]
	for n, w in zip(test_nums, test_wordifieds):
		assert all_wordifications(n, fname = small_words) == w		