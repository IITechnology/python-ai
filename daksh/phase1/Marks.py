subjects =["Maths","Science","English","Hindi","Social Science"]
marks=[99,98,97,96,95]
print("Subjects:",subjects)
print("Marks:",marks)

for i in range (len(subjects)):
    {
    print(f"Subjects:{subjects[i]}, Marks obtained:{marks[i]}")
    }
    
   
total=sum(marks)
print(f"Total Marks={total}")
average=total/len(marks)
print(f"Average marks={average}")
