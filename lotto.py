# import random

# tab_6_numbers = []
# tab_2_stars = []

# def random_number(n):
#     random_number = random.randint(1,n)
#     return random_number

# def lotto_numbers():
#     for i in range(0,6):
#         number = random_number(45)
#         while number in tab_6_numbers:
#             number = random_number(45)

#         tab_6_numbers.append(number)

# lotto_numbers()

# tab_6_numbers.sort()

# print(f"Votre grille: {tab_6_numbers}")

import random

# Generate 5 different random numbers between 1 and 45
euromillions_numbers = random.sample(range(1, 46), 6)
euromillions_numbers.sort()



print("Lotto numbers:", euromillions_numbers)