import math

def evaluate(self, string):
    first = {
    '*' : lambda x, y : x*y,
    '/' : lambda x, y : x/y
    
    }
    second = {
        '+' : lambda x, y : x+y,
        '-' : lambda x, y : x-y
    }


    string = string.split(' ')
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
    return string

def twoSign(string):
    i = 0
    while i < len(string):
        if (string[i] == '-' and string[i+1] == '+') or (string[i] == '+' and string[i+1] == '-'):
            string = string.replace(string[i] + string[i+1], '-')
            i = 0
        elif (string[i] == '-' and string[i+1] == '-') or (string[i] == '+' and string[i+1] == '+'):
            string = string.replace(string[i] + string[i+1], '+')
            i = 0
        i += 1
    i = 0
    '''
    while i < len(string):
        if (string[i] == '*' or string[i] == '/') and string[i+1] == '-' and math.isnan(string[i]):
            string = string.replace(float(string[i+1] + string[i+2]))
            i = 0
        i += 1
    '''
    return string
def formatage(string):
    symbols = ['*','/','-','+','(',')']
    tab = []
    temp = ''
    for i in range(len(string)):
        if string[i] in symbols:
            if temp:
                tab.append(temp)
                temp = ''
            temp += string[i]
            tab.append(temp)
            temp = ''
        else:
            temp += string[i]
        if i == len(string) - 1:
            if temp:
                tab.append(temp)
    return tab
def par(string):
    openpar = 0
    closepar = 0
    tab = []
    for i in range(len(string)):
        if string[i] == '(':
            openpar = i
        elif string[i] == ')':
            closepar = i
            break
    return string[openpar+1:closepar]
def ifminus(string):
    i = 0
    while i < len(string):
        if (string[i] == '/' or string[i] == '*') and string[i+1] == '-':
            if str(string[i+2])[0] == '-':
                string = string[:i+1] + [str(string[i+2])[1:]] + string[i+3:]
            else:
                string = string[:i+1] + ['-' + str(string[i+2])] + string[i+3:]
            i = 0
        i += 1
    return string
def calc(expression):
    if isinstance(expression, str):
        expression = list(expression.replace(' ',''))
    else:
        if len(expression) > 1:
            expression = evaluate()
        else:
            return expression

    return expression  
print(calc("-(-1)"))
print(calc("10- 2- -5"))

print(calc("3 -(-1)"))
print(calc("-7 * -(6 / 3)"))

print(calc("(((10)))"))


print(calc("(2 / (2 + 3.33) * 4) - -6")) #7.5009380863
print(calc("1 + 1"))
print(calc("8/16"))

print(calc("2 + -2"))
print(calc("3 * 5"))

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