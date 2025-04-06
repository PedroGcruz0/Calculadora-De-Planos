from sympy import *
from bib import *
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
        b.append(meuvetor(vectores[i]))
        print(tuple(b[i]))
    print('no puedes operar vectores de diferentes dimensiones: ')


else:
    print('has ingresado estos {} vectores de dimension {}: '.format(m,dimini+1))
    b=[]
    for i in range(0,m):
        b.append(meuvetor(vectores[i]))
        print(tuple(b[i]))


    c=migsch(b)
    print('los vectores obtenidos por el proceso de Grand-Schmidt son:')
    for i in range(0, m):
        if minorm(c[i])!=0:
            print(tuple(miunit(c[i])))
        if minorm(c[i])==0:
            print(tuple(c[i]))