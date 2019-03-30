import language.language_help as lang

def test_C_to_N():
	assert lang.C_to_N('C') == '2'
	assert lang.C_to_N('Z') == '9'
	assert lang.C_to_N('CZ') == '29'

def test_import_dictionary():
	words = ["HE", "HEY", "HELLOS", "HELL", "GELL",
		"HELLO", "HI", "HA"]
	import_file = "./language/words_short.txt"
	wordlist = lang.import_dictionary(import_file)

	for w in words:
		assert w in wordlist