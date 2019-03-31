# Overview 
Wordification is the process of taking a phone number and replacing subsets of the numbers with their corresponding characters as defined by the standard US telephone number-to-character mapping (e.g. 2 maps to A, B, and C). The goal is to find representations of the phone number which include English words in place of some or all of the numbers. 

This repository implements three main functions:

1. `words_to_number` takes a string of numbers and capital letters and maps it to the phone number which corresponds to that "wordified" phone number. By default it maps to 10-digit US phone numbers with a leading `1-` but support generic patterns for the phone number. Will only return the initial phone number if there are no valid wordifications for the number.
2. `all_wordifications` which takes as input a reference to a file containing all possible words and a phone number and returns a list of all possible "wordified" phone numbers for that number and list of words sorted by number of dashes present. By convention, the initial phone number is considered a wordification of itself, so there is always at least one wordification (the identity). This function works for any phone numbers which are no longer than the longest word in the word list after removing dashes (length 15 for the supplied word list).
3. `number_to_words` which outputs a single wordified version of the input phone number.

# Requirements

This code was written with Python 3.6.7. The requirements can be installed by running `pip install -r requirements.txt` from the root directory of the repository. In practice, only `pytest` should need to be installed.

# Running

Each primary function is located in its own file in the root folder under its respective name. An interface was written which can be accessed by running `python main.py` from the root folder, with the following arguments:

* `-n` or `--number` for `number_to_words` following by the phone number to wordify
* `-w` or `--word` for `words_to_number` followed by the wordified phone number to convert to phone number
* `-a` or `--all` for `all_wordifications` following by the phone number to woridfy

As an example, running

`python main.py -a 1-230-000-0000`

from the root directory of the repository should result in

```
Found 4 wordifications  
1 1-230-000-0000
2 1-AE-0-000-0000
3 1-AD-0-000-0000
4 1-BE-0-000-0000
```

up to some reordering of the wordifications.

In each case the resulting phone number or wordification(s) are printed out. In the first two cases, the printed string is returned. In the latter case, all wordifications are printed and numbered.

`number_to_words` may not return the same value for each run if there are multiple wordifications which use a word of the same length in wordification.

A set of unit tests are written for most modules in this code. To run them, from the root folder run `pytest` and the set of tests in the tests folder will execute.

_Note_: some functions depend on importing files from child folders. For this reason it is recommended that all code is run from the root folder so that both the `tests` folder and the `language` folder are available for importing.

# Approach

`words_to_number` is implemented by iterating over the input string and replacing characters by their corresponding numberas necessary through the use of a Python dictionary. After converting letters to numbers, we fit the resulting string of numbers to a pattern of dashes so that it represents a valid phone number. Although nonstandard patterns may be supplied, the default pattern is a number of the form `1-800-123-4567`.

`all_wordifications` uses knowledge of the input number when importing the dictionary of words to build up a collection of all possible wordifications for all possible subsets of the starting phone number. We compute all possible contiguous substrings of the input phone number and initialize a dictionary with these keys. These keys map to *sets* of possible wordifications of that number string. 

To build this dictionary, we iterate over a list of words which could be present somewhere in our wordified number in order of increasing length. For each word, we add it to the set of possible wordifications for its corresponding number. We then iterate over each element of its number to split the number into two parts. We then iterate over all possible wordifications of the left and right parts and join them with all possible wordifications for the splitting character. Since words are entered into this dictionary in increasing order of length, we are guaranteed to know the wordification for both sides of the split for all possible splits.

`number_to_words` functions similarly to `all_wordifications`, except the dictionary is never constructed. Instead, we simply keep the longest word which fits into the phone number.

# Miscellany

The code is written agnostic of the representation of the phone number, and the dictionary is not hard-coded. It should be possible to wordify phone numbers of any form consisting of numbers and dashes. The restrictions are that the number of digits is less than 15 and the number does not begin or end with a dash.

There is ambiguity as to where are appropriate places to insert dashes in a wordified number. In this project, I have adopted the convention that: 

* All words have a dash `-` preceding and following them, unless they are the first or last piece of the wordified number
* There is never more than one consecutive dash
* If a number was followed by a dash in the original phone number, it should be followed by a dash in the wordified phone number

It is possible to try different dictionaries of words, and I have included a smaller dictionary on which some tests were written. By default all functions will use the full dictionary, however. Function calls to the individual `numbers_to_words` and `all_wordifications` functions can specify a custom dictionary.

# Sources
Used a file of English words taken from https://github.com/jonbcard/scrabble-bot specifically https://github.com/jonbcard/scrabble-bot/blob/master/src/dictionary.txt
