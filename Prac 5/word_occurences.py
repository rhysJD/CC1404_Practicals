"""
CP1404 Practical 5
Rhys Donaldson
"""

in_string = input("Text\n >>> ").lower()
in_words = in_string.split(" ")
words_dict = {}

for word in in_words:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

in_words = list(words_dict.keys())
word_max = max(len(word) for word in in_words)
for word in in_words:
    print("{:{}} = {}".format(word, word_max, words_dict[word]))

