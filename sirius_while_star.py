## второй минимум
min1 = 10**9
min2 = 10**9
elem = int(input())
while elem != 0:
    if elem < min1:
        min2 = min1
        min1 = elem
    elif elem < min2:
        min2 = elem
    elem = int(input())
print(min2)
