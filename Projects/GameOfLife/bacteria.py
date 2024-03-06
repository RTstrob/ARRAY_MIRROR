from Projects.GameOfLife.lifeform import Lifeform


class Bacteria(Lifeform):
    def __init__(self, is_alive: bool) -> None:
        super().__init__(is_alive, 'X')

    def evolve(self, number_of_neighbors: int) -> None:
        #implement rules based on number of neighbors
        #decide whether this bacteria lives or dies
        pass