matrix = [
    [0, 0, 5],
    [0, 0, 0],
    [8, 0, 0]
]

zero = 0
nonzero = 0

for i in range(3):
    for j in range(3):
        if matrix[i][j] == 0:
            zero += 1
        else:
            nonzero += 1

print("Matrix:")
for row in matrix:
    print(row)

if zero > nonzero:
    print("It is a Sparse Matrix")
else:
    print("It is not a Sparse Matrix")

print("Zero elements:", zero)
print("Non-zero elements:", nonzero)