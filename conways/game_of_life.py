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
import csv
import os
import sys


os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__))))

def plant_seed(seed, state, pos):
    seeds = {
            'block':'block.csv',
            'eater':'eater.csv',
            'beehive':'beehive.csv',
            'loaf':'loaf.csv',
            'boat':'boat.csv',
            'tub':'tub.csv',
            'blinker':'blinker.csv',
            'toad':'toad.csv',
            'beacon':'beacon.csv',
            'pulsar':'pulsar.csv',
            'pentadecathlon':'pentadecathlon.csv',
            'glider':'glider.csv',
            'lwss':'lwss.csv',
            'mwss':'mwss.csv',
            'hwss':'hwss.csv',
            'puffer_zipper':'puffer_zipper.csv',
            'r-pentomino':'r-pentomino.csv',
            'diehard':'diehard.csv',
            'acorn':'acorn.csv',
            'gosper':'gosper.csv',
            'simkin':'simkin.csv',
            'gosper-eater':'gosper-eater.csv',
            'tetrominoes':'tetrominoes.csv'
            }

    still_lifes = ['block', 'eater', 'beehive', 'loaf', 'boat', 'tub']
    oscillators = ['blinker', 'toad', 'beacon', 'pulsar', 'pentadecathlon']
    spaceships = ['glider', 'lwss', 'mwss', 'hwss', 'puffer_zipper']
    methuselahs = ['r-pentomino', 'diehard', 'acorn']
    guns = ['gosper', 'simkin']
    configs = ['gosper-eater', 'tetrominoes']

    if seed in still_lifes:
        pattern_file = os.getcwd() + '/patterns/still_lifes/' + seeds[seed]
    elif seed in oscillators:
        pattern_file = os.getcwd() + '/patterns/oscillators/' + seeds[seed]
    elif seed in spaceships:
        pattern_file = os.getcwd() + '/patterns/spaceships/' + seeds[seed]
    elif seed in methuselahs:
        pattern_file = os.getcwd() + '/patterns/methuselahs/' + seeds[seed]
    elif seed in guns:
        pattern_file = os.getcwd() + '/patterns/guns/' + seeds[seed]
    elif seed in configs:
        pattern_file = os.getcwd() + '/patterns/configs/' + seeds[seed]
    else:
        raise Exception(f'Seed "{seed}" is not implemented. Available seeds are {[i for i in seeds]}')
    
    with open (pattern_file, 'r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            state[int(row[0]) + pos[0], int(row[1]) + pos[1]] = 1
    

class Board(object):

    def __init__(self, size=(100, 100), seed='random', interval=0.1, initial_pos=(0,0)):

        if seed == 'random':
            self.state = np.random.randint(2, size = size)

        else:
            self.state = np.zeros(size)
            plant_seed(seed, self.state, pos=initial_pos)

        self.engine = Engine(self)
        self.iteration = 0
        self.interval = interval
        self.size = size


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
            
            plt.pause(self.interval)

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

    size = (59, 500)
    seed = 'puffer_zipper'
    interval=0.05
    pos = (15, 10)
    board = Board(size=size, seed=seed, interval=interval, initial_pos=pos)

    for _ in board.animate():
        pass
#-------------------------------------------------------------------------

if __name__ == '__main__':
    main()