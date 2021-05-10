class claseFechaHora:
    __d = 0     #dia
    __m = 0     #mes
    __a = 0     #año
    __h = 0     #hora
    __mi = 0    #minutos
    __s = 0     #segundos
    def __init__(self, dia = 1, mes = 1, año = 2020, hora = 0, min = 0, seg = 0):
        if(dia>=1 and dia<=31):
            if(mes>=1 and mes<=12):
                if(año>=0):
                    if(hora>=0 and hora<=24):
                        if(min>=0 and min<=60):
                            if(seg>=0 and seg<=60):
                                self.__d = dia
                                self.__m = mes
                                self.__a = año
                                self.__h = hora
                                self.__mi = min
                                self.__s = seg
                            else: print('ERROR: segundos inválido')
                        else: print('ERROR: minutos inválido')
                    else: print('ERROR: hora inválido')
                else: print('ERROR: año inválido')
            else: print('ERROR: mes inválido')
        else: print('ERROR: día inválido')
    def PonerEnHora(self, h = 0, m = 0, s = 0):
        self.__h = h
        self.__mi = m
        self.__s = s
    def AdelantarHora(self, h = 0, m = 0, s = 0):
        self.__h += h
        self.__mi += m
        self.__s += s
    def actualizar(self, d, m, a, h, mi, s):
        band = False  # indica si es año bisiesto
        if (a % 100 == 0):  # verifica que el año sea bisiesto
            if (a % 400 == 0):
                band = True
        elif (a % 4 == 0):
            band = True
        if (s >= 60):
            mi += 1
            s -= 60
        if (mi >= 60):
            h += 1
            mi -= 60
        if (h >= 24):
            d += 1
            h -= 24
        if (band == True and m== 2 and d > 29):
            m += 1
            d -= 29
        elif (m == 2 and d >= 28):
            m += 1
            d -= 28
        if ((m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and d > 31):
            m += 1
            d -= 31
        if ((m == 4 or m == 6 or m == 9 or m == 11) and d > 30):
            m += 1
            d -= 30
        if (m > 12):
            a += 1
            m -= 12
        return claseFechaHora(d, m, a, h, mi, s)
    def Mostrar(self):
        cadena = """\
        +--------------------------+
        | {:2}/{:2}/{:4} ---- {:2}:{:2}:{:2} |
        +--------------------------+\
        """
        print(cadena.format(self.__d, self.__m, self.__a, self.__h, self.__mi, self.__s))
    def getHr(self):
        return self.__h
    def getMin(self):
        return self.__mi
    def getSeg(self):
        return self.__s
    def __add__(self, other):
        return self.actualizar(self.__d, self.__m, self.__a, self.__h + other.getHr(), self.__mi + other.getMin(),
                              self.__s + other.getSeg())
    def __radd__(self, other):
        obj = None
        if(type(other) == int):
            obj = self.actualizar(self.__d + other, self.__m, self.__a, self.__h, self.__mi, self.__s)
        else:
            obj = self.actualizar(self.__d, self.__m, self.__a, self.__h + other.getHr(), self.__mi + other.getMin(),
                                   self.__s + other.getSeg())
        return obj
    def __sub__(self, other):
        m = 0
        a = 0
        band = False  # indica si el año es bisiesto
        if (self.__a % 100 == 0):  # verifica que el año sea bisiesto
            if (self.__a % 400 == 0):
                band = True
        elif (self.__a % 4 == 0):
            band = True
        #resta
        a = self.__a
        m = self.__m
        d = self.__d - other
        if (d == 0):  # si los días son negativos, se pide un mes
            m -= 1
            if (m == 0):
                a -= 1
                m += 12
            # como en los meses hay diferentes cantidad de días según el mes
            if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
                d += 31  # se sumará 31 días
            if (m == 4 or m == 6 or m == 9 or m == 11):
                d += 30  # se sumará 30 días
            if (band == True):  # si el año es bisiesto
                if (m == 2):
                    d += 29  # se sumará 29 días
            else:  # si el año no es bisiesto
                if (m == 2):
                    d += 28  # se sumará 28 días
        return claseFechaHora(d, m, a, self.__h, self.__mi, self.__s)