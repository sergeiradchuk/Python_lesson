n = int(input())
arr = list()
for i in range(n):
    arr.append(int(input()))

m = min(arr)
sum_time = m * (len(arr) - 1)
print(sum_time)
