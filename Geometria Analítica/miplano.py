from sympy import *
from mibibl import *
a=input('ingrese los vectores separados por coma: ')
a=a.replace(' ', '')
m=a.count(')')
vectores=miselem(a)
t=0
dimini=vectores[0].count(',')
for i in range(1,m):
    dimfin=vectores[i].count(',')
    if dimini!=dimfin:
        t=1
if t==1:
    print('has ingresado estos {} vectores: '.format(m))
    b=[]
    for i in range(0,m):
        b.append(mivect(vectores[i]))
        print(tuple(b[i]))
    print('no puedes operar vectores de diferentes dimensiones: ')
else:
    if dimini==2:
        print('Has ingresado estos {} vectores de dimension {}: '.format(m,dimini+1))
        b=[]
        for i in range(0,m):
            b.append(mivect(vectores[i]))
            print(tuple(b[i]))
        v1=mirest(b[0],b[1])
        v2=mirest(b[0],b[2])
        n=mipvec(v1,v2)
        d=miproi(n,b[0])
        x=Symbol('x')
        y=Symbol('y')
        z=Symbol('z')
        if n[0]==n[1]==n[2]==0:
            print('los tres vectores son colineales, por lo tanto no generan ningun plano.')
        else:
            print('Dos vectores contenidos en el plano son: ')
            print('v={}={}-{}'.format(tuple(v1),tuple(b[0]),tuple(b[1])))
            print('w={}={}-{}'.format(tuple(v2),tuple(b[0]),tuple(b[2])))
            print('Así, el vector normal a nuestro plano es:')
            print('n=v x w = {}x{}={}'.format(tuple(v1),tuple(v2),tuple(n)))
            print('Entonces la ecuacion de nuestro plano tiene la forma: {}=d'.format(1*n[0]*x+1*n[1]*y+1*n[2]*z))
            print('siendo d={}.{}={}'.format(tuple(n),tuple(b[0]),d))
            if n[0]<0:
                print('Luego, la ecuacion del plano que pasa por esos puntos es: ',end='')
                print(-1*n[0]*x-1*n[1]*y-1*n[2]*z,end='')
                print(' = {}'.format(-d))
            else: 
                print('Luego, la ecuacion del plano que pasa por esos puntos es: ',end='')
                print(n[0]*x+n[1]*y+n[2]*z,end='')
                print(' = {}'.format(d))
            decision=input('quieres comprobar si algún punto está en ese plano si/no?:')
            if 's' in decision:
                nv=input('ingresa el vector que quieres comprobar: ')
                novect=mivect(nv)
                dpla=abs(miproi(n,novect)-d)/minorm(n)
                if dpla==0:
                    print('el punto está en el plano.')
                else:
                    print('el punto no está en el plano, de hecho la distancia del punto al plano es: {}'.format(dpla))
    else:
        print('esto solo funciona para vectores com 3 componentes.')
