import copy
import time
import random

from bacteria import Bacteria
from lifeform import Lifeform
from kbhit import KBHit

from datastructures.array2d import Array2D


class World:
    def __init__(self, size: int = 10, filename: str = ''):
        self._grid = self._initialize_grid(size, filename)

    def _initialize_grid(self, size: int, filename: str) -> Array2D:
        if filename != '':
            return self._build_grid_from_file(filename)
        
        grid = Array2D(size, size)

        for row in range(size):
            for col in range(size):
                is_alive = random.choice([True, False])
                grid[row][col] = Bacteria(is_alive=is_alive)

        return grid
    
    def print_current_grid(self) -> None:
        rows, cols = self._grid.dimensions
        for row in range(rows):
            for col in range(cols):
                print(self._grid[row][col], end=' ')
            print()

    def _build_grid_from_file(self, filename) -> Array2D: 
        return Array2D(0, 0)

    def run(self):
        #while loop that makes generations
        kb_hit = KBHit()

        generation = 0
        step = False

        while True:
            if self._reached_stable_state():
                print(f'Reached stable state after {generation} generations.')
                generation += 1

            self.print_current_grid()

            #generate next generation
            #check for stable or stagnant
            #archive current grid
            #replace current grid with next generation

            next_generation = copy.deepcopy(self._grid)

            rows, cols = next_generation.dimensions
            for row in range(rows):
                for col in range(cols):
                    neighbors = self._get_neighbors(row, col)
                    next_generation.evolve[row][col].evolve(neighbors)

            self._grid_history.append(self._grid)

            time.sleep(1)

            if step or kb_hit.kbhit():
                ch = kb_hit.getch()

                if ch == 's':
                    step = True
                    continue
                elif ch == 'c':
                    step = False
                    continue
                elif ch == 'q':
                    return
                else:
                    print('Invalid command.')
                

    def _get_neighbors(self, row: int, col: int) -> int:
        #count the neighbors
        raise NotImplementedError

def main():
    world = World()
    world.run()

if __name__ == '__main__':
    main()


# def main():
#     kb = KBHit()

#     print('Hit any key, or ESC to exit')

#     iteration = 0

#     while True:
        
#         print(f'In loop: {iteration}')
#         iteration += 1
#         time.sleep(1)

#         if kb.kbhit():
#             c = (kb.getch())
#             c_ord = ord(c)
#             print(c)
#             print(c_ord)
#             time.sleep(2)
#             if c_ord == 27:
#                 break
#             print(c)