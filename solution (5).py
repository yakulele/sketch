n, m, k = map(int, input().split())
race = []
res = []
for num in range(1, n+1):
    race.append(num)


for time in range(m):
    i, j = map(int, input().split())
    race[i-1], race[j-1] = race[j-1], race[i-1]
    le = len(res)
    for num in range(len(race)):
        if abs(race[num] - (num+1)) > k:
            res.append(1)
            break
    if le == len(res):
        res.append(0)



for result in res:
    print(result)