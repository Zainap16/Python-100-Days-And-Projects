import random
import game_data

# get dict print it
data = game_data.data

points = 0
'''
{
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
'''

def compare():
    global compare_a_followers
    global compare_b_followers
    global compare_b
    global compare_a
    # compare a value
    compare_a_item = random.randrange(0, len(data))
    compare_a = data[compare_a_item]
    compare_a_followers = data[compare_a_item]["follower_count"]
    print(f"compare_a: {compare_a}\nfollower numbers: {compare_a_followers}")
    # compare b value
    compare_b_item = random.randrange(0, len(data))
    compare_b = data[compare_b_item]
    compare_b_followers = data[compare_b_item]["follower_count"]
    print(f"compare_b: {compare_b}\nfollower numbers: {compare_b_followers}")



# who has more followers? A or B?
while points >= 0:
    compare()
    user_guess = input("Who has more followers A or B: ").lower()


    if user_guess == "a":
        if compare_a_followers > compare_b_followers:
            print("Point earned")
            points += 1
        elif compare_a_followers < compare_b_followers:
            print("Point lost")
            points -= 1
            break
    elif user_guess == "b":
        if compare_b_followers > compare_a_followers:
            print("Point earned")
            points += 1
        elif compare_b_followers < compare_a_followers:
            print("Point lost")
            points -= 1
            break

print(f"Points: {points}")
# point += 1
# keep running til you lose
'''
import random
import game_data

data = game_data.data
points = 0

def compare():
    compare_a_item = random.randrange(0, len(data))
    compare_a = data[compare_a_item]
    compare_a_followers = compare_a["follower_count"]

    compare_b_item = random.randrange(0, len(data))
    compare_b = data[compare_b_item]
    compare_b_followers = compare_b["follower_count"]

    print(f"compare_a: {compare_a}\nfollower numbers: {compare_a_followers}")
    print(f"compare_b: {compare_b}\nfollower numbers: {compare_b_followers}")

    return compare_a_followers, compare_b_followers

# Game loop
while points >= 0:
    compare_a_followers, compare_b_followers = compare()  # Get returned values

    user_guess = input("Who has more followers A or B: ").lower()

    if user_guess == "a" and compare_a_followers > compare_b_followers:
        print("Point earned")
        points += 1
    elif user_guess == "b" and compare_b_followers > compare_a_followers:
        print("Point earned")
        points += 1
    else:
        print("Point lost")
        points -= 1
        break

'''
