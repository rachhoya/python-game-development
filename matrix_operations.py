x=[[12,23,17],
   [68,90,23],
   [83,35,13]]

y=[[56,67,15],
   [32,42,75],
   [82,46,31]]

add=[[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(3):
    for j in range(3):
        add[i][j]=x[i][j]+y[i][j]
print(add)

product=[[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(3):
    for j in range(3):
        product[i][j]=x[i][j]*y[i][j]
print(product)

subtract=[[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(3):
    for j in range(3):
        subtract[i][j]=x[i][j]-y[i][j]
print(subtract)