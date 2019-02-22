# Program to implement Linear Search and also checks if search element is present multiple times
num = []
n = int(input("How many numbers you want to input: "))
for i in range(0, n):
    num.append(int(input("Enter number: ")))
s = int(input("Enter the element that you want to search: "))
start = 0
end = n-1
flag = 0
while start <= end:
    if num[start] == s:
        print(f"Search element found at {start}, as array starts at position 0")
        start += 1
        flag += 1
    else:
        start += 1

if start > end and flag == 0:
    print("Search element not present in the array")
