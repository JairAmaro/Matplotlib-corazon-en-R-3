# Author: Jair Amaro 
from mpl_toolkits.mplot3d import Axes3D   # pip install mplot3d
from matplotlib import pyplot as plt      # pip install matplotlib
import numpy as np                        # pip install numpy
from skimage import measure               # pip install scikit-image

n = 125                                   # numero de puntos en cada eje, entre mas grande se parace mas es mas suave la superficie
x = np.linspace(-3,3,n)                   # rango de valores en cada eje x,y,z por R^3 
y = np.linspace(-3,3,n)
z = np.linspace(-3,3,n)
X, Y, Z =  np.meshgrid(x, y, z)           # crea una malla de puntos en R^3

def rebe(x,y,z):                          # funcion que define la forma del corazon
    F = 320 * ((-x**2 * z**3 -9*y**2 * z**3/80) + (x**2 + 9*y**2/4 + z**2-1)**3) 
    return F
vol = rebe(X,Y,Z) # crea un volumen de puntos en R^3

verts, faces, normals, values = measure.marching_cubes(vol, 0,  spacing=(0.1, 0.1, 0.1)) # crea la superficie de la malla de puntos en R^3

plt.style.use('dark_background') # fondo negro para la figura
# ploteamos 3d
fig = plt.figure(figsize=(7,7)) # tamaño de la figura
ax = fig.add_subplot(projection='3d') 

# ploteamos la superficie
ax.plot_trisurf(verts[:, 0], 
                verts[:,1],
                faces, 
                verts[:, 2],
                cmap='autumn_r',     # importante -*-*-*-*-*-*-*-*_ 
                edgecolor = 'red',   # coemnta esta linea para ver la superficie sin bordes y quitale el # al alpha para ver otro bonito 
                #calpha = 0.5,
                lw=1) 

ax.view_init(15, -15) # angulo de vista de la figura 3d 
plt.title("Para la mas preciosa: Rebe ❤  \n" + r"Funcion:$ \quad -x^2z^3 -\frac{9y^2z^3}{80} + \left(x^2 + \frac{9y^2}{4} + z^2 - 1\right)^{3} $",  fontsize=15); # titulo de la figura
plt.show() # muestra la figura
