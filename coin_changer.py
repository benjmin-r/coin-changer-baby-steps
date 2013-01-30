import unittest

def coin_change(amount, coins):
    return coins

class TestCoinChanger(unittest.TestCase):
    def test_pass(self):
        pass

    def test_one(self):
        self.assertEquals(coin_change(1, [1]), [1])


if __name__ == '__main__':
    unittest.main()
