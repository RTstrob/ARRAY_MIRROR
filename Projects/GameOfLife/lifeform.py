from abc import abstractmethod


class Lifeform:
    def __init__(self, is_alive: bool, symbol: str) -> None:
        self._is_alive = is_alive
        self._symbol = symbol

    @property
    def is_alive(self) -> bool:
        return self._is_alive

    @is_alive.setter
    def is_alive(self, is_alive: bool) -> None:
        self._is_alive = is_alive

    @property
    def symbol(self):
        pass

    @symbol.setter
    def symbol(self, symbol: str) -> None:
        self.symbol = symbol

    @abstractmethod
    def evolve(self, number_of_neighbors: int) -> None:
        pass

    def __str__(self):
        return self._symbol if self.is_alive else ' '

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Lifeform):
            return False

        return self.is_alive == __value.is_alive and self.symbol == __value.symbol