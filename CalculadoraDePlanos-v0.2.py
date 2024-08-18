import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

from sympy.utilities.lambdify import lambdify

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Exemplo de uso
#--------------------------------------------------------#
def f(x, y):
    return x**2 + y**2

x, y = sp.symbols('x y')
f_sym = sp.Pow(x, 2) + sp.Pow(y, 2)


# ponto
x0, y0 = 1, 1

#--------------------------------------------------------#
    
# Calcula as derivadas parciais
f_x = sp.diff(f_sym, x)
f_y = sp.diff(f_sym, y)
    
# Avalia a função e as derivadas no ponto dado
f_x0_y0 = f_x.subs({x: x0, y: y0})
f_y0_y0 = f_y.subs({x: x0, y: y0})
f_x0_y0_val = f_sym.subs({x: x0, y: y0})

def plano_tangente(x, y):
    return f_x0_y0_val + f_x0_y0 * (x - x0) + f_y0_y0 * (y - y0)
    

# z do ponto de tangência
z0 = plano_tangente(x0, y0)


# Criação dos valores de x e y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x_grid, y_grid = np.meshgrid(x, y)


# Obtém os pontos da superfície
z_grid = f(x_grid, y_grid)


# Obtém os pontos do plano tangente
z_grid_plano_tangente = plano_tangente(x_grid, y_grid)


# Criação do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_grid, y_grid, z_grid, cmap='viridis')

# Plota o Ponto de Tangência
ax.scatter(x0, y0, z0, color='black', s=100)

#Plota os pontos do plano tangente
ax.plot_surface(x_grid, y_grid, z_grid_plano_tangente)

# Personalização do gráfico
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

# Exibição do gráfico
plt.show()