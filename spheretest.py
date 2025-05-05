import unittest
import sphere

class sphereTest(unittest.TestCase):

    #these need to be updated for a sphere
    def test_volume1(self):
        assert(sphere.volume(1) == 4.1887902047863905)

    def test_volume2(self):
        assert(sphere.volume(10) == 4188.790204786391)

    def test_volume3(self):
        assert(sphere.volume(100) == 4188790.2047863905)


if __name__ == '__main__':
    unittest.main()
