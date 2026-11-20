matrix = [
    [0, 0, 5],
    [0, 0, 0],
    [8, 0, 0],
    [4, 0, 9]
]

zero = 0
nonzero = 0

for i in range(4):
    for j in range(4):
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
print("Non-zero elements:", nonzero) # all about the matrix and that sparse

# this is all the matrix is sparse matrix or not and also count the zero and non-zero elements in the matrix.
# same matrix is used in the above code and also the same output is given.
# time complexity is O(n^2) and space complexity is O(1)
# all about the sparse matrix and also the same output is given in the above code.