import random
# random.randint(start, stop)
# print(random.randint(0, 1))
user = int(input("What do you choose? type 0 = rock, 1 = Paper , 2 = Scissors: "))
computer = random.randint(0, 2)
print(computer)

if user == computer:
    print("draw")
elif computer > user:
    print("you lose")
elif user == 0 and computer == 2:
    print("you win!")
else:
    print("invalid")