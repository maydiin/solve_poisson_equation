import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy
import math

import numpy as np
from  matplotlib.pyplot import *
def matrice_systeme(h):
    noudes=1/h
    diagonal=[]
    for i in range(int(noudes)):
        diagonal.append(-4)
    A=np.diag(diagonal)
    index=[]
    for i in range(int(noudes)):
        index.append(i)
    rem_ind = int(math.sqrt(noudes) - 1)
    for i in range(int(math.sqrt(noudes))):
        index.pop(rem_ind)
        rem_ind+=int(math.sqrt(noudes) - 1)

    for i in index:
        A[i][i+1]=1
        A[i+1][i]=1

    index_one=int(math.sqrt(noudes))
    for i in range(int(noudes)-int(math.sqrt(noudes))):
        A[i][index_one]=1
        A[index_one][i]=1
        index_one+=1

    return A

def source(x,y): #function source
    return 8*((np.pi)**2)*np.around(np.sin(math.radians(360*x)), decimals=5)*np.around(np.cos(math.radians(360*y)), decimals=5)

def val_func(m): #m=maillage
    h=1/m
    F=[]
    for i in range(1,m):
        for j in range(1,m):
            F.append(-source(j*h,1-(i*h))*(h**2))

    return F

#functions borders
def H(x): return 0
def D(y): return 0
def B(x): return 0
def G(y): return 0

def val_border(H,D,B,G,m):  #m=maillage
    h = 1 / m
    U=[]
    for i in range(1,m):
        U.append(H(i*h))
    for i in range(1,m):
        U.append(D(1-(i*h)))
    for i in range(1,m):
        U.append(B(1-(i*h)))
    for i in range(1,m):
        U.append(G(i*h))

    return U

def f_u(m):
    F=val_func(m)
    U=val_border(H,D,B,G,m)
    for i in range(m-1):
        F[i]=F[i]-U[i]
    for i in range(m-1,2*m-2):
        F[(m-2)+(i-(m-1))*(m-1)]= F[(m-2)+(i-(m-1))*(m-1)] -U[i]
    for i in range(2*m-2,3*m-3):
        F[((m-1)*(m-1)-1)-i+(2*m-2)]=F[((m-1)*(m-1)-1)-i+(2*m-2)] -U[i]
    for i in range(m-1):
        F[i*(m-1)]=F[i*(m-1)]- U[3*m-3+i]

    return F

def solution(maillage):
    A=matrice_systeme(1/((maillage-1)**2))
    F=f_u(maillage)
    u=np.linalg.solve(A,F)

    x=[]
    y=[]
    for i in range(maillage-1):
        for j in range(1,maillage):
            y.append((maillage-1-i)/maillage)
            x.append(j/maillage)
    z = u

    fig = plt.figure(figsize = (10,30))
    ax = plt.axes(projection='3d')
    ax.grid()

    ax.scatter(x, y, z, c = 'r', s = 5)
    ax.set_title('3D Scatter Plot')

    # Set axes label
    ax.set_xlabel('x', labelpad=20)
    ax.set_ylabel('y', labelpad=20)
    ax.set_zlabel('z', labelpad=20)
    ax.view_init(10, 50)
    plt.show()

solution(50)
