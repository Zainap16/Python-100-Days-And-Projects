import menu_caffe
'''

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
'''
menu = menu_caffe.MENU
resource = menu_caffe.resources

# prompt user // loop
user_choice_coffee = input("What would you like? (espresso/latte/cappuccino): ")

# turn off coffee by entering off -- secret word for the above while loop

# print report

if user_choice_coffee.lower() == "report" or user_choice_coffee.lower() == "r":
    for re in resource:
        print(f"{re}: {resource[re]}")
    

# check resources sufficient
# process coins
# check trabsaction successful
# make coffee