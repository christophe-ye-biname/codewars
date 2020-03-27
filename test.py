tab = [i for i in range(100)]

while len(tab) > 1:
    print(len(tab))
    tab.pop((248) % len(tab))
print(tab)