import argparse

parser = argparse.ArgumentParser(description='Program for parsing files similar to linux word counter')

parser.add_argument('file', type=argparse.FileType('r'), help='Enter filename including its extension, that you would '
                                                              'like to use this program on(required argument)')

parser.add_argument('-cl', '--COUNTLINES', help='Use this option to count all line in a given file',
                    action='store_true', dest='cl', default=False)

parser.add_argument('-cw', '--COUNTWORDS', help='Use this option to count all words in a given file',
                    action='store_true', dest='cw', default=False)

parser.add_argument('-cc', '--COUNTCHARS', help='Use this option to count all alphabetic characters in the given file',
                    action='store_true', dest='cc', default=False)


def count(cl, cw, cc, file):
    linecount = 0
    wordcount = 0
    charcount = 0
    for line in file:
        if cl:
            linecount += 1
        if cw:
            for singlestr in line.split():
                wordcount += singlestr.isalpha()
        if cc:
            for singlechar in line:
                charcount += singlechar.isalpha()
    if linecount:
        print('Line count: ', linecount)
    if wordcount:
        print('Word count: ', wordcount)
    if charcount:
        print('Char count: ', charcount)


args = parser.parse_args()

count(args.cl, args.cw, args.cc, args.file)



