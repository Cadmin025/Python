marks=int(input( "Enter percentage marks scored   "))
if marks>100 or marks<0:
   print("Error !!! Entor a valid mark 0-100%")
elif marks>=70:
    print("Grade is A")
elif marks>=60:
    print("Grade is B")
elif  marks>=50:
    print("Grade is C")
elif marks>=40:
    print("Grade is D")
elif marks>=30:
    print("Grade is E")
elif marks>=20:
    print("Grade is F")
elif marks>=10:
    print("Grade is U")

 if marks>=70 and marks<=100:
    print("Grade is A")