# # #Ex 1:
print('Sebastian')
print('DM2582')
print('sebcj2582@gmail.com')

# #Ex 2:
print('Sebastian\nDM2582\nsebcj2582@gmail.com')

# # #Ex 3:
number_1 = 14
number_2 = 7
print(f'print(f"sum={number_1+number_2},difference={number_1-number_2},multiplication={number_1*number_2},division={number_1/number_2}")')

# # #Ex 4
for i in range(1,6):
    print(i)

    # #Ex 5
    print('\"SDK\" stands for \"Software Development Kit\", whereas \"IDE\" stands for \"Integrated Development Environment\".')

    # # #Ex 6
    print('python is an \"awesome \"language.')
    print("python\n\t2023")
    print('I\'m from Entri.\b')
    print("\65")
    print("\x65")

# #Ex 7
num=23
textnum = "57"
decimal=98.30
total=num=int(textnum)+decimal
print(f"num:{type(num)}")
print(f"textnum:{type(textnum)}")
print(f"decimal {type(decimal)}")
print(f"sum:{total}")

# #Ex 8
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60
total_minutes = days_in_year * hours_in_day * minutes_in_hour
print(f"Total minutes in a year: {total_minutes}")

# #Ex 9
name = input("Please enter your name: ")
print(f"Hi {name}, welcome to Python programming :)")

# #Ex 10
# File name: PoundsToDollars.py
pounds = float(input("Please enter amount in pounds: £"))
conversion_rate = 1.25
dollars = pounds * conversion_rate
print(f"£{pounds} is ${dollars:.2f}")