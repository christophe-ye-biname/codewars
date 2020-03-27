def triple_trouble(one, two, three):
    #your code here
    str = ""
    for i in range(len(one)):
        str = str + one[i] + two[i] + three[i]
        
    return str

print(triple_trouble("aaa","bbb","ccc"))