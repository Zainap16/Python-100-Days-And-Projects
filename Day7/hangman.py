import random
# lives = 6
words = ["apple","pear","catty"]

# random word thru list
ran_word = random.choice(words)

# put _ down for each letter
under = ""
len_word = len(ran_word)
for underscore in range(len_word):
    under += "_"
print(under) 
print(ran_word)   
# take user input
LIVES = 6
while LIVES > 0:
    guess = input("Enter character: ")
    for char in ran_word:
        if char == guess:
            print("CORRECT")
        
    LIVES -= 1
# compare user input to word[ran_word]
