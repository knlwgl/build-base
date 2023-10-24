import argparse
import random
import string
import sys

parser = argparse.ArgumentParser(prog='xkcdpwgen', description='Generate a secure, memorable password using the XKCD '
                                                               'method')

parser.add_argument("-w", "--words", type=int, metavar="WORDS", default=4, help="include WORDS words in the password "
                                                                                "(default=4)")
parser.add_argument("-c", "--caps", type=int, metavar="CAPS", default=0, help="capitalize the first letter of CAPS "
                                                                              "random words (default=0)")
parser.add_argument("-n", "--numbers", type=int, metavar="NUMBERS", default=0, help="insert NUMBERS random numbers in "
                                                                                    "the password (default=0)")
parser.add_argument("-s", "--symbols", type=int, metavar="SYMBOLS", default=0, help="insert SYMBOLS random symbols in "
                                                                                    "the password (default=0)")

args = parser.parse_args()
sym = args.symbols
num = args.numbers
caps = args.caps
words = args.words

if words < caps:
    sys.stderr.write("Requested number of capitalized words exceeds number of words.")
    sys.exit(1)

wordlist = list()
with open('words.txt') as l:
    for line in l:
        wordlist.append(line.rstrip('\n'))

pwd = list()
for x in range(words):
    word = random.choice(wordlist)
    pwd.append(word)

for x in range(caps):
    rand = random.choice(pwd)
    while rand[0].isupper():
        rand = random.choice(pwd)
    new = rand.capitalize()
    pwd.insert(pwd.index(rand), new)
    pwd.remove(rand)

for x in range(num):
    pwd.insert(random.randrange(len(pwd)), str(random.randrange(9)))

for x in range(sym):
    pwd.insert(random.randrange(len(pwd)), random.choice(string.punctuation))

print("".join(pwd))
