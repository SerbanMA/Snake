import copy
import random

class Service(object):
    def __init__(self, table):
        self._table = table

    def get_table(self):
        return self._table
    
    def move(self, n):
        head = self._table.get_snake()[0]
        facing = self._table.get_facing()

        # for every speps
        for i in range (1, n+1):
            x = head[0] + i*facing[0]
            y = head[1] + i*facing[1]
            # if the snake meets a '+' that means that snake entered into the barrier or in the his body so 'Game over!'
            if (self._table.get_map()[x][y] == '+'):
                return False
            
            # is the snakes meets a '.' that means an apple so we count it and add another one 
            if (self._table.get_map()[x][y] == '.'):
                self._table.set_apple_eaten(1)
                self._table.add_apple()

            # moving
            # if an apple was eaten the counter decrease and the body grow by one
            # otherwise just move
            if (self._table.get_apple_eaten() == 1):
                self._table.set_apple_eaten(0)
            else:
                pos = self._table.get_snake().pop()
                self._table._map[pos[0]][pos[1]] = ' '

            self._table.get_snake().insert(0, [x, y])
            # print the snake on the map
            self._table.put_snake()

        return True
        

    def move_side(self, x):
        facing = self._table.get_facing()

        # set facing of the snake
        if ( x == 'up'):
            if facing == [1, 0]:
                raise Exception('Snake cannot return by 180 degrees! ')
            if facing == [-1, 0]:
                raise Exception('Snake already goes up! ')
            self._table.set_facing([-1, 0])
            
        elif ( x == 'down'):
            if facing == [-1, 0]:
                raise Exception('Snake cannot return by 180 degrees! ')
            if facing == [1, 0]:
                raise Exception('Snake already goes down! ')
            self._table.set_facing([1, 0])

        elif ( x == 'left'):
            if facing == [0, 1]:
                raise Exception('Snake cannot return by 180 degrees! ')
            if facing == [0, -1]:
                raise Exception('Snake already goes left! ')
            self._table.set_facing([0, -1])

        elif ( x == 'right'):
            if facing == [0, -1]:
                raise Exception('Snake cannot return by 180 degrees! ')
            if facing == [0, 1]:
                raise Exception('Snake already goes right! ')
            self._table.set_facing([0, 1])

        else:
            raise Exception('Invalid command! ')
        
        # move 1 step in the direction he's facing
        return self.move(1)
        
