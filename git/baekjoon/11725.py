n = int(input())
point_1 = [0]*(n-1)
point_2 = [0]*(n-1)

for i in range(n-1):
    point_1[i], point_2[i] = map(int, input().split())

def tree_sort(point_1, point_2, parent=1, sort_point = []):
    for i in range(point_1.count(parent)):
        index = point_1.index(parent)
        sort_point.append([point_2[index], point_1[index]])
        child = point_2[index]
        point_1.pop(index)
        point_2.pop(index)
        tree_sort(point_1, point_2, child, sort_point)

    for i in range(point_2.count(parent)):
        index = point_2.index(parent)
        sort_point.append([point_1[index], point_2[index]])
        child = point_1[index]
        point_1.pop(index)
        point_2.pop(index)
        tree_sort(point_1, point_2, child, sort_point)

    return sort_point

sort_points = tree_sort(point_1, point_2)
sort_points.sort()
for i in sort_points:
    print(i[1])