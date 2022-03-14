import random
arr = [random.randint(0, 100) for i in range(0, 10)]
def bubble_sort(arr) -> list:
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr
                
for i in bubble_sort(arr):
    print(i)