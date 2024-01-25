def cal(seq, ctrl, mark):
    sum = 0
    # 양수 혹은 음수만 있는경우 out of range 방지(양수: 0을 추가 / 음수: 1을 추가)
    if ctrl:
        seq.append(0)
    else:
        seq.append(1)

    for i in range(0,len(seq)-1,2):
        # 양수: 1보다 작으면 break / 음수: 0보다 크면 break
        if mark*seq[i] < ctrl:
            break
        # 양수: 다음 수가 1보다 작으면 1개만 계산 / 음수: 다음 수가 0보다 크면 1개만 계산
        elif mark*seq[i+1] < ctrl:
            sum += seq[i]
            break
        # 양수: 지금 수 or 다음 수가 1이면 각각 더해서 sum에 추가
        elif mark==1 and (seq[i]==ctrl or seq[i+1]==ctrl):
            sum += (seq[i] + seq[i+1])
        # 지금 수, 다음 수를 곱해서 sum에 추가
        else:
            sum += (seq[i] * seq[i+1])
    seq.pop() # 아까 append 한거 삭제
    return sum

# 입력
n = int(input())
seq = [0]*n
for i in range(n):
    seq[i] = int(input())

seq.sort(reverse=True) # 내림차순
pos = cal(seq,1,1) # 큰 수부터 1까지 연산
seq.sort() # 오름차순
neg = cal(seq,0,-1) # 작은 수부터 0까지 연산
print(pos + neg) # 각 연산 합 출력