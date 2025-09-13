from operations import * 

result = 0

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

c = input("Select the number of the operation:\n" +
                "+\n" +
                "-\n" +
                "*\n" +  
                "/\n" +
                "AC\n" +
                "E:\t")

while c != 'E' :
    if c == '+' :
        result = addition(a,b)
    elif c == '-' :
        result = subtraction(a,b)
    elif c == '*' :
        result = multiplication(a,b)
    elif c == '/' :
        result = division(a,b)
    elif c == 'AC' :
        result = 0
    print(result)
    c = input("Select the number of the operation:\n" +
                "+\n" +
                "-\n" +
                "*\n" +  
                "/\n" +
                "AC\n" +
                "E:\t")
    a=result
    b=int(input("Enter a number: "))


print("Thank you!")