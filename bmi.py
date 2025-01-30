# weight = float(input("your weight:"))
# hight = float(input("your hight:"))
# bmi = weight/(hight/100)**2
# print(bmi)
# if bmi <18.5:
#     print("underweight")
# elif bmi <24.9:
#     print("normal weight")
# elif bmi <29.9:
#     print("overweight")
# elif bmi <34.9:
#     print("almost fat")
# else:
#     print("FAT")



# def mark(percent):
#     if percent >=90:
#         return 'A'
#     elif percent >= 75:
#         return 'B'  
#     elif percent >= 65:
#         return 'C'  
#     elif percent >= 50:
#         return 'D'  
#     else:
#         return 'F'  
# percent = float(input("your percent: "))
# grade = mark(percent)
# print(f"your score: {grade}")




# import random

# def numbergame():
    
#     numbergame = random.randint(1, 100)

#     print("Guess the number from 1 to 100:")

#     while True:
#         guess = float(input("Guess: "))

#         if guess == numbergame:
#             print(f"GOT IT! {numbergame}!")
#             break
#         elif abs(numbergame - guess) <= 10:
#             print("Hot!")
#         elif abs(numbergame - guess) <= 20:
#             print("Warm!")
#         else:
#             print("Cold!")

# numbergame()



