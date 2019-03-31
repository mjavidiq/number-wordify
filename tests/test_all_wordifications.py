from all_wordifications import *

# Test that if no words are possible, then our wordification
#	is just an identity operation
def test_no_words():
	numbers = ["1-111-111-1111", "0-000-000-0000", "0-101-011-0010"]

	for n in numbers:
		all_words = all_wordifications(n)
		assert len(all_words) == 1
		assert next(iter(all_words)) == n

# Test that a some known solution is present in the result
#	to ensure that at least a base level of the wordification
#	is working
def test_existence_of_word():
    numbers = ["1-800-724-6837", "1-800-724-6837-90"]
    words = ["1-800-PAINTER","1-800-PAINTER-90"]
    for n,w in zip(numbers,words):
    	all_words = all_wordifications(n)
    	assert len(set([w]).intersection(set(all_words))) == 1

# Test exhaustively the wordification on a much smaller
#	corpus of words to draw from
def test_small_words():
	small_words = "./language/words_short.txt"
	test_nums = ["4", "43", "4355"]
	test_wordifieds = [set(["I","4"]), set(["HE","43", "I-3"]),
		set(["4355","HELL","GELL", "I-355", "HE-55"])]
	for n, w in zip(test_nums, test_wordifieds):
		assert set(all_wordifications(n, fname = small_words)) == w		

# Test that appending more numbers which cannot be wordified
#	to some wordifiable numbers does not affect the cardinality
#	of the set of wordified numbers
def test_invariant_numbers():
    number_pairs = [("1-100-724-6837", "724-6837")]
    for (n1,n2) in number_pairs:
    	words1 = set(all_wordifications(n1))
    	words2 = set(all_wordifications(n2))
    	assert len(words1) == len(words2)
    	for w in words2:
    		assert ("1-100" + w in words1) or ("1-100-" + w in words1)

# Test that words can be fond adjacent to one-another
#	in a wordified number. This is to catch a specific bug
#	that was found
def test_adjacent_words():
	numbers = ["1-100-724-6837","724-6837-1-100","724-6837-724-6837"]
	words = ["1-100-SAG-OVER","SAG-OVER-1-100", "SAG-OVER-SAG-OVER"]
	for (n,w) in zip(numbers, words):
		assert w in set(all_wordifications(n))

# Test that we can predict the number of wordifications by separating
#	two sub-numbers of known size and then taking the product of 
#	the number of their wordifications
def test_product_of_wordifications():
	sub_number_a = "724-6837"
	sub_number_b = "832"
	number = sub_number_a + "-1-" + sub_number_b

	sub_a = len(all_wordifications(sub_number_a))	
	sub_b = len(all_wordifications(sub_number_b))	
	N = len(all_wordifications(number))
	assert sub_a*sub_b  == N
