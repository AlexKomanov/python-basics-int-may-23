def reverse(word_input):
    x = ''
    for i in range(len(word_input)):
        x += word_input[len(word_input) - 1 - i]
    return x


word = input('give me a word:\n')
x = reverse(word)
if x == word:
    print('This is a Palindrome')
else:
    print('This is NOT a Palindrome')
