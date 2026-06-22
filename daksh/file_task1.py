import datetime

current_time=datetime.datetime.now()
print(f"Current date and time: {current_time}")

a= float(input("Enter first number: "))
b= float(input("Enter second number: "))

print("1. Addition \n")
print("2. Subtraction \n")
print("3. Multiplication \n")
print("4. Division \n")

choice = input("Enter your choice (1-4): ")

if choice == '1':
    result = a+b
    operation = "+"
elif choice == '2':
    result = a-b
    operation = "-"
elif choice == '3':
    result = a*b
    operation = "*"
elif choice == '4':
    if b!= 0:
        result = a/b
        operation = "/"
    else:
        print("Division by zero is not allowed.")
        exit()
else:
    print("Invalid choice.")
    exit()

print("Result =", result)



with open("calculator_results.txt", "a") as file:
    file.write(
        f"{current_time} : {a} {operation} {b} = {result}\n"
    )

print("Result saved in calculator_results.txt")