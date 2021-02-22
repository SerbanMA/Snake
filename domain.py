import random

class Table (object):
    def __init__(self, DIM, apple_count):
        self._map = []
        self._snake = []
        self._facing = [-1, 0]
        # (-1,  0) N
        # ( 1,  0) S
        # ( 0 , 1) E
        # ( 0, -1) W  
        self._apple_eaten = 0
        self._DIM = DIM
        self._apple_count = apple_count

        #_____ create the map _____
        for i in range (self._DIM+2):
            self._map.append([])
            for j in range (self._DIM+2):
                self._map[i].append(' ')
                j = j

        for i in range (self._DIM+2):
            for j in range (self._DIM+2):
                if (i == 0 or i == self._DIM + 1 or j == 0 or j == self._DIM + 1):
                    self._map[i][j] = '+'
                        
        #_____ create the snake _____  
        self._snake.append([self._DIM//2, self._DIM//2+1])
        self._snake.append([self._DIM//2+1, self._DIM//2+1])
        self._snake.append([self._DIM//2+2, self._DIM//2+1])
        self.put_snake()

        

        #_____ place the apples _____
        for i in range (self._apple_count):
            self.add_apple()

    def put_snake(self):
            for i in self._snake:
                self._map[i[0]][i[1]] = '+'
            self._map[self._snake[0][0]][self._snake[0][1]] = '*'

    def __str__(self):
        string = '+---'*(self._DIM) + '+\n'
        for i in range (1, self._DIM+1):
            string += '| '
            for j in range (1, self._DIM+1):
                string += str(self._map[i][j]) + ' | '
            string += '\n' + '+---'*(self._DIM) + '+\n'
        return string

    def get_map(self):
        return self._map

    def get_snake(self):
        return self._snake

    def get_facing(self):
        return self._facing

    def set_facing(self, facing):
        self._facing = facing  

    def get_apple_eaten(self):
        return self._apple_eaten

    def set_apple_eaten(self, x):
        self._apple_eaten = x

    def add_apple(self):
        def valid_apple (x, y):
            if self._map[x-1][y] != '.' and self._map[x][y-1] != '.' and self._map[x][y] == ' ' and self._map[x][y+1] != '.' and self._map[x+1][y] != '.':
                        return True
            return False
        
        x = random.randint(1, self._DIM)
        y = random.randint(1, self._DIM)

        # here should be correct:
        # while not valid_apple(x, y):
        #    x = random.randint(1, self._DIM)
        #    y = random.randint(1, self._DIM)
        #self._map[x][y] = '.'
        # but after a while it is possible to not be able to add another apple, so an for is better for not infinite looping

        i = 1
        while i < 1000:
            if  valid_apple(x, y):
                self._map[x][y] = '.'
                return
            else:
                x = random.randint(1, self._DIM)
                y = random.randint(1, self._DIM)
            i += 1

