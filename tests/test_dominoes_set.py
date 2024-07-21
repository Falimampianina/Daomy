from unittest import TestCase

from data_structures.playables.dominoes_set import DominoesSet


class TestDominoesSet(TestCase):
    def test_create_set(self):
        self.assertEqual(len(DominoesSet().dominoes), 28)

    def test_unique_domino(self):
        dominoes_set = DominoesSet()
        for domino in dominoes_set.dominoes:
            self.assertTrue(dominoes_set.dominoes.count(domino) == 1)
