import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from sympy.utilities.lambdify import lambdify
from mpl_toolkits.mplot3d import Axes3D


#Beta (Usar pontos pi em funções trigonométricas)
 
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

f_sympy = verificar_entrada()
x0_str = input('Digite o ponto X: ')
y0_str = input('Digite o ponto Y: ')

# Convertendo as entradas em expressões simbólicas, agora eu posso receber frações
x0_sym = sp.sympify(x0_str)
y0_sym = sp.sympify(y0_str)
# Ter esses valorem em float vai me ajudar a connfigurar o scatter de acordo com os pontos do usuário
x0_float = float(x0_sym.evalf())
y0_float = float(y0_sym.evalf())
x, y = sp.symbols('x y')
f_numpy = lambdify((x, y), f_sympy, modules='numpy')

# Calcula as derivadas parciais
f_x = sp.diff(f_sympy, x)
f_y = sp.diff(f_sympy, y)

# Avalia as derivadas e a função no ponto dado
f_x0_y0 = f_x.subs({x: x0_sym, y: y0_sym})
f_y0_y0 = f_y.subs({x: x0_sym, y: y0_sym})
f_x0_y0_val = f_sympy.subs({x: x0_sym, y: y0_sym})

# Define a função do plano tangente simbolicamente, isso servirá para mostrar a função do plano tangente de maneira normal
plano_tangente_expr = f_x0_y0_val + f_x0_y0 * (x - x0_sym) + f_y0_y0 * (y - y0_sym)

# Converte a função do plano tangente para uma função numpy, usando o numpy para avaliação de pontos temos uma maneira mais precisa e mais rápida
plano_tangente_numpy = lambdify((x, y), plano_tangente_expr, modules='numpy')

# Criação dos valores de x e y
x_vals = np.linspace(-(x0_float**2)-5,(x0_float**2)+5, 100)
y_vals = np.linspace(-(y0_float**2)-5,(y0_float**2)+5, 100)
x_grid, y_grid = np.meshgrid(x_vals, y_vals)

# Obtém os pontos da superfície
Z = f_numpy(x_grid, y_grid)

# Obtém os pontos do plano tangente
z_grid_plano_tangente = plano_tangente_numpy(x_grid, y_grid)

# Criação do gráfico 3D
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_grid, y_grid, Z, cmap='viridis', alpha=0.8)

# Plota o Ponto de Tangência
ax.scatter(float(x0_sym.evalf()), float(y0_sym.evalf()), float(f_x0_y0_val.evalf()), color='black', s=100)
# Plota o texto do Ponto de Tangência
ax.text(float(x0_sym.evalf()) + 2, float(y0_sym.evalf()), float(f_x0_y0_val.evalf()) - 2, f"Ponto P ({x0_str}, {y0_str})")

# Plota os pontos do plano tangente
ax.plot_surface(x_grid, y_grid, z_grid_plano_tangente, alpha=0.8)

# Personalização do gráfico
ax.set_title(f"O plano tangente a função: {f_sympy} em P: ({x0_str}, {y0_str}) é {plano_tangente_expr}")
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

# Exibição do gráfico
plt.show()
