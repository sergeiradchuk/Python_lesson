n = int(input())
k = int(input())
count = 0
while n > 0:
    os = n % k
    if os == 0:
        n = n // k
        count += 1
    else:
        n = n - os
        count = count + os
print(count)
