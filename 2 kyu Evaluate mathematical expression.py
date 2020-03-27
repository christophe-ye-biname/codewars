class Calculator(object):
    def evaluate(self, string):
        def calc(str):
            str = str.split(" ")
            while len(str) > 1:
                for i in range(len(str)):
                    if str[i] == "/":
                        str = divi(str, i)
                        i = 0
                    elif str[i] == "*":
                        str = mult(str, i)
                        i = 0
                for i in range(len(str)):
                    if str[i] == "+":
                        str = add(str, i)
                        i = 0
                    elif str[i] == "-":
                        str = sous(str, i)
                        i = 0
            return str
        def mult(arr, i):
            mult = []
            inter = float(arr[i-1]) * float(arr[i+1])
            for j in range(len(arr)):
                if j < i-1:
                    mult.append(arr[j])
                elif j == i:
                    mult.append(inter)
                elif j > i+1:
                    mult.append(arr[j]);
            return mult
        return calc(string)
        def div(arr, i):
            div = []
            inter = float(arr[i-1]) * float(arr[i+1])
            for j in range(len(arr)):
                if j < i-1:
                    div.append(arr[j])
                elif j == i:
                    div.append(inter)
                elif j > i+1:
                    div.append(arr[j]);
            return div
        def add(arr, i):
            add = []
            inter = float(arr[i-1]) * float(arr[i+1])
            for j in range(len(arr)):
                if j < i-1:
                    arr.append(arr[j])
                elif j == i:
                    arr.append(inter)
                elif j > i+1:
                    arr.append(arr[j]);
            return arr
        def sous(arr, i):
            sous = []
            inter = float(arr[i-1]) * float(arr[i+1])
            for j in range(len(arr)):
                if j < i-1:
                    sous.append(arr[j])
                elif j == i:
                    sous.append(inter)
                elif j > i+1:
                    sous.append(arr[j]);
            return sous
print (Calculator)
#oiiiiiiyuhnon,,ki,p,k,p,,o,o,o,,,,o,,,,,,,,oooooooontyuftufyufuyftdtydyftyfftyfyfiiygh i jay kay èlle èmm hygvbkgjijojioujponuionijjpojopmohbftyvtycytcvtgvfrcdexxdetrfcvyvvmoijmomkommlihlihdvdxvyvyvyycvyvgrtyuiopmlkijytktuhygtfrdeszqrfcxderfcxderfcxdeiunvkfvj;fv;gk;gk;hubbhbhbbhuuj,juhbhuj,,kol:lok,juhbgtrdxszq<vbgkhplplpgvbkgfyvgyugguyvjbjyytvgjyccccccnuhninuinyugyugvyuinichgcvfghjgjgcnjjingvyugyguigkiujbhyuhihijjnhbhbininjninnhnnnjhinjnjijinnjinjinjnninjnjinnjnjnjjnccrrfhgjtttytyrterazdfgyuhbkblohohhjgjfhfvfjkgkugkuènnuinihhhhhhhhhhhhhhh