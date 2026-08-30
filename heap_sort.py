import random
import time

lis_random = random.sample(range(0, 20_000), 20_000)
lis_normal = [i for i in range(0, 10)]

on = time.perf_counter()

def heapp(lis, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and lis[left] > lis[largest]:
        largest = left
    if right < n and lis[right] > lis[largest]:
        largest = right
    if largest != i:
        lis[i], lis[largest] = lis[largest], lis[i]
        heapp(lis, n, largest)

def heap_sort(lis):
    n = len(lis)
    for i in range(n // 2 - 1, -1, -1):
        heapp(lis, n, i)
    for i in range(n - 1, 0, -1):
        lis[i], lis[0] = lis[0], lis[i]
        heapp(lis, i, 0)
    return lis


print(heap_sort(lis_random))
tw = time.perf_counter()
print(f'Время выполнения: {tw - on}')