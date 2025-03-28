import sympy as sp
from sympy import oo, Symbol, limit, S
def verificar_entrada():
    funcaostr = input("Digite a função do limite: ")
    try:
        funcao = sp.sympify(funcaostr)
        var = funcao.free_symbols
        if var == set():
            print("Você precisa inserir pelo uma variável!")
            return verificar_entrada()
    except (SyntaxError, ValueError, sp.SympifyError):
        print("Insira uma função válida")
        return verificar_entrada()

    return funcao

def identificar_indeterminacao(expr, variavel, ponto):
    x = Symbol(variavel)
    # Convertendo o ponto para oo se for infinito
    try:
        if ponto.lower() in ['oo', 'inf', 'infinity']:
            p = oo
        else:
            p = sp.sympify(ponto)
    except:
        return "Ponto inválido. Use um número ou 'oo' para infinito."
    
 # Antes de começar, eu vejo se há indeterminação, pois o sympy resolve mesmo com indeterminação
    try:
        # Avalio meu numerador e denominador separado se for uma fração
        if expr.is_rational_function(x):
            num, den = expr.as_numer_denom()
            # Avalio no ponto que a variavel tende
            if p == oo:
                num_val = limit(num, x, p)
                den_val = limit(den, x, p)
            else:
                num_val = num.subs(x, p)
                den_val = den.subs(x, p)
            # Verifico os casos de indeterminação
            if num_val == 0 and den_val == 0:
                return "Indeterminação do tipo 0/0"
            elif (num_val in [oo, -oo]) and (den_val in [oo, -oo]):
                return "Indeterminação do tipo ∞/∞"
            elif (num_val in [oo, -oo]) and den_val.is_finite and den_val != 0:
                return "O limite tende a ∞. Não há indeterminação."
            elif num_val.is_finite and (den_val in [oo, -oo]):
                return "O limite tende a 0. Não há indeterminação."
        # Casos especiais
        if p == oo:
            expr_val = limit(expr, x, p)
        else:
            expr_val = expr.subs(x, p)
        if expr_val in [oo, -oo]:
            return f"O limite tende a {'+∞' if expr_val == oo else '-∞'}. Não há indeterminação."
        elif expr_val.is_finite:
            return f"O limite existe e vale {expr_val}. Não há indeterminação."
        # Outros tipos de indeterminação
        if expr_val == S.NaN:
            if expr.has(sp.Pow):
                base, expoente = expr.as_base_exp()
                if p == oo:
                    base_val = limit(base, x, p)
                    exp_val = limit(expoente, x, p)
                else:
                    base_val = base.subs(x, p)
                    exp_val = expoente.subs(x, p)
                if base_val == 1 and (exp_val in [oo, -oo]):
                    return "Indeterminação do tipo 1^∞"
                elif base_val == 0 and exp_val == 0:
                    return "Indeterminação do tipo 0^0"
                elif (base_val in [oo, -oo]) and exp_val == 0:
                    return "Indeterminação do tipo ∞^0"
        return "Não foi possível identificar a indeterminação. A expressão pode ser muito complexa."
    except Exception as e:
        return f"Erro ao analisar a expressão: {str(e)}"

expressao = verificar_entrada()
variavel = input("Digite a variável: ")
ponto = input("Digite o ponto para o qual a variável tende (ex: 0 ou oo): ")
resultado = identificar_indeterminacao(expressao, variavel, ponto)
print("\nResultado:", resultado)