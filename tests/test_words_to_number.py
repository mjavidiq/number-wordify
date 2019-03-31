from words_to_number import words_to_number

# Test that the length of the resulting phone number
#   has the correct length
def test_length_correct():
    words = ["1-800-PAINTER","1-800-PAINTER-90"]
    patterns = ["1-111-111-1111","1-111-111-1111-11"]
    for w,p in zip(words, patterns):
        assert len(words_to_number(w,p)) == len(p)

# Test that dashes are placed correctly in the string
def test_dash_placement():
    words = ["1-800-PAINTER","1-800-PAINTER-90"]
    patterns = ["1-111-111-1111","1-111-111-1111-11"]
    for w,p in zip(words, patterns):
        number = words_to_number(w, pattern = p)
        for (cn,cp) in zip(number, p):
            if cp == '-':
                assert cn == cp

# Test that the wordified number to number conversion 
#   is correct. This test subsumes previous tests but
#   they are left for the sake of future debugging
def test_words_to_numbers():
    words = ["1-800-PAINTER","1-800-PAINTER-90"]
    patterns = ["1-111-111-1111","1-111-111-1111-11"]
    numbers = ["1-800-724-6837", "1-800-724-6837-90"]
    for (w,p,n) in zip(words, patterns, numbers):
        number = words_to_number(w, pattern = p)
        assert number == n
