def multiple(*args):
    result = 1
    for number in args:
        result *= number
    return result

print(multiple(4, 2, 1))




def mirror(word, hello='hello'):
    if word == hello:
        return False
    word = word.replace(" ", "").lower()
    return word == word[::-1]


print(mirror('maks skam'))
print(mirror('hello'))
print(mirror('Python'))


def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return("Division by zero is not allowed.")
    elif operator == '**':
        return num1 ** num2
    elif operator == '%':
        return num1 % num2
    else:
        raise ValueError("Invalid operator. Supported operators are '+', '-', '*', '/', '**', and '%'.")

print(calculator(2, '**', 3))
print(calculator(5, '+', 9.6))
print(calculator(20, '%', 3))

