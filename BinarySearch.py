# A program to implement Binary Search
n = int(input("Enter number of elements in array: "))
num = []

# Below is the loop for accepting input into list
for i in range(0, n):
    num.append(int(input("Enter number: ")))

# First we will sort the list in ascending order
for j in range(0, n):
    for k in range(j+1, n):
        if num[j] > num[k]:
            num[j], num[k] = num[k], num[j]
        elif num[j] <= num[k]:
            pass

print("The sorted list is here:")
print(num)

# Now we will do Binary search
s = int(input("Enter the number you want to search: "))
start = 0
end = n-1
while True:
    mid = int((start+end)/2)
    if num[mid] == s:
        print(f"Search element is present at {mid}, as array count starts from 0")
        break
    elif s > num[mid]:
        start = mid + 1
    elif s < num[mid]:
        end = mid - 1
    else:
        print("Just relax")
