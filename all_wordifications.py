import wordifier

def all_wordifications(number, fname = "./language/words_alpha.txt"):
	worder = wordifier.wordifier(number, fname)
	wordified = worder(number.replace('-',''))
	wordified = set([w.replace('--','-') for w in wordified])

	return wordified

print(all_wordifications("1-800-7246837"))