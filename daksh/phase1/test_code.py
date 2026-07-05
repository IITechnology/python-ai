def get_grade(marks):
    if marks >= 90 and marks <= 100:
        return "OUTSTANDING"
    elif marks >= 75:
        return "EXCELLENT"
    elif marks >= 60:
        return "GOOD"
    elif marks >= 40:
        return "NEED IMPROVEMENT"
    else:
        return "Fail"

try:
    name = input("Enter student name: ")
    marks = int(input("Enter marks "))

    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100")
    else:
        grade = get_grade(marks)
        print("Name:", name)
        print("Grade:", grade)

        with open("result.txt", "w") as f:
            f.write("Name: " + name + "\n")
            f.write("Marks: " + str(marks) + "\n")
            f.write("Grade: " + grade + "\n")

except ValueError:
    print("Invalid input.")
