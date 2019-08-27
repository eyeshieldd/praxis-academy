import unittest

class TestSum(unittest.TestCase):
	def tes_split(self):
		s = 'johan aji'
		self.assertEqual(s.split(), ['hello', 'johan'])
		with self.assertRaises(TypeError):
			s.split(1)

if __name__=='__main__':
	unittest.main()