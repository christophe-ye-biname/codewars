class Calculator(object):
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
        return float(''.join(string))

res = Calculator()


print(res.evaluate("2 / 2 + 3 * 4 - 6")) #7
