# Overview 
Wordification is the process of taking a phone number and replacing subsets of the numbers with their corresponding characters as defined by the standard US telephone number-to-character mapping (e.g. 2 maps to A, B, and C). The goal is to find representations of the phone number which include English words in place of some or all of the numbers. 

This repository implements three main functions:

1. `words_to_number` takes a string of numbers and capital letters and maps it to the phone number which corresponds to that "wordified" phone number. By default it maps to 10-digit US phone numbers with a leading `1-` but support generic patterns for the phone number.
2. `all_wordifications` which takes as input a reference to a file containing all possible words and a phone number and returns a list of all possible "wordified" phone numbers for that number and list of words. This function should work for any phone numbers which are no longer than the longest word in the word list after removing dashes.
3. `number_to_words` which outputs a single wordified version of the input phone number.

# Running

# Approach

`words_to_number` is implemented by iterating over the input string and replacing characters by their corresponding numberas necessary through the use of a Python dictionary. After converting letters to numbers, we fit the resulting string of numbers to a pattern of dashes so that it represents a valid phone number.

`all_wordifications` uses knowledge of the input number when importing the dictionary of words to build up a collection of all possible wordifications for all possible subsets of the starting phone number. We compute all possible contiguous substrings of the input phone number and initialize a dictionary with these keys. These keys map to *sets* of possible wordifications of that number string. 

To build this dictionary, we iterate over a list of words which could be present somewhere in our wordified number in order of increasing length. For each word, we add it to the set of possible wordifications for its corresponding number. We then iterate over each element of its number to split the number into two parts. We then iterate over all possible wordifications of the left and right parts and join them with all possible wordifications for the splitting character. Since words are entered into this dictionary in increasing order of length, we are guaranteed to know the wordification for both sides of the split for all possible splits.

`number_to_words` functions identically to `all_wordifications`, except that only a single wordification is returned as oppose to a list.

# Sources
Used a file of English words taken from https://github.com/jonbcard/scrabble-bot specifically https://github.com/jonbcard/scrabble-bot/blob/master/src/dictionary.txt
