import argparse

from number_to_words import *
from words_to_number import *
from all_wordifications import *

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--number", action = "store",
    dest = "number", help = "Find a single wordification of phone number")
parser.add_argument("-w", "--word", action = "store",
    dest = "word", help = "Convert wordified number to phone number")
parser.add_argument("-a", "--all", action = "store",
    dest = "all", help = "Find all wordifications of phone number")
parser.add_argument("-d", "--dict", action = "store",
    dest = "dict", default = "./language/words_alpha.txt",
    help = "Specify custom dictionary")

def main(args):
    # Wordify a given phone number and print out one wordification
    if args.number != None:
        w = number_to_words(args.number, args.dict)
        print("Wordified number:", w)
        return w

    # De-wordify a string into the form 1-800-123-4567
    if args.word != None:
        n = words_to_number(args.word)
        print("Number from wordification:", n)
        return  n

    # Wordify a given phone number and int out all possible wordifications
    if args.all != None:
        all_w = all_wordifications(args.all, args.dict) 
        print("Found {} wordifications".format(len(all_w)))
        for i,w in enumerate(all_w):
            print(i+1, w)
        return  all_w


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)