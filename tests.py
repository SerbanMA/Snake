from domain import Table
from service import Service

class Tests():
    def __init__(self):
        pass

    def test_fire(self):
        table = Table()
        service = Service(table)

        ships = service.get_table().get_ships()
        assert(service.fire(ships[0][0], ships[0][1]) == True)
        assert(service.get_table().get_ships()[0][0] == -1)

        ships = service.get_table().get_ships()
        assert(service.fire(ships[1][0], ships[1][1]) == True)
        assert(service.get_table().get_ships()[1][0] == -1)

        if service.fire(1, 1) == False:
            assert(service.get_table().get_map()[1][1] == '*')
        else:
            assert(service.get_table().get_map()[1][1] == '-')




if __name__ == "__main__":
    test = Tests()
    test.test_fire()