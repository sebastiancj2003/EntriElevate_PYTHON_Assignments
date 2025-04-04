# Ex_1

def my_function(arg1, arg2=10, arg3=None):
    if arg3 is None:
        print("Sum:", arg1 + arg2)
    else:
        print("Product:", arg1 * arg2 * arg3)

my_function(5, 10, 15)


# Ex_2

def long_strings(strings):
    return [s for s in strings if len(s) >= 5]

string_list = ["apple", "cat", "elephant", "rat", "banana"]
result = long_strings(string_list)
print(result)


# Ex_3

def eval_expression(expression):
    try:
        result = eval(expression)
        print("Result:", result)
    except Exception as e:
        print("Error evaluating expression:", e)
        fallback_expression = "3 * 5 + 2"
        print("Evaluating fallback expression:", fallback_expression)
        try:
            result = eval(fallback_expression)
            print("Fallback Result:", result)
        except Exception as e2:
            print("Fallback also failed:", e2)



# Ex_4

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def non_primes(numbers):
    return list(filter(lambda x: not is_prime(x), numbers))

number_list = [2, 4, 5, 6, 9, 11, 15]
result = non_primes(number_list)
print(result)



# Ex_5

def convert_to_uppercase(strings):
    return list(map(str.upper, strings))

string_list = ["hello", "world", "python"]
result = convert_to_uppercase(string_list)
print(result)
