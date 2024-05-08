# factorial Itrative


def factorial_iterative(n):
    "Calculate the factorial of a non-negative integer using an iterative approach"
    if n < 1:
        return 0
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result


# factorial recursive
def factorial_recursive(n):
    "Calculate the factorial of a non-negative integer using a recursive approach."
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


# clumsy
def clumsy(n):

    "This function calculates the clumsy factorial of a positive integer n."

    # Define the operation cycle
    operations = ["*", "/", "+", "-"]
    current_op = 0

    # Initialize stack with n (fix for n=1 case)
    stack = [n]

    # Loop through numbers from n-1 to 1
    for i in range(n - 1, 0, -1):

        if operations[current_op] == "*":
            stack[-1] *= i
        elif operations[current_op] == "/":

            stack[-1] = int(stack[-1] / i)
        elif operations[current_op] == "+":
            stack.append(i)
        elif operations[current_op] == "-":
            stack.append(-i)

        current_op = (current_op + 1) % 4

    return sum(stack)
