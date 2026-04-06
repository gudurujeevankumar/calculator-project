#  Funtions for operations

def sum(a,b):
    return a + b
    
def diff(a,b):
    return a - b

def div(a,b):
    return a/b

def mul(a,b):
    return a*b

def call(a,b,op):
    if op == "/" and b == 0:
        print("ERROR, Divission not possible with 0")

    else:
        if op == "+":
            res = sum(a,b)

        if op == "-":
            res = diff(a,b)

        if op == "*":
            res = mul(a,b)

        if op == "/":
            res = div(a,b)
    return res

a = float(input("Enter the first number : "))
op = input("Enter the operator : ")
b = float(input("Enter the second number : "))

res = call(a,b,op)

print("Result : ", res)

while True:
    a = res
    op = input("If you want to do another operation give new operator or if don't want any operations to do enter ! : ")
    
    if op == "!":
        break
        
    b = float(input("Enter the new value : "))
    
    if op in ["+","-","/","*"]:
        res = call(a,b,op)
        print("New result : ", res)




