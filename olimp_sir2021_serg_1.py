def count_over(arr, val, mi):
    count = 0
    for i in range(0, mi):
        if arr[i] >= val:
            count += 1
    return count


def count_less(arr, val, mi):
    count = 0
    for i in range(mi, len(arr)):
        if arr[i] <= val:
            count += 1
    return count


def del_over(arr, val, mi):
    i = 0
    while i < mi:
        if arr[i] >= val:
            del p[i:i + 1]
            mi -= 1
        else:
            i += 1
    pass


def del_less(arr, val, mi):
    i = mi
    while i < len(arr):
        if arr[i] <= val:
            del p[i:i + 1]
        else:
            i += 1
    pass


p = list(map(int, input().split()))
k = 1
while k < len(p):
    if p[k - 1] == p[k]:
        del p[k - 1:k]
    elif p[k - 1] > p[k]:
        if count_over(p, p[k], k - 1) > count_less(p, p[k - 1], k):
            del_less(p, p[k], k)
        else:
            del_over(p, p[k], k)
    else:
        k += 1
print(' '.join(list(map(str, p))))
