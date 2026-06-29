def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b

try:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        
        addition=add(a,b)
        subtraction=subtract(a,b)
        multiplication=multiply(a,b)
        divide=division(a,b)
        
        print(f"ADDITION RESULT={addition}")
        print(f"SUBTRACTION RESULT={subtraction}")
        print(f"MULTIPLICATION RESULT={multiplication}")
        print(f"DIVISION RESULT={divide}")
except ValueError:
        print("ENTER VALID NUMBER")
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("code executed successfully")
    
add(a,b)
subtract(a,b)
multiply(a,b)
division(a,b)
        