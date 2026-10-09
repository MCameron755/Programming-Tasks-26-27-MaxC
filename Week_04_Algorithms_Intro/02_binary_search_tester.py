"""
TASK: 02 Binary Search Tester

# Binary Search Tester
Generate a sorted list. Implement:
- iterative binary search
- recursive binary search
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random
import time

def i_binarysearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def r_binarysearch(arr, target):
    def helper(low, high):
        if low > high:
            return -1

        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return helper(mid + 1, high)
        else:
            return helper(low, mid - 1)
    return helper(0, len(arr) - 1)

def generatesortedlist(size):
    return sorted(random.sample(range(size * 10), size))

def bencmarksearch():
    listsize = 100000
    searchnum = 5000
    print(f"Generating sorted list of size {listsize}...")
    sortedlist = generatesortedlist(listsize)
    targets = [random.choice(sortedlist) if random.random() < 0.2 else random.randint(0, listsize * 10) for _ in range(searchnum)]
    print(f"Benchmarking {searchnum} searches...")
    starttime = time.perf_counter()
    for target in targets:
        i_binarysearch(sortedlist, target)
    i_duration = time.perf_counter() - starttime
    starttime = time.perf_counter()
    for target in targets:
        r_binarysearch(sortedlist, target)
    r_duration = time.perf_counter() - starttime
    print(f"Iterative binary search took {i_duration:.6f} seconds.")
    print(f"Recursive binary search took {r_duration:.6f} seconds.")



if __name__ == "__main__":
    bencmarksearch()