m = int(input())
n = int(input())
places = []


for _ in range(n):
    i, p, d = input().split(';')
    i = int(i)
    p = int(p)
    places.append((i, p, d))


dp = [0] * (m + 1)
used = [[] for _ in range(m + 1)]


for i, p, d in places:
    for current_money in range(m, p - 1, -50):
        if dp[current_money - p] + i > dp[current_money]:
            dp[current_money] = dp[current_money - p] + i
            used[current_money] = used[current_money - p] + [d]


print(';'.join(used[m]))