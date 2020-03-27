def solution(string,markers):
    #your code here
    str = string
    for i in range(len(str)):
        if str[i] in markers:
            if str[i+1] not in markers and (str[i+2] != "\\" and str[i+2] != "n" ):
                str = str[:i+1] + str[i+2:]
                i = 0
    return str

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
#gvgjgnfhjbftfunhgfnjdhdbkbthdbgfdbdfgbdfbdgvkuhk