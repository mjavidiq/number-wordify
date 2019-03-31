import language.language_help as lang

# Test taking characters to their corresponding number
def test_C_to_N():
    assert lang.C_to_N('C') == '2'
    assert lang.C_to_N('Z') == '9'
    assert lang.C_to_N('CZ') == '29'

# Test importing a small dictionary of words
def test_import_dictionary():
    words = ["HE", "HEY", "HELLOS", "HELL", "GELL",
        "HELLO", "HI", "HA", "I"]
    import_file = "./language/words_short.txt"
    wordlist = lang.import_dictionary(import_file)

    assert set(words) == set(wordlist)

# Test conversion of strings with incorrect dashes
#   to those which have correct dashes as given by 
#   the original phone number
def test_fix_dashes():
    numbers = ["1-800","1-800-1"]
    in_strings = ["-1-800","1800--1-"]
    for (n, s) in zip(numbers, in_strings):
        assert set([n]) == lang.fix_dashes([s], n)

# Test is the same as above but should do nothing
def test_fix_dashes_indentity():
    numbers = ["724-6837","724-6837-90","1-800-724-6837"]
    in_strings = ["PAINTER","PAINTER-90","1-800-724-6837"]
    for (n, s) in zip(numbers, in_strings):
        assert set([s]) == lang.fix_dashes([s], n)

# Test the finding of the nth non-dash character in a string
#   given some potentially differently-dashed string
def test_nth_finder():
    strings = ["18007246837","1-800-724-6837","1800-PAINTER"]
    no_dash_strings = [s.replace("-","") for s in strings]
    for (s, no_dash_s) in zip(strings, no_dash_strings):
        for j in range(len(no_dash_s)):
            print(lang.find_nth_character(s,j))
            assert no_dash_s[j] == s[lang.find_nth_character(s,j)]