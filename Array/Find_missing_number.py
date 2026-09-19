arr =[1,2,3,5,6]
n=6

expected_sum=n*(n+1)//2

actual_sum=0

for num in arr:
    actual_sum+=num


missing_number= expected_sum-actual_sum

print("Missing number in this : ",missing_number)