import os
import sys
import fileinput

print("Text to search for:")
textToSearch = input("> ")

print("Text to replace it with:")
textToReplace = input("> ")

print("File to perform Search-Replace on:")
fileToSearch = input("> ")

tempFile = open(fileToSearch, 'r+')

for line in fileinput.input(fileToSearch):
    if textToSearch in line:
        print('Match Found')
    else:
        print('Match Not Found!!')
    tempFile.write(line.replace(textToSearch, textToReplace))
tempFile.close()

input('\n\n Press Enter to exit...')
