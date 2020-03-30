def calc(expression):
    ###########################################
    def evaluate(string):
        first = {
        '*' : lambda x, y : x*y,
        '/' : lambda x, y : x/y
        
        }
        second = {
            '+' : lambda x, y : x+y,
            '-' : lambda x, y : x-y
        }

        i = 0
        while i < len(string):
            if string[i] in first:
                temp = first[string[i]](float(string[i-1]), float(string[i+1]))
                string = string[:i-1] + [str(temp)] + string[i+2:]
                i = 0
            i += 1

        i = 0
        while i < len(string):
            if string[i] in second:
                temp = second[string[i]](float(string[i-1]), float(string[i+1]))
                string = string[:i-1] + [str(temp)] + string[i+2:]
                i = 0
            i += 1
        print(string, 'ty')
        print(type(string), 'op')
        if len(string) == 1:
            return string[0]
        else:
            return ''.join(string)
    #################################################
    def spli(str):
        tab = []
        op = ['*','/','+','-']
        temp = ""
        print(str, 'yu')
        for i in range(len(str)):
            if str[i] in op:
                if temp != "":
                    tab.append(temp)
                    temp = ""
                    temp += str[i]
                    tab.append(temp)
                    temp = ""
                elif temp == "":
                    temp += str[i]
                    tab.append(temp)
                    temp = ""
            elif str[i] not in op:
                temp += str[i]
            if i == len(str) - 1:
                tab.append(temp)
        i = 0
        while i < len(tab):
            if i == 0 and tab[i] == '-':
                tab = tab[:i] + [float(tab[i] + tab[i+1])] + tab[i+2:]
                i = 0
            elif i == 0 and tab[i] == '+':
                tab = tab[:i] + [float(tab[i+1])] + tab[i+2:]
            elif (tab[i] == '*' or tab[i] == '/') and tab[i+1] == '-':
                tab = tab[:i+1] + [(float(tab[i+1] + tab[i+2]))] + tab[i+3:]
                i = 0
            i += 1
        return tab
    ##################################################
    expression = expression.replace(' ', '')
    def twosign(str):
        i = 0
        while i < len(str) - 1:
            if str[i] == '-' and str[i+1] == '-':
                str = str.replace(str[i] + str[i+1], '+')
                i = 0
            elif (str[i] == '+' and str[i+1] == '-') or (str[i] == '-' and str[i+1] == '+'):
                str = str.replace(str[i] + str[i+1], '-')
                i = 0
            i += 1
        return str
    def par (string):
        openPar = 0
        closePar = 0
        i = 0
        while i < len(string):
            if string[i] == '(':
                openPar = i
            elif  string[i] == ')':
                closePar = i
                break
            i += 1
        print(string[openPar+1:closePar], '2')
        print(spli(string[openPar+1:closePar]), 'spli')
        temp = evaluate(spli(string[openPar+1:closePar]))
        temp = str(temp)
        print(type(temp), 'temp', temp)
        string = string[0:openPar] + temp + string[closePar+1:] 
        return twosign(string)
    print(expression, 'oui')
    while '(' in expression:
        expression = par(expression)
    expression = evaluate(spli(twosign(expression)))
    print(expression, 'rep')
    return float(expression)
    
print(calc("-(-1)"))
"""
print(calc("3 -(-1)"))
print(calc("-7 * -(6 / 3)"))

print(calc("(((10)))"))

print(calc("10- 2- -5"))



print(calc("(2 / (2 + 3.33) * 4) - -6")) #7.5009380863
print(calc("1 + 1"))
print(calc("8/16"))

print(calc("2 + -2"))
print(calc("3 * 5"))
"""
"""
    ["1 + 1", 2],
    ["8/16", 0.5],
    ["3 -(-1)", 4],
    ["2 + -2", 0],
    ["10- 2- -5", 13],
    ["(((10)))", 10],
    ["3 * 5", 15],
    ["-7 * -(6 / 3)", 14]
"""