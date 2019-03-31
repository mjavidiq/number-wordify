import sys

from number_to_words import *
from words_to_number import *
from all_wordifications import *

def main(args):
    function = args[0]
    in_str = args[1]

    # Wordify a given phone number and print out one wordification
    if function == "-n" or function == "--number":
        w = number_to_words(in_str)
        print("Wordified number:", w)
        return w

    # De-wordify a string into the form 1-800-123-4567
    elif function == "-w" or function == "--word":
        n = words_to_number(in_str)
        print("Number from wordification:", n)
        return  n

    # Wordify a given phone number and int out all possible wordifications
    elif function == "-a" or function == "--all":
        all_w = all_wordifications(in_str) 
        print("Found {} wordifications".format(len(all_w)))
        for i,w in enumerate(all_w):
            print(i+1, w)
        return  all_w

    else:
        print("Invalid argument")


if __name__ == "__main__":
    main(sys.argv[1:])