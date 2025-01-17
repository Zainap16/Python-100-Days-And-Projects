print("Welcome to tip calculator!")
total_bill = float(input("What was the total bill?: "))
amt_tip = int(input("How much tip would you give? 10, 12, or 15: "))
ppl_bill = int(input("How many people to split the bill?: "))
tip = amt_tip / 100
# too lazy to math

print(f"Each person should pay: {amt_tip}")