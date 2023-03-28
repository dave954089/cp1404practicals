"""
CP1404
Est: 25 min
Act: 27 min
"""

word_to_count = {}
text = input("text: ")
words = text.split()
for word in words:
    count = word_to_count.get(word, 0)
    word_to_count[word] = count+1
for word in words:
    print(f"{word} : {word_to_count[word]}")