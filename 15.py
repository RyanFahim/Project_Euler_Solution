#To move from the top left corner of an n×n grid to the opposite one you have to move n
#  times to the right and n times down. So in total you will do 2n moves. 
# If you could make those in any order there would be (2n)! ways of doing them. 
# But you don't have that freedom, because the order within the movements to the right and within the movements
#  down is fixed, e.g. you have to move from row 4 to row 5 before you can move from row 5 to row 6. So of the n! ways the 
# movements to the right can be ordered, only one is valid, and similarly with the movements down.
#Summing it all up, the closed form answer to that problem is:
#(2n)!n!n!

import math

def Lattice_path(grid_size):
    path = math.factorial(grid_size*2) / (math.factorial(grid_size) ** 2 )
    return path

n = Lattice_path(20)
print("%s" % (n))
