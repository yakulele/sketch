numbers = input()
nums = numbers.split()
res = []

def is16(num):
    for char in num:
        if not char.isdigit() and (not char.isalpha() or char.islower()):
            return False
    try:
        int(num, 16)
        return True
    except ValueError:
        return False

for num in nums:
    if num.startswith('0x'):
        if is16(num[2:]):
            res.append(num)
    elif is16(num):
        re = '0x' + str(num)
        res.append(re)

print(*res)