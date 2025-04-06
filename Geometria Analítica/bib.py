#Este código transforma cadeias da forma a/b em frações que podem ser operadas
#Lembre que as cadeias '3/2'+'3/2'='3/23/2' por serem cadeias
#Os números 3/2 + 3/2 = 3.
from sympy import *
from pylatex import *
def numtofrac(a):
    ctrden=False#Essa variável controla os casos a/0 pedindo que o usuário insira novamente o denominador
    ctrsinal=1#Essa variável controla os casos de cadeias da forma -a/b para não considerar o sinal como um carater
    while(not ctrden):#Este control pedira para você inserir a/b desde que b=0
        fraction=list(a)
        if '/' not in fraction and '.' not in fraction: #Neste if, se a cadeia é simplesmente um número transformamos a cadeia em um inteiro.
            f1=int(a)
        elif '/' in fraction: #Este elif trata as cadeias da forma a/b
            m=a.find('/')
            Numerador=int(a[:m])
            Denominador=int(a[m+1:])
            if Denominador==0:#Aviso no caso você tente ingressar uma fraçaõ com denominador nulo
                print('Fração inválida. Não é possível dividir por zero')
                print('Vamos tentar mais uma vez')
            else: #neste caso tudo deu certo para transformar a cadeia em números e agora vamos usar esses números para criar uma fração
                ctrden=True
                f1=Rational(Numerador, Denominador)
                
            f1=Rational(Numerador, Denominador)
        elif '.' in fraction: #Trata as cadeias da forma a.b ou -a.b (decimais)
            if '-' in a:
                a=a[1:]
                m=a.find('.')
                ParteInteira=int(a[:m])
                ParteDecimal=int(a[m+1:])
                TamanhoDecimal=len(a[m+1:])
                f1=ParteInteira+Rational(ParteDecimal,10**TamanhoDecimal)
                f1=-1*f1
            else:
                m=a.find('.')
                ParteInteira=int(a[:m])
                ParteDecimal=int(a[m+1:])
                TamanhoDecimal=len(a[m+1:])
                f1=ParteInteira+Rational(ParteDecimal,10**TamanhoDecimal)
        return f1    



#Este código separa uma cadeia em tantos vetores (ainda em cadeias) contidos na cadeia original
#A cadeia: '(1,2), (3,2), (2,4)' sera vista como as a lista  ['(1,2)' '(3,2)'  e '(2,4)'].

def miselem(a):
    a=list(a)
    v,w=[],[]
    contfin,contini,k=0,0,0#Começando os indices
    cadeia=''#Esta cadeia vazia ira armazenar os elementos da lista
    for i in range(0, len(a)):
        if a[i]!=')':
            contfin+=1#O contador final tera por valor o número de elementos do início da cadeia até o elemento anterior a ')'
        else:
            for j in range(contini, contini+contfin+1):#Neste for a cadeia armazena o primeiro vetor para transforma-lo em cadeia
                cadeia+=a[j]
            v.append(cadeia)#adicionamos o primeiro vetor como elemento da lista v
            k+=1#Este contador aumenta cada vez que um elemento é colocado na lista v, ou seja conta o número de vetores
            contini=contini+contfin+1#o contador iniciará no elemento após '('
            contfin=0#contador final reinicia
            i+=1#Este contador pula que contfin aumente quando você avalia os sinais ','
        cadeia=''#A cadeia reinicia
    for i in range(0,k):#
        if i==0:
            w.append(str(v[0]))#A cadeia zero inicia em '(' e finaliza em ')'
        else:
            w.append(str(v[i][1::]))#Estas cadeias contém uma ',' antes do vetor então aqui retiramos essa ','
    return w



#Este código toma o vetor '(1,2,4)' e transforma ele na tupla (1,2,4) o que permite operar os elementos como números
def meuvetor(a):
    a=list(a)
    v,w=[],[]
    contfin,contini,k=0,1,0#contini inícia em 1 para eliminar '(' em cada vetor
    cadeia=''
    for i in range(1, len(a)):
        if a[i]!=',' and a[i]!=')':#contfin aumentará até acabar o primeiro número real ou até acabar os vetores
            contfin+=1
        else:
            for j in range(contini, contini+contfin):#Toma  o i-esimo vetor dentro da cadeia e transforma ele no i-esimo elemento da lista sendo ainda cadeia
                cadeia+=a[j]
            v.append(cadeia)#Observe que cada cadeia aqui é numérica mas está no formato str
            #print(v[k])
            k+=1#Este contador aumenta cada vez que você adiciona um elemento à lista
            contini=contini+contfin+1
            contfin=0
            cadeia=''
    for i in range(0,k):
        w.append(numtofrac(v[i]))#A cadeia numérica é transformada em número através da função numtofrac
    return w


#Os códigos abaixo são operações com vetores
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



def transformaCadeia(cadeia):
    f1 = 0  #
    for i in range(0, len(cadeia)):
        f1 += int(cadeia[i]) * 10 ** (len(cadeia) - 1 - i)
    return f1




#Sympy opções matemáticas
#pylatex opções de manipular frações



'''import sympy
def numtofrac(a):
    ctrden=False#Essa variável controla os casos a/0 pedindo que o usuário insira novamente o denominador
    ctrsinal=1#Essa variável controla os casos de cadeias da forma -a/b para não considerar o sinal como um carater
    while(not ctrden):#Este control pedira para você inserir a a/b desde que b=0
        fraction=list(a)
        if '-' in fraction:#Neste if o control do sinal muda caso a fração seja -a/b ou o número seja -a.b ou -a ele armazena o sinal -1
            fraction.remove('-')#a cadeia perde o caracter '-'
            ctrsinal=-1
        if '/' not in fraction and '.' not in fraction: #Neste if, se a cadeia é simplesmente um número transformamos a cadeia em um inteiro.
            f1 = transformaCadeia(fraction)
            ctrden=True#É necessário mudar o valor desta variável para não seguir repetindo o processo para sempre
            if ctrsinal==-1:#No caso de um numero -a ele transformou a cadeia a no número a e neste if irá trocar o sinal
                f1=-1*f1





        elif '/' in fraction: #Este elif trata as cadeias da forma a/b ou -a/b



            c=0
            for i in fraction:
                if i!='/':
                    c+=1#Esta varíavel conta a quantidade de cifras no numerador
                else: break
            cadeia1 = fraction[:c]
            cadeia2 = fraction[c+1:]
            num=0#armazena o numerador
            num = transformaCadeia(cadeia1)#Transformando a cadeia numerador em um número.
            den=0#armazea o denominador
            den = transformaCadeia(cadeia2)#Transforma a cadeia denominador em um número.

            if den==0:#Aviso no caso você tente ingressar uma fraçaõ com denominador nulo
                print('Fração inválida. Não é possível dividir por zero')
                print('Vamos tentar mais uma vez')
                ctrsinal=1
                           #É necessário voltar este control para 1 pois caso tu ingressa -3/0 ele teria armazenado -1 e na segunda iteração se ingressar a cadeia '3/2' ele iria devolver o número -3/2
            else: #neste caso tudo deu certo para transformar a cadeia em números e agora vamos usar esses números para criar uma fração
                ctrden=True
                f1=Rational(num, den)
                if ctrsinal==-1:#Se no tivessemos escrito ctrsinal=1 cinco linhas acima poderia dar o problema relatado por lá
                    f1=-1*f1





        elif '.' in fraction: #Trata as cadeias da forma a.b ou -a.b (decimais)
            ctrden=1#É necessário virar um porque aqui não temos problemas de denominador
            c=0
            for i in fraction:#conta a parte inteira do número
                if i!='.':
                    c+=1
                else: break
            num=0
            cadeia1 = fraction[:c]
            cadeia2 = fraction[c+1:]

            num= transformaCadeia(cadeia1)#transforma a cadeia a que pode ter várias casas por exemplo a='2344' no número a=2344
            tamanhoCadeia2 = len(cadeia2)
            #Trata a parte decimal ou seja a parte b da cadeia a.b para transforma-la em uma fração
            cadeia2Real = transformaCadeia(cadeia2)
            den = Rational(cadeia2Real,10**tamanhoCadeia2)
            f1=num+den#Soma a parte inteira e a fração decimal
            if ctrsinal==-1:#No caso de ter sido -a.b por exemplo '-23.56' ele so transformou acima a cadeia '23.56' no número 23.56 e agora irá adicionar o sinal
                f1=-1*f1
        return f1
'''