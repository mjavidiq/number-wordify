from all_wordifications import *
from words_to_number import *
from number_to_words import *

# Test that wordifying a number with no wordifications
#   and then converting back to a number yields itself
def test_identity():
    numbers = ["1-111-111-1111", "0-000-000-0000", "0-101-011-0010"]

    for n in numbers:
        all_words = all_wordifications(n)
        one_word = number_to_words(n)

        assert words_to_number(one_word) == n
        for word in all_words:
            assert words_to_number(word) == n

# Test that wordifying a number with some wordifications
#   and then converting back to a number yields itself
def test_non_identity():
    numbers = ["1-800-724-6837"]

    for n in numbers:
        all_words = all_wordifications(n)
        one_word = number_to_words(n)

        assert words_to_number(one_word) == n
        for word in all_words:
            assert words_to_number(word) == n