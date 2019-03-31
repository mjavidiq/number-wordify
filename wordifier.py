import language.language_help as lang

# Given a file with words in it and a phone number, wordifies
#   that phone number.
class wordifier:

    def __init__(self, number, fname = "./language/words_alpha.txt"):
        self.phone_number = number.replace('-','')
        self.words = lang.import_dictionary(fname)

        # Keep only words which could appear SOMEWHERE in the string
        self.words = list(
            filter(lambda w: lang.C_to_N(w) in self.phone_number, self.words) 
            )
        # Sorting words is important so we know how all shorter numbers
        #   get wordified as we build up a set of wordifications
        self.words = sorted(self.words, key = lambda w: len(w))

        # Pre-allocate the dictionary for speed
        length = len(number)    
        dict_nums = set([
            self.phone_number[i:j+1] for i in range(length) for j in range(i,length)
            ])
        self.N_to_C_dict = dict.fromkeys(dict_nums)

        # No initial wordifications for each number
        for k in self.N_to_C_dict.keys():
            self.N_to_C_dict[k] = set([])

        # Add each number substring which is a word to the dictionary in order from 
        #   smallest words to largest words
        for w in self.words:
            key = lang.C_to_N(w)
            self.add_number_word(key, '-' + w + '-')
            # self.add_number_word(key, w)

    # Given a number, return all of its possible wordifications
    def wordify(self, number):
        if len(number) == 0: 
            return set([])

        if self.N_to_C_dict[number] == set([]):
            return self.add_number_word(number, number)
        
        return self.N_to_C_dict[number]

    # Add a number which translates to some given word to the dictionary,
    #   and then construct all of its sub-wordifications using the smaller
    #   wordifications already in the dictionary
    def add_number_word(self, number, word):
        if len(number) == 0:
            return set([])
        # A number can wordify to itself or the given word
        self.N_to_C_dict[number].add(word)
        self.N_to_C_dict[number].add(number)

        # Iterate over where we split the number into two sub-numbers
        #   that we wordify and stich together with all wordifications
        #   of the split number
        if len(number) > 1:
            for j in range(len(number)-1):
                lower = self.wordify(number[:j+1])
                upper = self.wordify(number[j+1:])
                for prefix in lower:
                    for suffix in upper:
                        self.N_to_C_dict[number].add(prefix + suffix)
        return self.N_to_C_dict[number]