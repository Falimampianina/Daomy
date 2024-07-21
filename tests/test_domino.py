from unittest import TestCase

from data_structures.playables.domino import Domino


class TestDomino(TestCase):
    def test_domino(self):
        with self.assertRaises(ValueError):
            Domino(7, 7)

    def test_equivalence(self):
        self.assertEqual(Domino(1, 3), Domino(3, 1))

    def test_reverse(self):
        self.assertEqual(str(Domino(1, 2)), str(Domino(2, 1).reverse()))

    def test_is_a_double(self):
        self.assertTrue(Domino(1, 1).is_a_double())

    def test_get_weight(self):
        self.assertEqual(Domino(6, 6).get_weight(), 12)
