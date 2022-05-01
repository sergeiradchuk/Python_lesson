n = int(input())
i = 2
while n % i != 0 and i * i <= n:
    i += 1
if i * i < n:
    print(i)
else:
    print(n)
