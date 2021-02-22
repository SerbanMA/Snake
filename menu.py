from console import UI
from service import Service
from domain import Table
from settings import Settings
import os

if __name__=="__main__":
    # run the game
    print("Want to play?")
    print("[Yes] / [No]")
    print(" ")
    answer = input (">>> ")
    os.system("cls")

    while answer == "Yes":
        # here I take attribues from settings file
        settings = Settings('settings.properties')
        DIM = int(settings.get_dimension())
        apple_count = int(settings.get_apples())

        table = Table(DIM, apple_count)
        service = Service(table)
        console = UI(service)

        console.run()

        print("Want another turn?")
        print("[Yes] / [No]")
        print(" ")
        answer = input (">>> ")
        os.system("cls")
    