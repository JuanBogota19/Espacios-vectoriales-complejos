import numpy as np
import unittest

def suma_vect(vector1, vector2):
    'Función para la Adición de vectores complejos.'
    resultado = vector1 + vector2
    return resultado

vector1 = np.array([1.+4.j, 2, 3], dtype = complex)
vector2 = np.array([4.+1.j, 5, 6], dtype = complex)

resultado = suma_vect(vector1, vector2)

print("1", resultado)

def inv_vect(vector):
    'Función para el Inverso (aditivo) de un vector complejo.'
    inverso_aditivo = -vector
    return inverso_aditivo

vector = np.array([1 + 4j, 2, 3], dtype=complex)
inverso_aditivo = inv_vect(vector)
print("2", inverso_aditivo)


def esc_vect(escalar, vector):
    'Función para la Multiplicación de un escalar por un vector complejo.'
    resultado = escalar * vector
    return resultado

escalar = 2
vector = np.array([4, 5, 6], dtype=complex)
resultado = esc_vect(escalar, vector)
print("3", resultado)

def suma_matrix(matrix1, matrix2):
    'Función para la Adición de matrices complejas.'
    resultado = matrix1 + matrix2
    return resultado

matrix1 = np.array([[1,2], [3,4]], dtype=complex)
matrix2 = np.array([[5,6], [7,8]], dtype=complex)
resultado = suma_matrix(matrix1, matrix2)
print("4", resultado)

def inv_matrix(matriz):
    'Función para la Inversa (aditiva) de una matriz compleja.'
    inverso_aditivo = -matriz
    return inverso_aditivo

matriz = np.array([[1 + 4j, 2, 3], [4, 5, 6]], dtype=complex)
inverso_aditivo = inv_matrix(matriz)
print("5", inverso_aditivo)

def esc_matrix(escalar, matriz):
    'Función para la Multiplicación de un escalar por una matriz compleja.'
    resultado = escalar * matriz
    return resultado

escalar = 2
matriz = np.array([[1 + 4j, 2, 3], [4, 5, 6]], dtype=complex)
resultado = esc_matrix(escalar, matriz)
print("6", resultado)

def t_matrix(matriz):
    'Función para la Transpuesta de una matriz/vector'
    filas, columnas = matriz.shape
    matriz_traspuesta = np.empty((columnas, filas), dtype=complex)
    for j in range(filas):
        for k in range(columnas):
            matriz_traspuesta[k][j] = matriz[j][k]
    return matriz_traspuesta

matriz = np.array([[1, 2, 3], [4 + 2j, 5, 6]], dtype=complex)
resultado = t_matrix(matriz)
print("7", resultado)

def conj_matrix(matriz):
    'Función para la Conjugada de una matriz/vector'
    filas, columnas = matriz.shape
    matriz_conjugada = np.empty((filas, columnas), dtype=complex)
    for j in range(filas):
        for k in range(columnas):
            elemento_original = matriz[j][k]
            elemento_conjugado = elemento_original.real - elemento_original.imag * 1j
            matriz_conjugada[j][k] = elemento_conjugado
    return matriz_conjugada

matriz = np.array([[1 + 2j, 3, -4j], [5j, 5, 4]], dtype=complex)
resultado = conj_matrix(matriz)
print("8", resultado)

def adj_matrix(matriz_compleja):
    'Funcion para la Adjunta (daga) de una matriz/vector'
    matriz_adjunta = t_matrix(conj_matrix(matriz_compleja))
    return matriz_adjunta

matriz_compleja = np.array([[1 + 2j, 3, -4j], [5j, 5, 4]], dtype=complex)
resultado = adj_matrix(matriz_compleja)
print("9", resultado)

def prodc_matrix(matriz1, matriz2):
    'Funcion para el Producto de dos matrices (de tamaños compatibles)'
    producto = matriz1 @ matriz2
    return producto

matriz1 = np.array([[1, 2, 3], [4, 5, 6]], dtype=complex)
matriz2 = np.array([[7, 8], [9, 10], [11, 12]], dtype=complex)
resultado = prodc_matrix(matriz1, matriz2)
print("10", resultado)

def accion_matriz(matriz, vector):
    'Función para calcular la "acción" de una matriz sobre un vector'

    filas_matriz, columnas_matriz = matriz.shape
    filas_vector, = vector.shape

    if columnas_matriz != filas_vector:
        return False

    resultado = np.zeros((filas_matriz), dtype=complex)

    for j in range(filas_matriz):
        for k in range(columnas_matriz):
            resultado[j] += matriz[j, k] * vector[k]
    return resultado

matriz = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]], dtype=complex)
vector = np.array([2, 3, 4])
resultado = accion_matriz(matriz, vector)
print("11", resultado)

def inter_vect(vector1, vector2):
    'Funcion del Producto interno de dos vectores'
    producto_interno = 0
    for j in range(len(vector1)):
        producto_interno += vector1[j] * vector2[j]
    return producto_interno

vector1 = np.array([1+2j, 2, 3], dtype=complex)
vector2 = np.array([4, 5, 6], dtype=complex)
resultado = inter_vect(vector1, vector2)
print("12", resultado)

def norma_vector(vector):
    cuadrado = np.square(vector)
    suma = np.sum(cuadrado)
    norma = suma**0.5
    return norma

vector = np.array([1, 2, 3], dtype=complex)
resultado = norma_vector(vector)
print("13", resultado)

def distancia_vector(vector1, vector2):
    vector = vector1 - vector2
    distancia = norma_vector(vector)
    return distancia

vector1 = np.array([1, -2], dtype=complex)
vector2 = np.array([3, 4], dtype=complex)
resultado = distancia_vector(vector1, vector2)
print("14", resultado)

#def propio_matriz







