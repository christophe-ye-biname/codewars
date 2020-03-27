def find_all(array, n):
    # your code here
    tab = []
    for i in range(len(array)):
        if array[i] == n:
            tab.append(i)
    return tab