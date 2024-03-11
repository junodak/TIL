N = int(input())
A = list(map(int, input("").split()))
B, C = map(int, input().split())
supervision = 0

for i in range(N):
    A[i] -= B
    supervision += 1
    if A[i]>0:
        supervision = supervision + A[i]//C
        if A[i]%C !=0:
            supervision += 1

print(supervision)
