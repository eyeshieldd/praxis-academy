
import unittest

def tambah(x, y): #mendeklarasikan method tambah 
    return x + y


def kurang(x, y):
    return x - y


class TestCalc(unittest.TestCase):

    def test_tambah(self):
        self.assertEqual(tambah(10, 5), 15) #membandingkan dengan operasi tambah, apakah 10+5 = 15
        self.assertEqual(tambah(-1, 1), 0)
        self.assertEqual(tambah(-1, -1), -2)

    def test_kurang(self):
        self.assertEqual(kurang(10, 5), 5)
        self.assertEqual(kurang(-1, 1), -2)
        self.assertEqual(kurang(-1, -1), 0)


if __name__ == '__main__':
    unittest.main()