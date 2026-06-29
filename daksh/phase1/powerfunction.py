# power function with exception 
def Power():
    
    try:
        a=int(input("enter first no."))
        b=int(input("enter second no."))
        result=a**b
        print(f"Result={result}")
    except ValueError:
        print("enter valid number")
        
Power()