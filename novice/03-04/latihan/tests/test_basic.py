import unittest

class TestBasic(unittest.TestCase):
    def setUp(self):
        self.app = App(database='fixtures/test_basic.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 100)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=10)
        self.assertEqual(customer.name, "Org XYZ")
        self.assertEqual(customer.address, "10 Red Road, Reading")

class TesComplexData(unittest.TestCase):
    def setUp(self):
        self.app = App(database='fixtures/test_complex.json')
    
    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 10000)
    
    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=9999)
        self.assertEqual(customer.name, u"sffd")
        self.assertEqual(customer.address, "10 Red Road, tokyo")

if __name__ == '__main__':
    unittest.main()