words = ('attack', 'bless', 'look', 'short', 'monster', 'sound')

words_with_position = list(enumerate(words, start=1))

for number, word in words_with_position:
    print(f"Word with index {number} = {word}")
