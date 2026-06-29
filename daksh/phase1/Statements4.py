def calculate_marks(marks):
    if 0< marks> 100:
    
        if marks< 90:
            print(f"OUTSTANDING")
    elif marks< 80:
            print(f"VERY GOOD")
    elif marks< 70:
            print(f"GOOD")
    elif marks< 60:
            print(f"AVERAGE")
    else:
            print(f"NEEDS IMPROVEMENT")
            
try:
    user_marks=int(input("ENTER YOUR MARKS"))
    result=calculate_marks(user_marks)
    print(f"Result is:{result}")
except:
    print(f"enter valid marks")
    

