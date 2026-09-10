"""
TASK: 05 String Parser

# String Parser
Write a parser that:
- Accepts a sentence from the user.
- Splits it into words manually (not using split()).
- Outputs number of words + list of words.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def string_parser(sentence):
    words = []
    currentword = []
    for char in sentence:
        if char.isspace():
            if currentword:
                words.append("".join(currentword))
                currentword = []
        else:
            courrent.append(char)
    if currentword:
        words.append("".join(currentword))
    return words

def string_input(:
    userinput = input("Enter a sentence:")
    wordlist = manual_split(userinput)
    wordcount = len(wordlist)
    print("Number od words:", wordcount)
    print("List of words":)

if __name__ == "__main__":
    print("Running string parser")
    string_input()
