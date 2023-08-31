import numpy as np
import unittest

def suma_vect(a,b):
    'Función para la Adición de vectores complejos.'
    m = np.array(np.zeros((1,3)),dtype = complex)
    n = np.array(np.zeros((1,3)),dtype = complex)
    for j in range(0,m.shape[0]):
        for k in range(0,m.shape[1]):
            m[j,k] = a[j,k]
            n[j,k] = b[j,k]
            c[j,k] = a[j,k]+b[j,k]

    return c

a = np.array([[1,2,3]], dtype=complex)
b = np.array([[1,2,3]], dtype=complex)
c = np.array(np.zeros((1,3)), dtype=complex)

def inv_vect(d):
    'Función para el Inverso (aditivo) de un vector complejo.'
    m = np.array(np.zeros((1,3)),dtype = complex)


    for j in range(0,m.shape[0]):
        for k in range(0,m.shape[1]):
            m[j,k] = d[j,k]
            e[j,k] = (-d[j,k])
            f[j,k] = m[j,k]+e[j,k]

    return f

d = np.array([[1,2,3]], dtype=complex)
e = np.array(np.zeros((1,3)), dtype=complex)
f = np.array(np.zeros((1,3)), dtype=complex)


def esc_vect(z):
    'Función para la Multiplicación de un escalar por un vector complejo.'
    m = np.array(np.zeros((1,3)),dtype=complex)
    for j in range(0,m.shape[0]):
        for k in range(0,m.shape[1]):
            m[j,k]=z[j,k]*4
    return m

z = np.array([[1.+2.j,2,3]], dtype=complex)

def suma_matrix():
    'Función para la Adición de matrices complejas.'
    a = np.array([[1.+1.j,2],[3,4.+4.j]], dtype = complex)
    b = np.array([[9,-3],[3,5.+3.j]], dtype = complex)
    c = a + b

    return c

def inv_matrix():
    'Función para la Inversa (aditiva) de una matriz compleja.'
    a = np.array([[1.+1.j,-7,-8],[1,-4,-4],[-1,3,3]], dtype = complex)
    b = (-a)
    c = a + b

    return c

def esc_matrix(a):
    'Función para la Multiplicación de un escalar por una matriz compleja.'
    m = np.array(np.zeros((3,3)),dtype=complex)
    for j in range(0,m.shape[0]):
        for k in range(0,m.shape[1]):
            m[j,k]=a[j,k]*2
    return m

g = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=complex)

def t_matrix():
    'Función para la Transpuesta de una matriz/vector'
    matrix = np.array([[1.+1.j,-7,-8],[1,-4,-4],[-1,3,3]], dtype = complex)

    result = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]
    return result

def conj_matrix(zz):
    'Función para la Conjugada de una matriz/vector'
    matriz = []
    for i in zz:
        fila = []
        for k in i:
            fila.append(k.conjugate())
            matriz.append(fila)

    return (matriz)


print("Adición de vectores complejos",suma_vect(a,b))
print("Inverso (aditivo) de un vector complejo",inv_vect(d))
print("Multiplicación de un escalar por un vector complejo", esc_vect(z))
print("Adición de matrices complejas", suma_matrix())
print("Multiplicación de un escalar por una matriz compleja", esc_matrix(g))
print("inversa aditiva matriz", inv_matrix())
print("Transpuesta de una matriz/vector", t_matrix())
print("Conjugada de una matriz/vector",conj_matrix(np.array([[1.+1.j,-7,-8],[1,-4,-4],[-1,3,3]], dtype = complex)))
