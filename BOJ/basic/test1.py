from collections import Counter
word = Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
word_cnt = word['l']
print(word_cnt)