class Base(object):
    def __init__(self):
        pass
    def suma_base(self,num1, num2, base):
        if isinstance (num1,list) and (num2,list) and (acarreo,int) and (base,int) and (num1+num2==base) and (len(num1) == len(num2)) num1 and num2 !=base:
            return self.base_aux(num1,num2,base,0)
        else:
            return "error"
        def base_aux(self,num1,num2,base,acarreo):
            if [num1+num2]==[]:
                return acarreo
            elif (num1[0:]+num2[0:]):
                return base_aux(num1[:-1]+num2[:-1],base,acarreo+num1[-1:]+num2[-1:])
            elif (num1[1]+num2[-1],acarreo)<base:
                return base_aux(num1[:-1]+num2[:-1],base,acarreo+num1[-1:]+num2[-1:])
            elif (num1+num2+acarreo)>base:
                return base_aux(num1[:-1]+num2[:-1],base,acarreo+num1[-1:]+num2[-1:])
            else:
                return base_aux(num1[:-1]+num2[:-1],base,acarreo+num1[-1:]+num2[-1:])
