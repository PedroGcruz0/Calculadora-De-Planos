from sympy import *
from minhabiblioteca import *
# a todo momento que eu falar de vetor estou falando do ponto entendendo ele como um vetor por ter mais de uma componente
a=input('ingrese os pontos(vetores de Rn) separados por vírgula:')
a=a.replace(' ', '')
m=a.count(')') #m conta o número vetores que você inseriu pois cada vetor acaba em )
vetores=miselem(a)
t=0
#acima ingresamos uma cadeia e transformamos ela para lista eliminando os espaços. Cada elemento da lista acima é um vetor mas está ainda como cadeia
dimini=vetores[0].count(',') #dimini= conta o número de , no primeiro elemento da lista, ou seja, a dimensao será dimini+1
for i in range(1,m):
    dimfin=vetores[i].count(',') #dimfin analisa se os vetores após o primeiro tem a mesma dimensão ou não
    if dimini!=dimfin:
        t=1 #se t=1 então os vetores não são da mesma dimensão logo não será possivel operar eles.
if t==1:
    print('você inseriu os seguintes {} pontos: '.format(m))
    b=[]
    for i in range(0,m):
        b.append(meuvetor(vetores[i]))# a função meu vetor transforma cada cadeia na tupla vetores para uma lista onde cada elemento da lista deixa de ser caideia para virar número.
        print(tuple(b[i]))
    print('Não é possível operar pontos(vetores) de dimensões diferentes.')
else:
    if m==2:#se m=2 tem-se dois vetores logo é possível criar uma reta p0+tp1
        print('Você inseriu os seguintes {} vetores de dimensão {}: '.format(m,dimini+1))
        b=[]
        for i in range(0,m):
            b.append(meuvetor(vetores[i]))
            print(tuple(b[i]))
        if b[0]!=b[1]:
            vetordir=mirest(b[1],b[0])#vetordir armazena o vetor diretor da reta ou seja a diferencia dos pontos dados.
            print('A equação vetorial da reta que passa pelos vetores dados é:')
            print('L:{}+t{}'.format(tuple(b[0]),tuple(vetordir)))#transformar  a tupla é somente para parecer vetores () no lugar de []
            if dimini==1: #dimini=1 quer dizer que são vetores em r2, ou seja podemos escrever equação geral
                vetornormal=[-vetordir[1],vetordir[0]] #as componentes deste vetor são a e b na equação ax+by=c
                x=Symbol('x')
                y=Symbol('y')
                c=miproi(vetornormal,b[0])# este valor es para calcular el termino c da ax+by=c
                print('O vetor diretor à reta é v={}-{}={}'.format(tuple(b[1]),tuple(b[0]),tuple(vetordir)))
                print('O vetor normal à reta é n={}'.format(tuple(vetornormal)))
                print('Portanto, a equação da reta é:')
                print('{}=c'.format(1*vetornormal[0]*x+1*vetornormal[1]*y))
                print('onde c={}.{}={}'.format(tuple(vetornormal),tuple(b[0]),c))
                if vetornormal[0]<0:#Isto somente é visual para ter x com sinal positivo.
                    print('Em consequência, a equação geral da reta que passa pelos pontos dados é: ',end='')
                    print(-1*vetornormal[0]*x-1*vetornormal[1]*y,end='')
                    print(' = {}'.format(-c))
                else: #mesma coisa, visual 
                    print('Em consequência, a equação da reta que passa pelos pontos dados é: ',end='')
                    print(vetornormal[0]*x+vetornormal[1]*y,end='')
                    print(' = {}'.format(c))
        else:
            print('Na realidade os dois vetores inseridos são iguais.')        
    if m==3:#neste caso tem-se três vetores
       if dimini==2:#dimini=2 indica que são três vetores em r3 usando o 'if' acima
        print('Você inseriu os seguintes {} vetores de dimensão {}: '.format(m,dimini+1))
        b=[]
        for i in range(0,m):
            b.append(meuvetor(vetores[i]))
            print(tuple(b[i]))
        v1=mirest(b[0],b[1])#Dados os pontos b0 e b1 criamos o vetor v1 contido no plano
        v2=mirest(b[0],b[2])#Dados os pontos b0 e b1 criamos o vetor v2 contido no plano 
        n=mipvec(v1,v2)#n é o vetor normal ou seja o produto vetorial de v1 e v2
        d=miproi(n,b[0])#A equação do plano é (p-b0).n=0 separando p.n é o lado algébrico e n.b0 é d na equação ax+by+cz=d
        x=Symbol('x')#permite trabalhar com variável x análogo para as outras variáveis
        y=Symbol('y')
        z=Symbol('z')
        if n[0]==n[1]==n[2]==0:#neste caso o vetor normal é nulo ou seja os vetores v1 e v2 são colineares
            print('Os três vetores são colineares, logo não podem gerar um plano.')
        else: #neste caso o vetor normal não é nulo portanto posso criar o plano
            print('Dois vetores contidos no plano são: ')
            print('v={}={}-{}'.format(tuple(v1),tuple(b[0]),tuple(b[1])))
            print('w={}={}-{}'.format(tuple(v2),tuple(b[0]),tuple(b[2])))
            print('Daí, o vetor normal ao plano é:')
            print('n=v x w = {}x{}={}'.format(tuple(v1),tuple(v2),tuple(n)))
            print('Portanto a equação do nosso plano é: {}=d'.format(1*n[0]*x+1*n[1]*y+1*n[2]*z))
            print('Para d={}.{}={}'.format(tuple(n),tuple(b[0]),d))
            if n[0]<0:#parte estética mesmo que no caso da reta anterior
                print('Em consequência, a equação do plano que passa pelos pontos dados é: ',end='')
                print(-1*n[0]*x-1*n[1]*y-1*n[2]*z,end='')
                print(' = {}'.format(-d))
            else: #mesma coisa, estética.
                print('Em consequência, a equação do plano que passa pelos pontos dados é: ',end='')
                print(n[0]*x+n[1]*y+n[2]*z,end='')
                print(' = {}'.format(d))