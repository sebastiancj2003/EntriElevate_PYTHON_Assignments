# Exercise 1

try:
    file_1 = input("Enter the file name: ")
    with open(file_1, 'r') as file:
        content = file.read()
    print("File contents:")
    print(content)
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


# Exercise 2

try:
    source_file = input("Enter the source file name: ")
    destination_file = input("Enter the destination file name: ")

    with open(source_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)

    print(f"Contents of '{source_file}' copied to '{destination_file}'.")
except FileNotFoundError:
    print("The source file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")



# EXERCISE 3

try:
    filename = input("Enter the file name: ")
    with open(filename, 'r') as file:
        content = file.read()
    words = content.split()
    print(f"The file contains {len(words)} words.")
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


# EXERCISE 4

try:
    user_input = input("Enter a string: ")
    number = int(user_input)
    print(f"Converted integer: {number}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")


# EXERCISE 5

try:
    user_input = input("Enter a list of integers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    for num in numbers:
        if num < 0:
            raise ValueError("Negative numbers are not allowed.")
    print("All numbers are positive.")
except ValueError as e:
    print(f"Error: {e}")


# EXERCISE 6

try:
    user_input = input("Enter a list of integers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    average = sum(numbers) / len(numbers)
    print(f"The average is {average:.2f}.")
except ZeroDivisionError:
    print("Error: Cannot compute the average of an empty list.")
except ValueError:
    print("Error: Please enter valid integers.")
finally:
    print("Program execution completed.")


# EXERCISE 7

try:
    filename = input("Enter the file name: ")
    content = input("Enter the content to write to the file: ")

    with open(filename, 'w') as file:
        file.write(content)

    print(f"Content written to '{filename}' successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("Welcome! No exceptions occurred.")
