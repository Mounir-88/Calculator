operations = ['+', '-', '*', '/', '=']

def addition(a, b):
    return a+b

def subtraction(a, b):
    return a-b

def multiplication(a, b):
    return a*b

def division(a, b):
    return a/b

def expression(op, nbr1, nbr2):
    if op == '+':
        return addition(nbr1, nbr2)
    elif op == '-':
        return subtraction(nbr1, nbr2)
    elif op == '*':
        return multiplication(nbr1, nbr2)
    elif op == '/':
        return division(nbr1, nbr2)
    else:
        return nbr1