import numpy as np
import random
import classes
import functions
import variables

print("BATTLESHIP: Raymond's version")
print("Boats are created randomly (both player and cpu)")
print("You will be asked for a value in the axis x and y between 0 and 9 to shoot. Insert ONLY INTEGERS")
print("If you are right, you will keep the turn, if you are not, machine will randomly attack your boats")
classes.boats_cpu()
classes.boats_p1()

while variables.cpu_lives > 0 and variables.p1_lives > 0:
    while variables.Turn == True:
        functions.shoot(int(input("Introduce coordinate x")), (int(input("Introduce coordinate y"))), variables.cpu_board_boats, variables.p1_board_shots, "p1")
    while variables.Turn == False:
        functions.shoot((random.randint(0,9)), (random.randint(0,9)), variables.p1_board_boats, variables.p1_board_shots, "cpu")