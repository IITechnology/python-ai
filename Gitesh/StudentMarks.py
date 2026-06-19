subjects=["Maths","Science","English","Hindi","Social Science"]
marks=[99,98,97,96,95]
print("Subjects:",subjects)
print("Marks:",marks)
# print(f"Subjects:{subjects[0]}, Marks obtained:{marks[0]}")
# print(f"Subjects:{subjects[1]}, Marks obtained:{marks[1]}")
# print(f"Subjects:{subjects[2]}, Marks obtained:{marks[2]}")
# print(f"Subjects:{subjects[3]}, Marks obtained:{marks[3]}")
# print(f"Subjects:{subjects[4]}, Marks obtained:{marks[4]}")

for i in range(len(subjects)):
    print(f"Subjects:{subjects[i]}, Marks obtained:{marks[i]}")


total=sum(marks)
print(f"Total marks obtained: {total}")
average=total/len(marks)
print(f"Average marks obtained: {average}")
#test