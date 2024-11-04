import numpy as np
import sympy as sp
from numpy.linalg import norm
import math
from math import cos, sin, pi

def rotX(ang:float):
    ang = (ang*pi)/180
    R = np.array([[1,0       ,0        ,0],
                  [0,cos(ang),-sin(ang),0],
                  [0,sin(ang),cos(ang) ,0],
                  [0,0       ,0        ,1]])
    return R

def rotY(ang:float):
    ang = (ang*pi)/180
    R = np.array([[cos(ang) ,0,sin(ang),0],
                  [0        ,1,0       ,0],
                  [-sin(ang),0,cos(ang),0],
                  [0        ,0,0       ,1]])
    return R

def rotZ(ang:float):
    ang = (ang*pi)/180
    R = np.array([[cos(ang),-sin(ang),0,0],
                  [sin(ang),cos(ang) ,0,0],
                  [0       ,0        ,1,0],
                  [0       ,0        ,0,1]])
    return R

def D_H(param:np):
    theta = param[0]
    d = param[1]
    a = param[2]
    alpha = param[3]
    
    A = np.array([
        [math.cos(theta), -math.cos(alpha)*math.sin(theta),  math.sin(alpha)*math.sin(theta), a*math.cos(theta)],
        [math.sin(theta),  math.cos(alpha)*math.cos(theta), -math.sin(alpha)*math.cos(theta), a*math.sin(theta)],
        [              0,                  math.sin(alpha),                  math.cos(alpha),                 d],
        [              0,                                0,                                0,                 1]
    ])
    return A

def D_H2(parametros):
    A = sp.Matrix([
        [sp.cos(parametros[0]), -sp.cos(parametros[3]) * sp.sin(parametros[0]),  sp.sin(parametros[3]) * sp.sin(parametros[0]), parametros[2] * sp.cos(parametros[0])],
        [sp.sin(parametros[0]),  sp.cos(parametros[3]) * sp.cos(parametros[0]), -sp.sin(parametros[3]) * sp.cos(parametros[0]), parametros[2] * sp.sin(parametros[0])],
        [0,                      sp.sin(parametros[3]),                         sp.cos(parametros[3]),                         parametros[1]],
        [0,                      0,                                              0,                                              1]
    ])
    return A

def crearCuaternio(theta,k:np.array):
    k = k/norm(k)
    q0 = q0=cos(theta/2)
    qv=k*sin(theta/2)
    Q = np.zeros(4)
    Q[0] = q0
    Q[1:4] = qv
    return Q
    
def conjCuaternio(Q:np.array):
    Q1 = np.zeros(4)
    Q1[0:4] = Q[0:4]
    Q1[1:4] = -Q[1:4]
    return Q1
    
def proCuaternios(Q1:np.array,Q2:np.array):
    s1 = Q1[0]
    v1 = Q1[1:4]
    s2 = Q2[0]
    v2 = Q2[1:4]
    
    s3 = s1*s2-np.dot(v1,v2)
    v3 = np.cross(v1,v2)+s1*v2+s2*v1
    
    Q3 = np.zeros(4)
    Q3[0] = s3
    Q3[1:4] = v3
    return Q3
    
def modeloDinamico(par:sp.Matrix, jrj:sp.Matrix, g:sp.Matrix):
    # pi = sp.symbols('pi')
    # par.subs(pi, sp.pi)
    n = par.shape[0]
    jrj = np.vstack([jrj, np.ones(n)])
    g = np.append(g, 0)

    # Crear variables simbólicas
    q = sp.symbols(f'q1:{n+1}')
    m = sp.symbols(f'm1:{n+1}')
    dq = sp.symbols(f'dq1:{n+1}')

    if jrj.shape[1] == n and par[n-1, 3] == 0:
        x, y, z = jrj[:3, :]
        A0n = sp.eye(4)
        A0i = np.array([sp.zeros(4, 4) for _ in range(n)])
        A = np.array([sp.zeros(4, 4) for _ in range(n)])
        Uij = np.empty((4, 4, n, n), dtype=object)
        Uijk = np.empty((4, 4, n, n, n), dtype=object)
        J = np.array([sp.zeros(4, 4) for _ in range(n)])

        # Paso 2
        for i in range(n):
            A[i] = D_H2(par[i, :])
            A0n = A0n @ A[i]
            A0i[i] = A0n

        # Paso 3
        for i in range(n):
            for j in range(n):
                Uij[:, :, i, j] = sp.diff(sp.Matrix(A0i[i]), q[j])

        # Paso 4
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    Uijk[:, :, i, j, k] = sp.diff(sp.Matrix(Uij[:, :, i, j]), q[k])

        # Paso 5
        for i in range(n):
            J[i] = sp.Matrix([[x[i]**2 * m[i]  , x[i]*y[i] * m[i], x[i]*z[i] * m[i], x[i] * m[i]],
                              [y[i]*x[i] * m[i], y[i]**2 * m[i]  , y[i]*z[i] * m[i], y[i] * m[i]],
                              [z[i]*x[i] * m[i], z[i]*y[i] * m[i], z[i]**2 * m[i]  , z[i] * m[i]],
                              [x[i] * m[i]     , y[i] * m[i]     , z[i] * m[i]     , m[i]       ]])

        # Paso 6
        D = sp.zeros(n, n)
        for i in range(n):
            for j in range(n):
                for k in range(max(i, j), n):
                    D[i, j] += sp.trace(sp.Matrix(Uij[:, :, k, j]) @ sp.Matrix(J[k]) @ sp.Matrix(Uij[:, :, k, i].T))

        # Paso 7
        hikm = np.array([sp.zeros(n, n) for _ in range(n)])
        for i in range(n):
            for k in range(n):
                for m in range(n):
                    for j in range(max(i, k, m), n):
                        hikm[m][i,k] += sp.trace(sp.Matrix(Uijk[:, :, j, k, m]) @ sp.Matrix(J[j]) @ sp.Matrix(Uij[:, :, j, i].T))
                    hikm[m][i,k] = sp.simplify(hikm[m][i,k])

        # Paso 8
        H = sp.zeros(n, 1)
        for i in range(n):
            for k in range(n):
                for m in range(n):
                    H[i] += hikm[m][i,k] * dq[k] * dq[m]

        # Paso 9
        m = sp.symbols(f'm1:{n+1}')
        C = sp.zeros(n, 1)
        for i in range(n):
            for j in range(n):
                C[i] -= m[j] * (g) @ (Uij[:, :, j, i]) @ (jrj[:, j])

        # Paso 10
        n_d = 5
        D = sp.N(sp.simplify(D), n_d)
        H = sp.N(sp.simplify(H), n_d)
        C = sp.N(sp.simplify(C), n_d)
        
        # Crear una lista vacía para almacenar los símbolos
        t = []
        # Bucle para llenar el vector t
        for i in range(n):
            # Comprobar si qi está en la primera columna de Par
            if q[i] in par[i, 0].free_symbols:
                # Si qi está presente, agregar Ti
                t.append(sp.symbols(f'T{i+1}'))
            else:
                # Si qi no está presente, agregar Fi
                t.append(sp.symbols(f'F{i+1}'))
        t = sp.Matrix([t])
        t = t.T

        ddq = []
        for i in range(n):
            ddq.append(['ddq'+str(i+1)]) 

        return t,ddq,D,H,C

    else:
        raise ValueError("Los parámetros ingresados no son correctos o no están de la forma explicada en las instrucciones")
        return None, None, None
    