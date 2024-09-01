import sympy as sp

x, y = sp.symbols('x y')

def verificar_entrada():
    funcaostr = input("Digite a função f válida: ")
    try:
        funcao = sp.sympify(funcaostr)   
        var = funcao.free_symbols
        if var == set():
            print("Você precisa inserir pelo menos uma variável!")
            return verificar_entrada()        
    except (SyntaxError, ValueError, sp.SympifyError):
        print("Insira uma função válida")
        return verificar_entrada()
    
    return funcao

def calcular_pc(funcao):
    var = list(funcao.free_symbols)
    PCs = []
    Hessiana = None
    
    if len(var) == 1:  # se for univariado
        var = var[0]
        d_x = sp.diff(funcao, var)
        pontos_criticos = sp.solve(d_x)
        for ponto in pontos_criticos:
            if ponto.is_real:
                PCs.append(ponto)
        return PCs, funcao
    
    else:  # se for multivariado
        derivada_x = sp.diff(funcao, x)
        derivada_y = sp.diff(funcao, y)
        Hessiana = sp.hessian(funcao, (x, y))
        
        pontos_criticos = sp.solve([derivada_x, derivada_y], (x, y), dict=True)
        for ponto in pontos_criticos:
            ponto_x = ponto[x]
            ponto_y = ponto[y]
            if ponto_x.is_real and ponto_y.is_real:
                PCs.append((ponto_x, ponto_y))
    
    return PCs, Hessiana

funcao1 = verificar_entrada()
pontos_criticos, Hessiana = calcular_pc(funcao1)

#lembrar que uma lista vazia é considerado falso em um contexto booleano
if not pontos_criticos:
    print("Nenhum ponto crítico encontrado.")

for pontos in pontos_criticos:
    if isinstance(pontos, tuple):  # se for multivariado
        Hessiana_Avaliada = Hessiana.subs({x: pontos[0], y: pontos[1]})
        determinante = Hessiana_Avaliada.det()
        
        if determinante > 0:
            if Hessiana_Avaliada[0, 0] > 0:
                tipo = "Ponto de Mínimo local"
            else:
                tipo = "Ponto de Máximo local"
        elif determinante < 0:
            tipo = "Ponto de sela"
        else:
            tipo = "Indeterminado"
        print(f"O ponto {pontos} é {tipo}")
    
    else:  # se for univariado
        d2_x = sp.diff(funcao1, x, 2)
        eq = d2_x.subs(x, pontos)
        if eq > 0:
            tipo = "Ponto de Mínimo local"
        else:
            tipo = "Ponto de Máximo local"
        print(f"O ponto ({pontos}) é {tipo}")