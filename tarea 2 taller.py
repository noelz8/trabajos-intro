hexa = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
    16: "G"
}

class Base(object):
    def __init__(self):
        pass
    def suma_base(self,num1, num2, acarreo, base):
        if isinstance (num1,list) and (num2,list) and (acarreo,int) and (base,int) and (num1+num2==base) and (len(num1) == len(num2)) num1 and num2 !=base:
            return self.base_aux(num1,num2,0)
        else:
            return "error"
        def base_aux(self,num1,num2,acarreo, base):
            if [num1+num2]==[]:
                return (acarreo)
            elif (num1[-1]+num2[-1]+acarreo)==base:
                return base_aux(num1[:-1]+num2[:-1],1)+[0]
            elif (num1[1]+num2[-1]+acarreo)<base:
                return base_aux(num1[:-1]+num2[:-1] +0)
            elif (num1+num2+acarreo)>base:
                return (((num1[:-1]+num2[:-1])-base)+1)
            else:
                return base_aux(num1[-1]+num2[-1]+acarreo)
        
