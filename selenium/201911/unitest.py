import  unittest
#print help(unittest)

class IntegerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):  ## test method names begin 'test*'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

    def testDivide(self):
        result=7/2
        hope=3
        self.assertEqual(result,hope)


if __name__ == '__main__':
    unittest.main()