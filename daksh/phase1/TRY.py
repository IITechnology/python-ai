# division by zero
try:
    a=int(input("enter numerator"))
    b=int(input("enter denominator"))
    result=a/b
    print(f"Result is={result}")
except:
    print(f"cannot divide by zero")
