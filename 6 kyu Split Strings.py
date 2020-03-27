def solution(s):
    tab = []
    
    if len(s) % 2 == 0:
        for i in range(0, len(s), 2):
                tab.append(s[i] + s[i+1])
    else:
        if len(s) % 2 == 1:
            for i in range(0, len(s)-1, 2):
                tab.append(s[i] + s[i+1])
            tab.append(s[len(s) - 1])
            tab[len(tab) - 1] += '_'
    return tab


print(solution("asdfadsf"))
print(solution("asdfads"))
print(solution(""))
print(solution("x"))



'''
("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"])
'''