def max_of_three(a, b, c):
    return max(a, b, c)

def reverse_string(s):
    return s[::-1]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    # Task 1: Max of three numbers
    print("1. Max of three numbers:")
    numbers = (10, 5, 8)
    result = max_of_three(*numbers)
    print(f"The maximum of {numbers} is: {result}")

    # Task 2: Reverse a string
    print("\n2. Reverse a string:")
    sample_string = "1234abcd"
    reversed_string = reverse_string(sample_string)
    print(f"Original string: {sample_string}")
    print(f"Reversed string: {reversed_string}")

    # Task 3: Calculate factorial
    print("\n3. Calculate factorial:")
    number = 5
    fact = factorial(number)
    print(f"The factorial of {number} is: {fact}")

if __name__ == "__main__":
    main()