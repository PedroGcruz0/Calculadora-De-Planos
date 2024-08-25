#calcular máximos e mínimos
import sympy as sp
from sympy import symbols, diff
from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt
#Estou afirmando que X e Y são Reais, então quaisquer soluções para equações em termos xy serão desconsideradas as soluções complexas.
x, y = sp.symbols('x y', real = True)
f , g = sp.symbols('f g')
# Defina a função
#funcaostr = input("Digite a função f(x, y) que deseja plotar (por exemplo, sin(sqrt(x**2 + y**2))): ")
#funcao = sp.sympify(funcaostr)

funcao= x**4+y**4-4*x*y+1
# Calcule as derivadas parciais
derivada_x = sp.diff(funcao, x)
derivada_y = sp.diff(funcao, y)

# Encontre os pontos críticos
pontos_criticos = sp.solve([derivada_x, derivada_y], [x, y])

# Calcule a matriz Hessiana
hessiana = sp.Matrix([[sp.diff(diff(funcao, x, x), x), diff(diff(funcao, x, y), y)],
                   [diff(diff(funcao, x, y), y), diff(diff(funcao, y, y), y)]])
print(pontos_criticos)
print (f"A matriz Hessiana é: {hessiana}")