def count_words(filename):
        try:
             with open(filename, "r") as f:
                      text=f.read()
                      count=text.split()
                      print("Word count:", len(count))
        except FileNotFoundError:
            print("File not found!")
filename = input("Enter file name: ")
count_words(filename)