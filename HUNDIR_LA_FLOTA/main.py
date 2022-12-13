import numpy as np
import random
import Clases 
import Funciones
import Variables

print("BATTLESHIP: Raymond's version")
print("Boats are created randomly (both player and cpu)")
print("You will be asked for a value in the axis x and y between 0 and 9 to shoot. Insert ONLY INTEGERS")
print("If you are right, you will keep the turn, if you are not, machine will randomly attack your boats")
Clases.boats_cpu()
Clases.boats_p1()

while Variables.cpu_lives > 0 and Variables.p1_lives > 0:
    while Variables.Turn == True:
        Funciones.shoot(int(input("Introduce coordinate x")), (int(input("Introduce coordinate y"))), Variables.cpu_board_boats, Variables.p1_board_shots, "p1")
    while Variables.Turn == False:
        Funciones.shoot((random.randint(0,9)), (random.randint(0,9)), Variables.p1_board_shots, "cpu")