"""
TASK: 03 Insertion Sort

# Insertion Sort Tester
Generate an unsorted list (maybe use RNG). Implement:
- Insertion sort without using inbuild sorts
- Count number of comparions
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random
import time

def generateunsortedlist(size, minval = 1, maxval = 10000):
    return [random.randint(minval, maxval) for _ in range(size)]

def insertionsort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, comparisons

def benchmarkinsertionsort():
    sizes = [100, 500, 1000, 2000, 5000]
    print(f"{'Size':<12}{'Time (s)':<25}{'Comparisons':<15}")
    print("-" * 58)
    for size in sizes:
        data = generateunsortedlist(size)
        starttime = time.perf_counter()
        sorteddata, comparisons = insertionsort(data)
        endtime = time.perf_counter()
        executiontime = endtime - starttime
        print(f"{size:<12}{executiontime:<25.6f}{comparisons:<15}")

if __name__ == "__main__":
    benchmarkinsertionsort()