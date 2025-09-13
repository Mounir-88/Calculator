from operations import *

result = 0
off = False

result = float(input("1:: "))

while not off:
    
    op = input("2:: ")
    
    if op == operations[4]:
        print(result)
        continue

    if op not in operations:
        off = True
        break
    
    nbr = float(input("3:: "))
    result = expression(op, result, nbr)
    print(result)
    




print("Thank you!")