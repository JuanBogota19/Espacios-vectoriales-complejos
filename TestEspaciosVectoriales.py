import EspaciosVectoriales as ev
import numpy as np
import unittest

class TestCplxOperations(unittest.TestCase):

    def testsuma_vec(self):
        a = np.array([[1,2,3]], dtype=complex)
        b = np.array([[1,2,3]], dtype=complex)
        e = [[2.+0.j,4.+0.j,6.+0.j]]
        self.assertAlmostEqual(ev.suma_vect(a,b),e)




if __name__ == '__main__':
    unittest.main()
