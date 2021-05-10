from FechaHora import claseFechaHora
from Hora import claseHora
if __name__ == '__main__':
     d = int(input('Ingrese Dia: '))
     mes = int(input('Ingrese Mes: '))
     a = int(input('Ingrese Año: '))
     h = int(input('Ingrese Hora: '))
     m = int(input('Ingrese Minutos: '))
     s = int(input('Ingrese Segundos: '))
     f = claseFechaHora(d, mes, a, h, m, s)
     f.Mostrar()
     input()
     h1 = int(input('Ingrese Hora: '))
     m1 = int(input('Ingrese Minutos: '))
     s1 = int(input('Ingrese Segundos: '))
     r = claseHora(h1, m1, s1)
     r.Mostrar()
     input()
     f2 = f + r
     f2.Mostrar()
     input()
     f3 = r + f
     f3.Mostrar()
     input()
     f4 = f3 - 1
     f4.Mostrar()
     input()
     f4 = 1 + f2
     f4.Mostrar()
     input()