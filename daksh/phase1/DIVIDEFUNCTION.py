# DIVIDE FUNCTION WITH EXCEPTION HANDLING

def divide():
    try:
                num1=int(input("enter first number="))
                num2=int(input("enter second number="))
            
                result=num1/num2
                print(f"Result= {result}")
            
    except ValueError:
                print("enter valid number")
                
    except ZeroDivisionError:
                print("cannot divide by zero")
    finally:
                print("code executed sucessfully")
                
                
    
divide()            
            
            
    