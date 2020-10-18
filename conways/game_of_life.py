"""
Implementation of John CH. Conway's Game of Life.
Rules:
    - A dead cell with exactly three living neighbours becomes alive
    - A living cell with two or three living neighbours remains alive
    - In all other cases, the cell becomes (or remains) dead.
"""


#Import required library

import numpy as np
import matplotlib.pyplot as plt

import argparse
import time


class Board(object):

    def __init__(self, size=(100, 100), seed='Random'):

        if seed == 'Random':
            self.state = np.random.randint(2, size = size)

        self.engine = Engine(self)
        self.iteration = 0


    def animate(self):

        i = self.iteration
        im = None
        plt.title("Conway's Game of Life")

        while True:
            if i == 0:
                plt.ion()
                im = plt.imshow(self.state, vmin = 0, vmax = 2, cmap = plt.cm.gist_earth)

            else:
                im.set_data(self.state)

            i += 1
            self.engine.applyRules()

            print('Life Cycle: {} Birth: {} Survive: {}'.format(i, self.engine.nBirth, self.engine.nSurvive))
            
            plt.pause(0.05)

            yield self


class Engine(object):

    def __init__(self, board):

        self.state = board.state
    
    
    def countNeighbors(self):
        state = self.state

        # Create matrix of neighbours
        n = (state[0:-2,0:-2] + state[0:-2,1:-1] + state[0:-2,2:] +
            state[1:-1,0:-2] + state[1:-1,2:] + state[2:,0:-2] +
            state[2:,1:-1] + state[2:,2:])

        return n
   
   
    def applyRules(self):

        n = self.countNeighbors()
        state = self.state
        birth = (n == 3) & (state[1:-1,1:-1] == 0) # Dead cell surrounded by 3 alive cells.
        survive = ((n == 2) | (n == 3)) & (state[1:-1,1:-1] == 1) # Alive cell surrounded by 2 or 3 alive cells.
        state[...] = 0 # All elements to zero
        state[1:-1,1:-1][birth | survive] = 1 # Cells to 1 if birth or survive value of cell equal True
        nBirth = np.sum(birth)
        self.nBirth = nBirth
        nSurvive = np.sum(survive)
        self.nSurvive = nSurvive
        return state

#-------------------------------------------------------------------------

def main():
    size = (50, 50)
    seed = 'Random'
    board = Board(size=size, seed=seed)

    for _ in board.animate():
        pass
#-------------------------------------------------------------------------

if __name__ == '__main__':
    main()