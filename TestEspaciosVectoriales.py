import EspaciosVectoriales as ev
import numpy as np
import unittest

class TestCplxOperations(unittest.TestCase):

    def testsuma_vec(self):
        vector1 = np.array([1.+4.j, 2, 3], dtype=complex)
        vector2 = np.array([4.+1.j, 5, 6], dtype=complex)
        resultado_esperado = np.array([5.+5.j, 7, 9], dtype=complex)
        resultado_real = ev.suma_vect(vector1, vector2)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testinv_vect(self):
        vector = np.array([1.+4.j, 2, 3], dtype=complex)
        resultado_esperado = np.array([-1.-4.j, -2.-0.j, -3.-0.j], dtype=complex)
        resultado_real = ev.inv_vect(vector)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testesc_vect(self):
        escalar = 2
        vector = np.array([4, 5, 6], dtype=complex)
        resultado_esperado = np.array([8.+0.j, 10.+0.j, 12.+0.j], dtype=complex)
        resultado_real = ev.esc_vect(escalar, vector)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testsuma_matrix(self):
        matrix1 = np.array([[1,2], [3,4]], dtype=complex)
        matrix2 = np.array([[5,6], [7,8]], dtype=complex)
        resultado_esperado = np.array([[6.+0.j, 8.+0.j], [10.+0.j, 12.+0.j]], dtype=complex)
        resultado_real = ev.suma_matrix(matrix1, matrix2)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testinv_matrix(self):
        matriz = np.array([[1.+4.j, 2, 3], [4, 5, 6]], dtype=complex)
        resultado_esperado = np.array([[-1.-4.j, -2.-0.j, -3.-0.j], [-4.-0.j, -5.-0.j, -6.-0.j]], dtype=complex)
        resultado_real = ev.inv_matrix(matriz)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testesc_matrix(self):
        escalar = 2
        matriz = np.array([[1 + 4j, 2, 3], [4, 5, 6]], dtype=complex)
        resultado_esperado = np.array([[2 + 8j, 4, 6], [8, 10, 12]], dtype=complex)
        resultado_real = ev.esc_matrix(escalar, matriz)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testt_matrix(self):
        matriz = np.array([[1, 2, 3], [4 + 2j, 5, 6]], dtype=complex)
        resultado_esperado = np.array([[1, 4 + 2j], [2, 5], [3, 6]], dtype=complex)
        resultado_real = ev.t_matrix(matriz)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testconj_matrix(self):
        matriz = np.array([[1 + 2j, 3, -4j], [5j, 5, 4]], dtype=complex)
        resultado_esperado = np.array([[1 - 2j, 3, 4j], [-5j, 5, 4]], dtype=complex)
        resultado_real = ev.conj_matrix(matriz)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testadj_matrix(self):
        matriz_compleja = np.array([[1 + 2j, 3, -4j], [5j, 5, 4]], dtype=complex)
        resultado_esperado = np.array([[1 - 2j, -5j], [3, 5], [4j, 4]], dtype=complex)
        resultado_real = ev.adj_matrix(matriz_compleja)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testprodc_matrix(self):
        matriz1 = np.array([[1, 2, 3], [4, 5, 6]], dtype=complex)
        matriz2 = np.array([[7, 8], [9, 10], [11, 12]], dtype=complex)
        resultado_esperado = np.array([[58, 64], [139, 154]], dtype=complex)
        resultado_real = ev.prodc_matrix(matriz1, matriz2)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testaccion_matriz(self):
        vector = np.array([2, 3, 4])
        matriz = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]], dtype=complex)
        resultado_esperado = np.array([20, 47, 74], dtype=complex)
        resultado_real = ev.accion_matriz(matriz, vector)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testinter_vect(self):
        vector1 = np.array([1+2j, 2, 3], dtype=complex)
        vector2 = np.array([4, 5, 6], dtype=complex)
        resultado_esperado = (32+8j)
        resultado_real = ev.inter_vect(vector1, vector2)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testnorma_vector(self):
        vector = np.array([1, 2, 3], dtype=complex)
        resultado_esperado = (3.7416573867739413)
        resultado_real = ev.norma_vector(vector)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testdistancia_vector(self):
        vector1 = np.array([1, -2], dtype=complex)
        vector2 = np.array([3, 4], dtype=complex)
        resultado_esperado = (6.324555320336759)
        resultado_real = ev.distancia_vector(vector1, vector2)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testmatriz_unitaria(self):
        matriz = np.array([[1, 0], [0, 1]])
        resultado_esperado = True
        resultado_real = ev.matriz_unitaria(matriz)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testmatriz_hermitania(self):
        matriz = np.array([[1, 2 + 3j], [2 - 3j, 4]])
        resultado_esperado = True
        resultado_real = ev.matriz_hermitania(matriz)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testproduct_tensor(self):
        matriz1 = np.array([[1, 2], [3, 4]])
        matriz2 = np.array([[0, 5], [6, 7]])
        resultado_esperado = ([[0, 5, 0, 10], [6, 7, 12, 14], [0, 15, 0, 20], [18, 21, 24, 28]])
        resultado_real = ev.product_tensor(matriz1, matriz2)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))


if __name__ == '__main__':
    unittest.main()
