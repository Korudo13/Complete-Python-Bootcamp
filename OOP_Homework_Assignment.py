'''
Problem 1:

Fill in the Line class methods to accept coordinate as a pair of tuplesand return the slope and distance of the line
'''

class Line(object):

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1  # unpack tuple coordinate1 (10,2) into separate variables x1, y1
        x2,y2 = self.coor2
        return ((x2-x1)**2) + ((y2-y1)**2)**0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return float ((y2-y1)/(x2-x1)) # avoiding inaccurate rounding to nearest integer

coordinate1 = (10,2)
coordinate2 = (5,8)

li = Line(coordinate1,coordinate2)
print li.distance()
print li.slope()
