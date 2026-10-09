"""
TASK: 01 Bubble Sort

# Bubble Sort
Implement Bubble Sort on any size list:
- Do not use built-in sort()
- Count swaps
- Extend by

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def bubblesort(arr):
    n = len(arr)
    swapcount = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapcount += 1
    return arr, swapcount

if __name__ == "__main__":
    testlist = [56, 23, 83, 26, 11, 94, 35]
    print("Original list:", testlist)
    sortedlist, totalswaps = bubblesort(testlist)
    print("Sorted list:", sortedlist)
    print("Total swaps:", totalswaps)