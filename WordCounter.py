import argparse

parser = argparse.ArgumentParser(description='Program for parsing files similar to linux word counter')
parser.add_argument('file', nargs='?', type=argparse.FileType('r'), help='Name file to parse')
parser.add_argument('-cl', '--COUNTLINES', help='Option to count lines in a given file')
args = parser.parse_args()
filename = args.file

wordcount = 0
linecount = 0
scannedline = ''

if filename is not None:
    for line in filename:
        linecount += 1
        wordcount += len(line.split())
else:
    print('No file given, use -h option to see proper syntax')


print('Number of lines:', linecount, " Number of words: ", wordcount)


