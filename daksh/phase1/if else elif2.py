A=float(input("enter first number"))
B=float(input("enter second number"))
op=input("enter operator:(+,-,*,/):")

if op=='+':
    print(f"Result is:{A+B}")
elif op=='-':
    print(f"Result is:{A-B}")
elif op=='*':
    print(f"Result is:{A*B}")
elif op=='/':
    print(f"Result is:{A/B}")
    
else:
    print("INVALID OPERATOR")
    