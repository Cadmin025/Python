for i in range(1,5):
    print(f"Enter marks for student#{i}#")
    total=0
    for j in range(1,4):
        marks= int(input(f"Enter marks for subject #{j}#"))
        total=total+marks
    average = marks/3
    print(f"Average marks of subject{i} is {average}")