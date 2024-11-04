import sympy as sp
from functions.unidad_1 import modeloDinamico


# Definir las variables simbólicas
q1, q2, L1 = sp.symbols('q1 q2 L1')

# Definir los parámetros de D-H
# Par = sp.Matrix([[-sp.pi/2, q1, L1, -sp.pi/2],
#                  [0       , q2, 0 , 0       ]])
# Par = sp.Matrix([[sp.sympify('-pi/2'), sp.sympify('q1'), sp.sympify('L1'), sp.sympify('-pi/2')],
#                  [sp.sympify('0')       , sp.sympify('q2'), sp.sympify('0') , sp.sympify('0')       ]])
Par = [['q1','0','0','-pi/2'],
       ['0','q2','0','0']]
Par = sp.Matrix(sp.sympify(Par))

# Definir las coordenadas de los centros de masas
jrj = sp.Matrix([[0, 0],
                 [0, 0],
                 [0, 0]])

# Definir el vector de gravedad
g = sp.Matrix([0, 0, -9.80665])

# Llamar a la función modelo_dinamico
t,D, H, C = modeloDinamico(Par, jrj, g)

# Mostrar los resultados
print("D:", D)
print("H:", H)
print("C:", C)