import random
import time

lis_random = random.sample(range(0, 20_000), 20_000)
lis_normal = [i for i in range(0, 10)]

on = time.perf_counter()
  
def merge_sort(lis):
    if len(lis) <= 1:
        return lis
    mid = len(lis) // 2
    left = merge_sort(lis[:mid])
    right = merge_sort(lis[mid:])
    return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res



merge_sort(lis_random)
tw = time.perf_counter()
print(f'Время выполнения: {tw - on}')