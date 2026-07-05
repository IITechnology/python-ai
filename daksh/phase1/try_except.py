def division(a,b):
    return a/b
try:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        divide=division(a,b)
        print(f"DIVISION RESULT={divide}")
except ValueError:
         print("ENTER VALID NUMBER")
except ZeroDivisionError:
    print("cannot divide by zero")
