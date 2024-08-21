import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from sympy.utilities.lambdify import lambdify
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#--------------------------------------------------------------------------
#AGRADECIMENTO ESPECIAL AO PROF. DR. MARCOS DANIEL N. MAIA PELA ATENÇÃO! =)
#--------------------------------------------------------------------------



fxy_str = input("Digite a função f(x, y) que deseja: (ex: sin(sqrt(x**2 + y**2)), tan(x + y)), E**(x**2 + y**2), log(x): ")
x0_str=input('Digite o ponto X: ')
y0_str=input('Digite o ponto Y: ')
x0 = int(x0_str)
y0 = int(y0_str)

# Convertendo funções String em funções Simbólicas, de simbólicas para funções que posso utilizar no numpy

def converter_em_numpy(f_string):
    
    # Converter a string da função para uma expressão simbólica
    
    f_sympy = sp.sympify(f_string)
    
    #Usa lambdify para converter a expressão simbólica em uma função numérica que pode ser avaliada com numpy
    
    f_numpy = sp.lambdify((x, y), f_sympy, modules='numpy')
    return f_sympy,f_numpy

x, y = sp.symbols('x y') 
f_sympy , f_numpy = converter_em_numpy(fxy_str)

#--------------------------------------------------------#
    
# Calcula as derivadas parciais
f_x = sp.diff(f_sympy, x)
f_y = sp.diff(f_sympy, y)
    
# Avalia a função e as derivadas no ponto dado
f_x0_y0 = f_x.subs({x: x0, y: y0})
f_y0_y0 = f_y.subs({x: x0, y: y0})
f_x0_y0_val = f_sympy.subs({x: x0, y: y0})

def plano_tangente(x, y):
    return f_x0_y0_val + f_x0_y0 * (x - x0) + f_y0_y0 * (y - y0)
    

# z do ponto de tangência
z0 = plano_tangente(x0, y0)

fn=plano_tangente(x,y)
# Criação dos valores de x e y
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
x_grid, y_grid = np.meshgrid(x, y)


# Obtém os pontos da superfície
Z = f_numpy(x_grid, y_grid)


# Obtém os pontos do plano tangente
z_grid_plano_tangente = plano_tangente(x_grid, y_grid)


# Criação do gráfico 3D
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_grid, y_grid, Z, cmap='plasma',alpha=0.7)

# Plota o Ponto de Tangência
ax.scatter(x0, y0, z0, color='black', s=100)
# Plota o texto do Ponto de Tangênte
ax.text(x0+2,y0,z0-2,(f"Ponto P ({x0},{y0})"))


# Plota os pontos do plano tangente
ax.plot_surface(x_grid, y_grid, z_grid_plano_tangente,alpha=0.7)

# Personalização do gráfico
ax.set_title(f"O plano tangente a função f(x,y)={f_sympy} em P: ({x0},{y0}) é: z={fn}")
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

# Exibição do gráfico
plt.show()

testando outra vez