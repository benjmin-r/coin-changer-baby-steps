import unittest

def coin_change(amount, coins):
    if amount != coins[0]:
        return [amount / coins[0]]
    return coins

class TestCoinChanger(unittest.TestCase):
    def test_pass(self):
        pass

    def test_one(self):
        self.assertEquals(coin_change(1, [1]), [1])

    def test_two(self):
        self.assertEquals(coin_change(2, [1]), [2])


if __name__ == '__main__':
    unittest.main()
