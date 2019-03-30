import language.language_help as lang

# Given a file with words in it and a phone number, wordifies
#   that phone number.
class wordifier:

    def __init__(self, number, fname = "./language/words_alpha.txt"):
        self.phone_number = number.replace('-','')

        self.words = lang.import_dictionary(fname)

        # Keep only words which could appear SOMEWHERE in the string
        #   as well as A and I (exclude other letters as "words", e.g. 'F')
        # This decision was arbitrary
        self.words = list(filter(lambda w: len(w) > 1, self.words))
        self.words += ['A', 'I']
        self.words = list(
            filter(lambda w: lang.C_to_N(w) in self.phone_number, self.words) 
            )
        # Sorting words is important so we know how all shorter numbers
        #   get wordified as we build up a set of wordifications
        self.words = sorted(self.words, key = lambda w: len(w))

        # Pre-allocate the dictionary for speed
        length = len(number)    
        dict_nums = set([
            self.phone_number[i:j+1] for i in xrange(length) for j in xrange(i,length)
            ])
        self.N_to_C_dict = dict.fromkeys(dict_nums)

        # No initial wordifications for each number
        for k in self.N_to_C_dict.keys():
            self.N_to_C_dict[k] = set([])

        # Add each number substring which is a word to the dictionary in order from 
        #   smallest words to largest words
        for w in self.words:
            key = lang.C_to_N(w)
            # self.add_number_word(key, '-' + w + '-')
            self.add_number_word(key, w)

    # See self.wordifier()
    def __call__(self, number):
        return self.wordifier(number)
        

    # Given a number, return all of its possible wordifications
    def wordifier(self, number):
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

        if len(number) > 1:
            # Iterate over where we split the number into two sub-numbers
            #   that we wordify and stich together with all wordifications
            #   of the split number
            for j in range(len(number)):
                split_chars = self.wordifier(number[j])
                lower = self.wordifier(number[:j])
                upper = self.wordifier(number[j+1:])
                # If we split on the first character
                if len(lower) == 0:
                    lower = set([''])
                # If we split on the last character
                if len(upper) == 0:
                    upper = set([''])

                # Add all possible wordifications to the dictionary
                for p in split_chars:
                    for prefix in lower:
                        for suffix in upper:
                            self.N_to_C_dict[number].add(
                                prefix + p + suffix
                                )
        return self.N_to_C_dict[number]