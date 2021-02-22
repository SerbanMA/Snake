import re
import os

class UI(object):
    def __init__(self, service):
        self._service = service

    def run(self):
        print (self._service.get_table())
        while True:
            try:
                x = input ('>>> ')
                print ('\n')
                os.system('cls')
                
                # Command for move n steps!
                if re.match(r'move [0-9]+$', x):
                    X = x.split()
                    X = int(X[1])
                    
                    ok = self._service.move(X)
                    print(self._service.get_table())

                    if ok == False:
                        print('Game over!')
                        return 
                # Command for move 1 step!
                elif re.match(r'move$', x):
                    ok = self._service.move(1)
                    print(self._service.get_table())

                    if ok == False:
                        print('Game over!')
                        return 
                
                # Command for move side!
                elif re.match(r'up$', x):
                    ok = self._service.move_side(x)
                    print(self._service.get_table())

                    if ok == False:
                        print('Game over!')
                        return

                elif re.match(r'down$', x):
                    ok = self._service.move_side(x)
                    print(self._service.get_table())

                    if ok == False:
                        print('Game over!')
                        return 

                elif re.match(r'left$', x):
                    ok = self._service.move_side(x)
                    print(self._service.get_table())

                    if ok == False:
                        print('Game over!')
                        return 

                elif re.match(r'right$', x):
                    ok = self._service.move_side(x)
                    print(self._service.get_table())

                    if ok == False:
                        print('Game over!')
                        return 

                else:
                    print(self._service.get_table())
                    raise Exception('Invalid command! ')
                    
            except Exception as ex:
                print (str(ex))