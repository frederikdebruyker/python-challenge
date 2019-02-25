import os
import re

# variables


# functionality
# myfile = os.path.join(os.path.expanduser('~'),"google drive","rice big data bootcamp","hw", "hw3","resources","TheZennofPython.txt")
myfile = os.path.join(os.path.expanduser('~'),"google drive","rice big data bootcamp","hw", "hw3","resources","language.txt")

word_count = 0
words = []
word_letter_count = 0

with open(myfile,"r") as f:
    for line in f:
        # initialize
        words = []
        line_word_count = 0
        # split line into words
        words = re.split(r'\s+', line)
        # count words
        line_word_count = len(words)
        word_count = line_word_count + word_count
        # split into sentences
        sentences = re.split("(?<=[.!?]) +", line)
        sentence_count = len(sentences)
        # letters per word count
        for word in words:
            word_letter_count = word_letter_count + len(word)

print('Paragraph Analysis')
print('-------------_----')
print(f'Approximate Word Count: {word_count}')
print(f'Approximate Sentence Count: {sentence_count}')
print(f'Average Letter Count: {word_letter_count / word_count}')
print(f'Average Sentence Length: {word_count / sentence_count}')