word = input("Enter word: ")
char = word[0].upper()

new_word = word.replace(word[0],char,1)
print(new_word)
