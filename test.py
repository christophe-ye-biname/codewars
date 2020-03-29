def spli(str):
    tab = []
    op = ['*','/','+','-']
    temp = ""
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
        if (tab[i] == '*' or tab[i] == '/') and tab[i+1] == '-':
            tab = tab[:i+1] + [(float(tab[i+1] + tab[i+2]))] + tab[i+3:]
            i = 0
        i += 1
    return tab

stri = '64.54-648*-4648684/48646-468455*48545'

print(spli(stri))
op = ['*','/','+','-']
#print('*' in op,'/' in op,'+' in op,'-' in op)


'''
while i < len(tab):
          if tab[i] == '-':
            tab = tab[:i-1] + [float('-' + tab[i+1])] + tab[i+2:]
            i = 0
          i += 1
'''