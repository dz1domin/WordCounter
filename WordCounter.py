import argparse
import sys

parser = argparse.ArgumentParser(description='Program for parsing files similar to linux word counter')

parser.add_argument('-f', '--file', type=argparse.FileType('r'), default=sys.stdin, action='store',
                    help='Enter filename including its extension, that you would like to use this program '
                         'on(default is standard input)')

parser.add_argument('-cl', '--COUNTLINES', help='Use this option to count all line in a given file',
                    action='store_true', dest='cl', default=False)

parser.add_argument('-cw', '--COUNTWORDS', help='Use this option to count all words in a given file',
                    action='store_true', dest='cw', default=False)

parser.add_argument('-cc', '--COUNTCHARS', help='Use this option to count all alphabetic characters in the given file',
                    action='store_true', dest='cc', default=False)


def count(cl, cw, cc, stream):
    linecount = 0
    wordcount = 0
    charcount = 0
    for line in stream:
        if cl:
            linecount += 1
        if cw:
            for singlestr in line.split():
                wordcount += singlestr.isalpha()
        if cc:
            for singlechar in line:
                charcount += singlechar.isalpha()
    if cl:
        print('Line count: ', linecount)
    if cw:
        print('Word count: ', wordcount)
    if cc:
        print('Char count: ', charcount)


args = parser.parse_args()

if args.cl or args.cw or args.cc:
    count(args.cl, args.cw, args.cc, args.file)
else:
    print('No options chosen, use -h option to see the other options.')


