n = int(input())
arr1 = [n]
arr2 = [n]
golden_ratio = (1 + 5**(0.5))/2

arr1.append(int(arr1[0]//golden_ratio))
arr2.append(int(arr2[0]//golden_ratio)+1)

while arr1[-2]>=arr1[-1]:
    arr1.append(arr1[-2]-arr1[-1])
while arr2[-2]>=arr2[-1]:
    arr2.append(arr2[-2]-arr2[-1])

if len(arr1) > len(arr2):
    print(len(arr1))
    print(*arr1)
else:
    print(len(arr2))
    print(*arr2)
