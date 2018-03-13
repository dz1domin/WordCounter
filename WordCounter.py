import argparse

parser = argparse.ArgumentParser(description='Program for parsing files similar to linux word counter')
parser.parse_args()

wordcount = 0

file = open('loremipsum.txt', 'r')
for line in file:
    newstring = line.split()
    wordcount += len(newstring)

print(wordcount)

file.close()
