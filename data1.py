# lyric = 'The night begin to shine, the night begin to shine'
# words = lyric.split()
# print(words)

import string

path = '/Users/hyh/Desktop/temp/Walden.txt'
with open(path, 'r') as text:
    # words = text.read().split()
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    counts_dict = {index:words.count(index) for index in words_index}
    # print(words)

# for word in words:
for word in sorted(counts_dict,key=lambda x: counts_dict[x],reverse=True):
    print('{}-{} times'.format(word, words.count(word)))