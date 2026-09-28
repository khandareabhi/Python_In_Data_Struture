
a=[
    [0,2,0,0],
    [0,0,5,0],
    [0,4,0,0],
    [0,0,6,0]
]

zero=0
non_zero=0

for i in range(4):
    for j in range(4):
        if(a[i][j]==0):
            zero+=1
        else:
            non_zero+=1




if(zero>non_zero):
    print("sparse is matrix")
else:
    print("Spase is not matrix ")
