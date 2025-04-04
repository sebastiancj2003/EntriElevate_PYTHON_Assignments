month_number = int(input("Enter a number (1-12): "))

if 1 <= month_number <= 12:
     months = [ "January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]
     print("Month:", months[month_number - 1])
else:
     print("Invalid input. Please enter a number between 1 and 12.")


#Ex-2:Ticket price
age = int(input("Enter your age:22"))

if age < 3:
     print("Your ticket costs: $0.00")
elif 3 <= age <= 12:
     print("Your ticket costs: $12.00")
elif age > 12:
     print("Your ticket costs: $25.00")
else:
     print("Invalid age.")


# Ex no:3 - Body Mass Index (BMI) Calculator

# Taking weight and height input from the user
weight = float(input("Enter your weight (in kg):"))
height = float(input("Enter your height (in meters): "))

# Calculating BMI
bmi = weight / (height ** 2)

# Displaying the BMI value
print(f"Your BMI is: {bmi:.2f}")

# Determining the BMI category
if bmi < 18.5:
    print("You are in the underweight range.")
elif 18.5 <= bmi <= 24.9:
    print("You are in the normal range.")
elif 25 <= bmi <= 29.9:
    print("You are in the overweight range.")
else:
    print("You are in the obesity range.")


# ExNo:4 - Program to find the greatest of three numbers

# Taking three numbers as input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Finding the greatest number using the max() function
greatest = max(num1, num2, num3)

# Displaying the result
print("The greatest number is:", greatest)

# Exno:5
num = int(input("Enter a number: "))
factorial = 1

if num < 0:
   print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, num + 1):
         factorial *= i
   print(f"The factorial of {num} is: {factorial}")



# ExNo:6
num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
  digit = num % 10
  reversed_num = reversed_num * 10 + digit
  num //= 10

print("Reversed number:", reversed_num)


# Exno:7
num = int(input("Enter a number: "))
limit = int(input("Enter the range limit: "))

print(f"Multiples of {num} up to {limit}:")
for i in range(1, limit + 1):
    if i % num == 0:
        print(i)


# Exno: 8

while True:
    value = input("Enter a value (type 'done' to stop): ")
    if value.lower() == "done":
        print("Done")
        break
    print(f"You entered: {value}")


# Exno: 9

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# ExNo: 10

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()





