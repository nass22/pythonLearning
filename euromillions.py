# import random

# tab_5_numbers = []
# tab_2_stars = []

# def random_number(n):
#     random_number = random.randint(1,n)
#     return random_number

# def euromillions_numbers():
#     for i in range(0,5):
#         number = random_number(50)
#         while number in tab_5_numbers:
#             number = random_number(50)

#         tab_5_numbers.append(number)

# def euromillions_stars():
#     for i in range(0,2):
#         number = random_number(12)
#         while number in tab_2_stars:
#             number = random_number(12)

#         tab_2_stars.append(number)

# euromillions_numbers()
# euromillions_stars()

# tab_5_numbers.sort()
# tab_2_stars.sort()

# print(f"Votre grille: {tab_5_numbers}   {tab_2_stars}")

import random

# Generate 5 different random numbers between 1 and 50
euromillions_numbers = random.sample(range(1, 51), 5)
euromillions_numbers.sort()

# Generate 2 different random numbers between 1 and 12
lucky_stars = random.sample(range(1, 13), 2)
lucky_stars.sort()

print("Euromillions numbers:", euromillions_numbers)
print("Lucky stars:", lucky_stars)


