from collections import defaultdict

# 정점의 개수 입력
n = int(input())

# 입력된 간선의 양 끝점을 저장할 리스트 초기화
edges = defaultdict(list)

# 간선 정보 입력
for i in range(n-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

# 스택을 활용한 깊이 우선 탐색을 통해 부모를 저장
parents = [0] * (n+1)
stack = [1]

while stack:
    node = stack.pop()
    for child in edges[node]:
        if parents[child] == 0:
            parents[child] = node
            stack.append(child)

# 각 노드의 부모 출력
for node in range(2, n+1):
    print(parents[node])


'''
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)  # 재귀 제한을 풀어줌

# 정점의 개수 입력
n = int(input())

# 입력된 간선의 양 끝점을 저장할 리스트 초기화
edges = defaultdict(list)

# 간선 정보 입력
for i in range(n-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

# 깊이 우선 탐색을 통해 부모를 저장
parents = [0] * (n+1)

def dfs(node, parent):
    parents[node] = parent
    for child in edges[node]:
        if child != parent:
            dfs(child, node)

# 1을 루트로 하는 트리를 순회하여 부모 저장
dfs(1, 0)

# 각 노드의 부모 출력
for node in range(2, n+1):
    print(parents[node])
'''

'''
# 정점의 개수 입력
n = int(input())

# 입력된 간선의 양 끝점을 저장할 리스트 초기화
point_1 = [0]*(n-1)
point_2 = [0]*(n-1)

# 간선 정보 입력
for i in range(n-1):
    point_1[i], point_2[i] = map(int, input().split())

# 부모와 자식을 구분하여 정렬한 결과를 반환하는 함수
def tree_sort(point_1, point_2, parent=1, sorted_point = []):
    # parent와 연결된 자식들을 찾아 정렬 리스트에 추가하고 재귀 호출
    # 자식은 또 다른 자식을 낳기때문.
    for i in range(point_1.count(parent)):
        index = point_1.index(parent)
        sorted_point.append([point_2[index], point_1[index]]) # 부모-자식 간선 추가
        child = point_2[index]
        point_1.pop(index)
        point_2.pop(index)
        tree_sort(point_1, point_2, child, sorted_point)

    for i in range(point_2.count(parent)):
        index = point_2.index(parent)
        sorted_point.append([point_1[index], point_2[index]])
        child = point_1[index]
        point_1.pop(index)
        point_2.pop(index)
        tree_sort(point_1, point_2, child, sorted_point)

    return sorted_point

# 부모와 자식을 정렬한 결과를 얻음
sort_points = tree_sort(point_1, point_2)

# 각 간선별로 차례로 부모를 출력하기 위한 정렬
sort_points.sort()
for i in sort_points:
    print(i[1])
'''