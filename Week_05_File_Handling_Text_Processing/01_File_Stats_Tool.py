"""
TASK: 01 File Stats Tool

# Read a .txt file and compute:
Task:
- Number of lines
- Number of words
- Number of characters
- Most frequent word

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def filestats(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    numlines = len(lines)
    fulltext = "".join(lines)
    numchar = len(fulltext)
    words = fulltext.split()
    numwords = len(words)
    if words:
        wordcounts = {}
        for word in words:
            word = word.lower()
            if word in wordcounts:
                wordcounts[word] += 1
            else:
                wordcounts[word] = 1
        mostfreqword = max(wordcounts, key=wordcounts.get)
    else:
        mostfreqword = None
    return numlines, numwords, numchar, mostfreqword

filetotest = "scores.txt"
filestats(filetotest)