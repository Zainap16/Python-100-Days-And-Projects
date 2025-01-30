import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_game = input("do you want to blackjack y or n: ")

if play_game == "y":
#     random choose two random numbers in list
    score_1 = random.randrange(0,len(cards))
    score_2 = random.randrange(0,len(cards))

    # computer
    computer = cards[random.randrange(0,len(cards))]
    print(f"Computer score: {computer}")

    total_score = cards[score_1] + cards[score_2]
    print(f"Total User Score: {total_score}, list: {cards[score_1]},{cards[score_2]}")

    while total_score < 21:
        hit = input("y or n for another hand?")
        if hit == "y":
            score_2 = random.randrange(0,len(cards))
            total_score += cards[score_2]
            print(f"Total Score: {total_score}")

        elif hit == "n" and total_score < 21 and total_score > computer :
            print("You Win")
            break
        else:
            print("You lose")
else:
    print("so not slay")



