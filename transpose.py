m1=[[12,17,13,5],
    [23,7,67,54],
    [90,83,21,42]]
transpose=[]
for i in range(4):
    row=[]
    for j in range(3):
        row.append(m1[j][i])
    transpose.append(row)
print(transpose)