def add_two_numbers(a, b):
    return a+b


def c_area(radius):
    pi = 3.14159
    return pi*radius**2


def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total


def temp(celsius):
    return (celsius*9/5)+32


def calculate_slope(x1, x2, y1, y2):
    return (y2-y1)/(x2-x1)


def solve_quadratic(a, b, c):
    disc = b**2-4*a*c
    if disc < 0:
        return "No real roots"
    elif disc == 0:
        return -b/(2*a)
    else:
        root1 = (-b+disc**0.5)/(2*a)
        root2 = (-b-disc**0.5)/(2*a)
        return root1, root2


def print_list(lst):
    for item in lst:
        print(item)


def reverse_list(arr):
    list = []
    for i in range(len(arr)-1, -1, -1):
        list.append(arr[i])
    return list


def capitalize_list(lst):
    return [item.capitalize()for item in lst]


def add_item(lst, item):
    lst.append(item)
    return lst


def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst


def sum_of_numbers(a):
    total = 0
    for i in range(a+1):
        total += i
    return total


def sum_of_odds(a):
    total = 0
    for i in range(a+1):
        if i % 2 != 0:
            total += i
    return total


def sum_of_evens(a):
    total = 0
    for i in range(a+1):
        if i % 2 == 0:
            total += i
    return total


def evens_and_odds(a):
    e = 0
    o = 0
    for i in range(a+1):
        if i % 2 == 0:
            e += 1
        else:
            o += 1
    return f"The number of odds are {o}\nThe number of evens are {e}."


def factorial(n: int):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
    return result


def calculate_mean(lst):
    if len(lst) == 0:
        return 0
    return sum(lst)/len(lst)


def calculate_median(lst):
    n = len(lst)
    if n == 0:
        return 0
    sorted_list = sorted(lst)
    mid = n//2
    if n % 2 == 0:
        return (sorted_list[mid-1]+sorted_list[mid+1])/2
    else:
        return sorted_list[mid]


def calculate_mode(lst):
    if len(lst) == 0:
        return None
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    max_freq = max(frequency.values())
    mode = [key for key, value in frequency.items() if value == max_freq]
    return mode


def calculate_variance(lst):
    if len(lst) == 0:
        return 0
    mean = calculate_mean(lst)
    squared_diffs = [(x - mean) ** 2 for x in lst]
    return sum(squared_diffs) / len(lst)


def calculate_standard_deviation(lst):
    return calculate_variance(lst) ** 0.5


def greet(name):
    if name == "":
        return "Hello, Guest! "
    else:
        return f"Hello, {name}!"


def show_args(**args):
    for key, value in args.items():
        print(f"{key}: {value}")


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def is_unique(lst):
    return len(lst) == len(set(lst))


def is_same_datatype(lst):
    if len(lst) == 0 or len(lst) == 1:
        return True
    f_type = type(lst[0])
    for item in lst:
        if not isinstance(item, f_type):
            return False
    return True


def valid_variable(a):
    if not a.isidentifier():
        return False
    return True


print(add_two_numbers(3, 5))
print(valid_variable("my_var"))
print(c_area(5))
print(add_all_nums(1, 2, 3, 4, 5))
print(temp(25))
print(calculate_slope(1, 2, 3, 4))
print(solve_quadratic(1, -3, 2))
print(print_list([1, 2, 3, 4, 5]))
print(reverse_list([1, 2, 3, 4, 5]))
print(capitalize_list(["hello", "world"]))
print(add_item([1, 2, 3], 4))
print(remove_item([1, 2, 3, 4], 3))
print(sum_of_numbers(10))
print(sum_of_odds(10))
print(sum_of_evens(10))
print(evens_and_odds(10))
print(factorial(5))
print(calculate_mean([1, 2, 3, 4, 5]))
print(calculate_median([1, 2, 3, 4, 5]))
print(greet("Alice"))
print(greet(""))
show_args(name="Alice", age=30)
print(is_prime(7))
print(is_prime(8))
print(is_unique([1, 2, 3, 4, 5]))
print(is_unique([1, 2, 2, 3, 4]))
print(is_same_datatype([1, 2, 3, 4, 5]))
print(is_same_datatype([1, 2, "3", 4, 5]))
