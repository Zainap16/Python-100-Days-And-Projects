import random
# lives = 6
words = ["apple","pear","catty"]

# random word thru list
ran_word = random.choice(words)

# put _ down for each letter

len_word = len(ran_word)
 
print(ran_word)   
# take user input

display = ""
for lives in range(5):
    guess = input("Enter character: ").lower()
  

    for char in ran_word:
        if char == guess:
            display += char
        else:
            display += "_"
                
        print(display)       
    
  
# compare user input to word[ran_word]
