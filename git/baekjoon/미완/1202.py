n, k = map(int, input().split())
gem = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]

gem.sort()
bag.sort(reverse=True)