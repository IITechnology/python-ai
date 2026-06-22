with open("file_name.txt", "r") as f:
    for line in f:
        print(f"line {line.strip()}")
        print(f"line ended")