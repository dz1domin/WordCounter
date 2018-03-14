import argparse

parser = argparse.ArgumentParser(description='Program for parsing files similar to linux word counter')
parser.add_argument('file', type=argparse.FileType('r'), help='Name file to parse')

parser.add_argument('-cl', '--COUNTLINES', help='Use this option to count all line in a given file',
                    action='store_true', dest='cl', default=False)

parser.add_argument('-cw', '--COUNTWORDS', help='Use this option to count all words in a given file',
                    action='store_true', dest='cw', default=False)

parser.add_argument('-cc', '--COUNTCHARS', help='Use this option to count all alphabetic characters in the given file',
                    action='store_true', dest='cc', default=False)


def countlines(isTrue, file):
    lineCount =0
    if isTrue:
        for line in file:
            lineCount += 1
        file.seek(0, 0)
        print(lineCount)
    else:
        pass


def countwords(isTrue, file):
    wordCount = 0
    if isTrue:
        for line in file:
            wordCount += len(line.split())
        file.seek(0, 0)
        print(wordCount)
    else:
        pass

def countchars(isTrue, file):
    charcount = 0
    if isTrue:
        for line in file:
            for singlechar in line:
                charcount += int(singlechar.isalpha())
        file.seek(0, 0)
        print(charcount)
    else:
        pass


args = parser.parse_args()

countlines(args.cl, args.file)

countwords(args.cw, args.file)

countchars(args.cc, args.file)



