#  Funtions for operations

def sum(a,b):
    return a + b
    
def diff(a,b):
    return a - b

def div(a,b):
    return a/b

def mul(a,b):
    return a*b

a = float(input("Enter the first number : "))
op = input("Enter the operator : ")
b = float(input("Enter the second number : "))

if op == "/" and b == 0:
    print("ERROR, Divission not possible with 0")

else:
    if op == "+":
        print("result : ", sum(a,b))

    if op == "-":
        print("result : ", diff(a,b))

    if op == "*":
        print("result : ", mul(a,b))

    if op == "/":
        print("result : ", div(a,b))

