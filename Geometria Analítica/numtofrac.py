from sympy import *
fraction1, fraction2=[],[]
ctrden1=0
ctrsinal1=1
ctrsinal2=1
while(ctrden1==0):
    a=input('Ingrese o primeiro número: ')
    fraction1=list(a)
    if '-' in fraction1:
        fraction1.remove('-')
        ctrsinal1=-1
    if '/' not in fraction1 and '.' not in fraction1:
        f1=0
        for i in range(0,len(fraction1)):
            f1+=int(fraction1[i])*10**(len(fraction1)-1-i)
        ctrden1=1
        if ctrsinal1==-1:
            f1=-1*f1  
    elif '/' in fraction1:
        c=0
        for i in fraction1:
            if i!='/':
                c+=1
            else: break
        num1=0
        for i in range(0,c):
            num1+=int(fraction1[i])*10**(c-1-i)
        den1=0
        for i in range(c+1, len(fraction1)):
            den1+=int(fraction1[i])*10**(len(fraction1)-i-1)
        if den1==0:
            print('Fração inválida. Não é possível dividir por zero')
            print('Vamos tentar mais uma vez')
            ctrsinal1=1
        else: 
            ctrden1=1 
            f1=Rational(num1, den1)
            if ctrsinal1==-1:
                f1=-1*f1
    elif '.' in fraction1:
        ctrden1=1
        c=0
        for i in fraction1:
            if i!='.':
                c+=1
            else: break
        num1=0
        for i in range(0,c):
            num1+=int(fraction1[i])*10**(c-1-i)
        den1=0
        for i in range (c+1, len(fraction1)):
            den1+=int(fraction1[i])*10**(len(fraction1)-i-1)
        f1=num1+Rational(den1, 10**(len(fraction1)-c-1))
        if ctrsinal1==-1:
            f1=-1*f1

ctrden2=0
while(ctrden2==0):
    b=input('Ingrese o segundo número: ')
    fraction2=list(b)
    if '-' in fraction2:
        fraction2.remove('-')
        ctrsinal2=-1
    if '/' not in fraction2 and '.' not in fraction2:
        f2=0
        for i in range(0,len(fraction2)):
            f2+=int(fraction2[i])*10**(len(fraction2)-1-i)
        ctrden2=1
        if ctrsinal2==-1:
            f2=-1*f2
    elif '/' in fraction2:
        c=0
        for i in fraction2:
            if i!='/':
                c+=1
            else: break
        num2=0
        for i in range(0,c):
            num2+=int(fraction2[i])*10**(c-1-i)
        den2=0
        for i in range(c+1, len(fraction2)):
            den2+=int(fraction2[i])*10**(len(fraction2)-i-1)
        if den2==0:
            print('Fração inválida. Não é possível dividir por zero')
            print('Vamos tentar mais uma vez')
            ctrsinal2=1
        else: 
            ctrden2=1 
            f2=Rational(num2, den2)
            if ctrsinal2==-1:
                f2=-1*f2
    elif '.' in fraction2:
        ctrden2=1
        c=0
        for i in fraction2:
            if i!='.':
                c+=1
            else: break
        num2=0
        for i in range(0,c):
            num2+=int(fraction2[i])*10**(c-1-i)
        den2=0
        for i in range (c+1, len(fraction2)):
            den2+=int(fraction2[i])*10**(len(fraction2)-i-1)
        f2=num2+Rational(den2, 10**(len(fraction2)-c-1))
        if ctrsinal2==-1:
            f2=-1*f2
print('os números dados são')
print(f1)
print(f2)
print('A soma é {}, a diferença é {} e o produto é {}'.format(f1+f2,f1-f2,f1*f2))