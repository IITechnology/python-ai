with open("notes.txt","w") as f:
        f.write("HELLO PYTHON")

with open("notes.txt", "r") as f :
        print(f.read())