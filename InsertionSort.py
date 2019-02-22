# A program to implement Insertion Sort
n = int(input("Enter number of elements: "))
num = []
for i in range(0, n):
    num.append(int(input("Enter number: ")))

for i in range(0, n):
    for j in range(1, n):
        if num[i] > num[j]:
            for k in range(0, j):
                if num[k] > num[j]:
                    num[k], num[j] = num[j], num[k]
                elif num[k] < num[j]:
                    pass
        elif num[i] < num[j]:
            pass
print("The sorted array is here: ")
print(num)
