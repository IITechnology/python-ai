# largest of 3 number
A=int(input("ENTER FIRST NUMBER"))
B=int(input("ENTER SECOND NUMBER"))
C=int(input("ENTER THIRD NUMBER"))

if A>B & B>C:
    print(f"A IS THE LARGEST")
elif A<B & B>C:
    print(f"B IS THE LARGEST")
else:
    print(f"C IS THE LARGEST")