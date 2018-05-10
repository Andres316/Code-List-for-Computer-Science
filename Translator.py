print('Welcome to the Mars Translator!')
sos = 'zuc'
original = input('Enter a word: ')
if len(original) and original.isalpha() > 0:
    word = original.lower()
    second = word[1]
    fourth = word[3]
    new_word = word[2:len(word)] + sos + second + fourth
    print(new_word)
else:
    print('empty')
