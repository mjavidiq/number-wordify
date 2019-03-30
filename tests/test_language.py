import language.language_help as lang

def test_C_to_N():
	assert lang.C_to_N('C') == '2'
	assert lang.C_to_N('Z') == '9'

def test_small_words():
	corpus = lang.corpus("./language/words_short.txt")
	assert corpus('4') == set(['I','4'])
	assert corpus('43') == set(['HE','43'])
	assert corpus('4355') == set(['4355','HELL','GELL'])
