##List
##Q1.Create a list of 5 random numbers and print the list
import random
numbers = [random.randint(1, 100) for _ in range(5)]
print("List of random numbers:", numbers)
 ##Q2.Insert 3 new values to the list and print the updated list
numbers.extend([200, 300, 400])  # Adding 3 new values
print("Updated list:", numbers)
 ##Q3.Use a for loop to print each element in the list
for num in numbers:
print(num)

##Dictionary
##Q1: Create a dictionary with keys name, age, and address and values John, 25, and New York.
person = {
    "name": "John",
    "age": 25,
    "address": "New York"
}
print("Dictionary:", person)
##Q2: Add a new key-value pair with key phone and value 1234567890.

person["phone"] = "1234567890"
print("Updated dictionary:", person)


##Set
# ##Q1: Create a set with values 1, 2, 3, 4, and 5.
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

##Q2:Add the value 6 to the set.
my_set.add(6)
print("Set after adding 6:", my_set)

##Q3: Remove the value 3 from the set.
my_set.discard(3)  # Use discard to avoid error if 3 doesn't exist
print("Set after removing 3:", my_set)


##Tuple
##Q1: Create a tuple with values 1, 2, 3, and 4.
my_tuple = (1, 2, 3, 4)
print("Tuple:", my_tuple)
##Q2: Print the length of the tuple.
print("Length of tuple:", len(my_tuple))
