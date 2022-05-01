num = int(input())
n = num
tmp1 = 2
tmp2 = num//2
d = 0
while tmp1 <= tmp2:
    if num % tmp1 == 0:
        d = tmp1
        num = num // tmp1
        tmp2 = tmp1 // 2
    tmp1 += 1
if num>d:
    print(num)
else:
    print(d)
