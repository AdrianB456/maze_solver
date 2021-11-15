# maze_solver

## Idea
The idea of this AI is to be able to solve a map no matter what dimesions and positions it has (except the absolut impossible ones). It uses a vanilla Q learning algorithm to solve each map in an optimal way.

## Installation

To install this AI you need to have the following requiremenets:

- Python 3.9.*
- Pygame 2.0.0
- Numpy 1.20.1
- Matplotlib 3.4.3

## How to use it.

You simply have to run main.py and add the name of the map (without the extension '.pkl') and let the AI train, once it's finished a graph should pop up to show the progress of the AI, and by closing the graph and pressing the enter button it will show you the sollution of the map (all the maps are in a folder named 'maps'). It also comes with a map creator (create_maps.py) this is how you use it:

First you run the file and add the name of the map, then you use the left button to of your mouse to create walls and the right one to delete them. If you want to edit the map even more you can change the sizes and the positions of each object by editing the file in specific variables (python knowledge is required).
