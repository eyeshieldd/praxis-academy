import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.dictionary = ['fox', 'boss', 'orange', 'toes', 'fairy', 'cup']

    def test_in_one(self):
        self.assertIn('fox', self.dictionary)
        self.dictionary.remove('fox')

    def test_in_two(self):
        self.assertIn('fox', self.dictionary)

if __name__=='__main__':
  unittest.main()