def mifrac(a):
    fraction=list(a)
    c,t,num,den=0,0,0,0
    if '/' in fraction:
        for i in fraction:
            if i!='/':
                c+=1
            else: break
        for i in range(0,c):
            if fraction[i]=='-':
                t=1
                continue
            else:
                num+=int(fraction[i])*10**(c-1-i)
        for i in range (c+1, len(fraction)):
            den+=int(fraction[i])*10**(len(fraction)-i-1)
        if t==1:
            f1=Rational(-1*num, den)
        else:
            f1=Rational(num, den)

    elif '.' in fraction:
        for i in fraction:
            if i!='.':
                c+=1
            else: break
        for i in range(0,c):
            if fraction[i]=='-':
                t=1
                continue
            else:
                num+=int(fraction[i])*10**(c-1-i)
        for i in range (c+1, len(fraction)):
            den+=int(fraction[i])*10**(len(fraction)-i-1)
        if t==1:
            f1=-1*num-Rational(den, 10**(len(fraction)-c-1))
        else:
            f1=num+Rational(den, 10**(len(fraction)-c-1))
    else:
        c=len(fraction)
        f1=0
        for i in range(0,c):
            if fraction[i]=='-':
                t=1
                continue
            else:
                f1+=int(fraction[i])*10**(c-1-i)
        if t==1:
            f1=-1*f1
    return f1

def mivect(a):
    a=list(a)
    v,w=[],[]
    cf,ci,k=0,1,0
    cad=''
    for i in range(1, len(a)):
        if a[i]!=',' and a[i]!=')':
            cf+=1
        else:
            for j in range(ci, ci+cf):
                cad+=a[j]
            v.append(cad)
            #print(v[k])
            k+=1
            ci=ci+cf+1
            cf=0
            cad=''
    for i in range(0,k):
        w.append(mifrac(v[i]))
    return w

def miselem(a):
    a=list(a)
    v,w=[],[]
    cf,ci,k=0,0,0
    cad=''
    for i in range(0, len(a)):
        if a[i]!=')':
            cf+=1
        else:
            for j in range(ci, ci+cf+1):
                cad+=a[j]
            v.append(cad)
            k+=1
            ci=ci+cf+1
            cf=0
            i+=1
        cad=''
    for i in range(0,k):
        if i==0:
            w.append(str(v[0]))
        else:
            w.append(str(v[i][1::]))  
    return w

def misuma(v,w):
    u=[]
    for i in range(0,len(v)):
        u.append(v[i]+w[i])
    return u

def mirest(v,w):
    u=[]
    for i in range(0,len(v)):
        u.append(v[i]-w[i])
    return u

def miproi(v,w):
    pi=0
    for i in range(0,len(v)):
        pi+=v[i]*w[i]
    return pi

def mipvec(v,w):
    u=[]
    u.append(v[1]*w[2]-v[2]*w[1])
    u.append(v[2]*w[0]-v[0]*w[2])
    u.append(v[0]*w[1]-w[0]*v[1])
    return u

def minorm(v):
    norm=sqrt(miproi(v,v))
    return norm

def miunit(v):
    w=[]
    for i in range(0, len(v)):
        w.append(v[i]/minorm(v))
    return w

def miproy(v,w):
    u1=[]
    num=miproi(v,w)
    den=miproi(w,w)
    coe=Rational(num, den)
    for i in range(0,len(v)):
        u1.append(coe*w[i])
    return u1

def migsch(v):
    t=[]
    for i in range(0,len(v)):
        if i==0:
            t.append(v[i])
        else:
            k=[]
            for j in range(0, i):
                if j==0:
                    k.append(v[i])
                k.append(mirest(k[j],miproy(v[i],t[j])))
                if j==i-1:
                    t.append(k[i])
    return t
from sympy import *
from pylatex import *
