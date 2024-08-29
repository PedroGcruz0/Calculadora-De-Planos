#calcular máximos e mínimos
import sympy as sp
x, y = sp.symbols('x y')
# Defina a função
funcaostr = input("Digite a função f(x, y) que deseja calcular os pontos máximos e mínimos ex: x**4+y**4-4*x*y+1 ")
funcao = sp.sympify(funcaostr)

# Calcule as derivadas parciais
derivada_x = sp.diff(funcao, x)
derivada_y = sp.diff(funcao, y)

Hessiana = sp.hessian(funcao,(x,y) )#maneira mais objetiva de calcular Hessiana
# Encontre os pontos críticos
pontos_criticos = sp.solve([derivada_x, derivada_y], (x, y),domain=sp.S.Reals)
for pontos in pontos_criticos:
    if pontos[0].is_real and pontos[1].is_real: #função disponível no sympy para verificação se é real
        Hessiana_Avaliada = Hessiana.subs({x:pontos[0], y: pontos[1]})#função subs me permite fazer a avaliação dos pontos
        #calcular os determinantes dos pontos
        if(Hessiana_Avaliada.det()>=0):
            if(Hessiana[0].subs({x:pontos[0],y:pontos[1]})>=0):
                tipo = "Mínimo local"
            else:
                tipo = "Máximo local"
        elif(Hessiana_Avaliada.det()<0):
            tipo = "Ponto de sela"   
        else:
            tipo = "Não me permite obter nenhuma conclusão"     
        
        print(f"Ponto crítico: {pontos}, Tipo: {tipo}")

