# with open("file_name.txt", "w") as f:
#     f.write("hello world \n")
#     f.write("learning python \n")
# print(f"file created successfully")

#  reading file

# with open("file_name.txt", "r") as f:
#     filecontent=f.read()
#     print(f"filecontent:{filecontent}")
    
# update a file

# with open("file_name.txt", "a") as f:
#     f.write("this is new content \n")
    
# reading line by line

with open("file_name.txt", "r") as f:
    for line in f:
        print(f"line {line.strip()}")
        print(f"line ended")
        
        
#  create a calculator and the result must be stored in the file and must be next line and must print the date and time.