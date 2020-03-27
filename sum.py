import random

lol = ['oio45df', '45', '45.85']

def sum(arr):
    if len(arr) == 0:
        return 0
    elif arr[0].isnumeric():
        return int(arr[0]) + sum(arr[1:])
    else:
        return sum(arr[1:])

print(sum(lol))
print('45.45'.isdecimal())

random_float = random.uniform(1.0, 3.0)

print(random_float)
print(str(random_float))

tab = [random.uniform(1.0, 3.0) for i in range(10)]
print(tab)
tab2 = [str(tab[i]) for i in range(len(tab))]
print(sum(tab2))