from unittest import TestCase
from logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(1, 2, '+')
        self.assertEqual(3, result)

    def test_plus(self):
        result = operations(1, 2, '-')
        self.assertEqual(-1, result)

    def test_plus(self):
        result = operations(1, 2, '*')
        self.assertEqual(2, result)

    def test_plus(self):
        result = operations(1, 2, '/')
        self.assertEqual(0.5, result)