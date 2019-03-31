from number_to_words import *
from all_wordifications import *

# Tests that numbers which are not wordifiable map to themselves
def test_no_words():
    numbers = ["1-111-111-1111", "0-000-000-0000", "0-101-011-0010"]

    for n in numbers:
        assert number_to_words(n) == n

# Test that the wordified number we return is a valid wordification
#   (under assumption that all_wordification works) and that
#   the returned value is NOT the original number
def test_some_word():
    numbers = ["1-800-724-6837", "1-800-724-6837-90"]
    words = ["1-800-PAINTER","1-800-PAINTER-90"]

    for (n,w) in zip(numbers, words):
        all_words = all_wordifications(n)
        word_chosen = number_to_words(n)
        assert word_chosen != n
        assert word_chosen in all_words