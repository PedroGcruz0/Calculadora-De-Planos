import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plano_tangente(f, ponto):
    x, y = sp.symbols('x y')
    x0, y0 = ponto
    
    # Calcula as derivadas parciais
    f_x = sp.diff(f, x)
    f_y = sp.diff(f, y)
    
    # Avalia a função e as derivadas no ponto dado
    f_x0_y0 = f_x.subs({x: x0, y: y0})
    f_y0_y0 = f_y.subs({x: x0, y: y0})
    f_x0_y0_val = f.subs({x: x0, y: y0})
    
    # Equação do plano tangente
    plano_tangente_eq = f_x0_y0_val + f_x0_y0 * (x - x0) + f_y0_y0 * (y - y0)
    
    #return f_x0_y0_val, plano_tangente_eq
    return plano_tangente_eq

'2*x + 2*y - 2'
'2,+2,-2'
def normalizar_plano_tangente(X, Y, plano):
    plano_str = str(plano)
    plano_str = plano_str.replace("*x", ",")
    plano_str = plano_str.replace("*y", ",")
    plano_str = plano_str.replace(" ", "")
    plano_normalizado = plano_str.split(",")

    coeficientes = []
    for coefiente in plano_normalizado:
        coeficientes.append(coefiente)
    
    c_x = float(coeficientes[0])
    c_y = float(coeficientes[1])
    c_z = float(coeficientes[2])

    print(type(c_x))

    return c_x*X + c_y*Y + c_z



# Exemplo de uso
x, y = sp.symbols('x y')
f = x**2 + y**2  # Função exemplo
ponto = (1, 1)  # Ponto onde queremos o plano tangente

plano = plano_tangente(f, ponto)

# Criação dos valores de x e y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Função z = x^2 + y^2
#Z = plano

Z= normalizar_plano_tangente(X, Y, plano)

# Criação do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Personalização do gráfico
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')
ax.set_title(f'Gráfico 3D da função z = {plano}')

# Exibição do gráfico
plt.show()

