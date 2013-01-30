import unittest

def coin_change(amount, coins):
    if amount != reduce(lambda c1, c2: c1 + c2, coins):
        return [amount / reduce(lambda c1, c2: c1 + c2, coins)]
    return coins

class TestCoinChanger(unittest.TestCase):
    def test_pass(self):
        pass

    def test_one(self):
        self.assertEquals(coin_change(1, [1]), [1])

    def test_two(self):
        self.assertEquals(coin_change(100, [50]), [2])


if __name__ == '__main__':
    unittest.main()
