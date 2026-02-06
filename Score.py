Score={}
S1=int(input("Enter your marks for the first subject"))
S2=int(input("Enter your marks for the second subject"))
S3=int(input("Enter your marks for the thirdsubject"))
S4=int(input("Enter your marks for the fifth subject"))
S5=int(input("Enter your marks for the sixth subject"))
Score["Subject 1"]=S1
Score["Subject 2"]=S2
Score["Subject 3"]=S3
Score["Subject 4"]=S4
Score["Subject 5"]=S5
print(Score)
Total=0
for i in Score:
    Total=Total+Score[i]
print(Total)