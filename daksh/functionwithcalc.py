def add(a,b):
    return a+b
def power(a,b):
    return a**b
try:
    
    a=int(input("enter first number"))
    b=int(input("enter second number"))

    add_result=add(a,b)
    power_result=power(a,b)
    print(f"Add result:{add_result}")
    print(f"Power result is:{power_result}")
 
except ValueError:
    print(f"invalid")
except ZeroDivisionError:
    print(f"error in division ")
except Exception as e:
    print(f"an unexpected error {e}")
finally: 
    print(f"code executed sucessfully")
         

