# Does this code work?

i = 1
arr = [-1,4,8,6,-345,2465,89]
while (i < len(arr)):
    print (i, end=" ")
    i += 1

# Does this code work?

arr = [1,2,3,4,5]
if arr.index(3) == 3:
    for i in arr:
        print (arr[i])
elif arr.index(4) == 3:
    for i in arr:
        print(arr[i])

# What is the type of this var?

arr = ["3", "4", "5"]
myvar = float(str(int(arr[1])))

# What is the output of this code?

arr = [10, -20, 30, -40, 50]
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = math.abs(arr[i])
    for j in range(len(arr)):
        if arr[i] > 0:
            arr[i] *= -1

print (arr)
