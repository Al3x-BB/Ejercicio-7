class claseHora:
    __h = 0
    __m = 0
    __s = 0
    __d = 0
    def __init__(self, h=0, m = 0, s = 0):
        if(h >= 0 and h<=24):
            if(m >= 0 and m <= 60):
                if(s >= 0 and s <= 60):
                    self.__h = h
                    self.__m = m
                    self.__s = s
                else: print('ERROR: segundos inválido')
            else: print('ERROR: minutos inválido')
        else: print('ERROR: hora inválida')
    def getHr(self):
        return self.__h
    def getMin(self):
        return self.__m
    def getSeg(self):
        return self.__s
    def Mostrar(self):
        cadena = """\
        +----------+
        | {:2}:{:2}:{:2} |
        +----------+\
        """
        print(cadena.format(self.__h, self.__m, self.__s))