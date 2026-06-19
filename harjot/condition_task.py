def calculate_grade(marks):
    if 0< marks >100:
        return "invalid marks"
        
    if marks>90:
        return(f"outstanding")
    elif marks>80:
        return(f"excellent")
    elif marks>70:
        return(f"verygood")
    elif marks>60:
        return(f"good")
    elif marks>=50:
        return(f"pass")
    else:
        return(f"need improvement")
try:    
    user_marks=int(input("Enter your marks:"))

    result=calculate_grade(user_marks)
    print(f"Result:{result}")
except ValueError:
    print("please enter valid numeric value")

