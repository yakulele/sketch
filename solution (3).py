def find_max_l(s):
    max_l = 0
    le = len(s)
    for i in range(le):
        for j in range(i+1, le):
            if s[i] == s[j]:
                c_le = j-i+1
                max_l = (max_l, c_le)
    if max_l == 0:
        return [1]
    return max_l

print(find_max_l(input())[-1])