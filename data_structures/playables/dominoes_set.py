from data_structures.playables.domino import Domino


class DominoesSet:
    def __init__(self):
        self.dominoes = []
        self.create_set()

    def create_set(self):
        dominoes_pairs = [(x, y) for x in range(0, 7) for y in range(x, 7)]
        for x, y in dominoes_pairs:
            self.dominoes.append(Domino(x, y))

    def __str__(self):
        output = ""
        for domino in self.dominoes:
            output += str(domino) + "\n"
        return output

    @property
    def dominoes(self) -> list[Domino]:
        return self._dominoes

    @dominoes.setter
    def dominoes(self, dominoes: list[Domino]):
        self._dominoes = dominoes


if __name__ == '__main__':
    example = DominoesSet()
    print(example)
