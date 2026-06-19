#Multiplication using exception handling

def multiply():
    try:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        result=a*b
        print(f"Result={result}")
    except ValueError:
        print("enter valid number")
        
multiply()
        
        