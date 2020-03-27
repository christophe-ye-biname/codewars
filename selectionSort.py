import random

tab = [random.randint(0,101) for i in range(100)]
print(tab)

def selection(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

print(selection(tab))