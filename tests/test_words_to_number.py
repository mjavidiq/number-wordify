from words_to_number import words_to_number

def test_length_correct():
    words = ["1-800-PAINTER","1-800-PAINTER-90"]
    patterns = ["1-111-111-1111","1-111-111-1111-11"]
    for w,p in zip(words, patterns):
        assert len(words_to_number(w,p)) == len(p)


def test_dash_placement():
    words = ["1-800-PAINTER","1-800-PAINTER-90"]
    patterns = ["1-111-111-1111","1-111-111-1111-11"]
    for w,p in zip(words, patterns):
        number = words_to_number(w, pattern = p)
        for (cn,cp) in zip(number, p):
            if cp == '-':
                assert cn == cp

def test_words_to_numbers():
    words = ["1-800-PAINTER","1-800-PAINTER-90"]
    patterns = ["1-111-111-1111","1-111-111-1111-11"]
    numbers = ["1-800-724-6837", "1-800-724-6837-90"]
    for (w,p,n) in zip(words, patterns, numbers):
        number = words_to_number(w, pattern = p)
        assert number == n
