import numpy as np
import random
import variables

def list_of_contiguous(random_boat):
    '''
    This function takes the previously generated boat and returns a list with all the contiguous locations of it.
    The list includes the boat locations too.
    '''
    contiguous = []
    for spot in random_boat: #For each spot coordinates, we add the values on the tuples to get the contiguous
        for dx, dy in [(1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1), (-1, 0), (0, 1), (0, -1), (0, 0)]:
            nx, ny = spot[0] + dx, spot[1] + dy
            if nx >= 0 and nx < variables.size and ny >= 0 and ny < variables.size: #To avoid including spots out of the board
                if (nx,ny) in contiguous: 
                    continue #Some of the contiguous values will be repeated, so we avoid that with this if
                else:
                    contiguous.append((nx, ny))
    return contiguous

def random_boats_generator(size, player):
    '''
       Function that creates new boats of a specified size and validates them in their board 
    '''
    random_boat = []

    while len(random_boat) < size:   #Inicialize a new boat with random values: first spot (column and row), and orientation
        random_row = random.randint(0,9)
        random_column = random.randint(0,9)
        orien = random.choice(["North", "South", "East", "West"])
        random_boat.append((random_row, random_column))
        if size == 1:    #To make the whole loop work, separated boats of size = 1 in this condition
            if player == "p1":
                for spot in list_of_contiguous(random_boat):
                    if variables.p1_board_boats[spot] == "O":
                        random_boat.clear() #If any spot in the list of contiguous is in the board, the random boat restarts
                        continue

            if player == "cpu":
                for spot in list_of_contiguous(random_boat):
                    if variables.cpu_board_boats[spot] == "O":
                        random_boat.clear()  #If any spot in the list of contiguous is in the board, the random boat restarts
                        continue
                    
        while random_boat != [] and len(random_boat) != size:
            if orien == "North": #To create the new boat according to the orientation
                random_row = random_row - 1
            if orien == "South":
                random_row = random_row + 1
            if orien == "East":
                random_column = random_column + 1
            if orien == "West":
                random_column = random_column - 1
            random_boat.append((random_row, random_column))
            if random_row >= 10 or random_column >= 10 or random_row <= 0 or random_column <= 0:
                random_boat.clear() #Restart the boat if any axis of the new spot is above 10 or under 0
                continue
            
            if player == "p1":
                for spot in list_of_contiguous(random_boat):
                    if variables.p1_board_boats[spot] == "O":
                        random_boat.clear()
                        continue #Restart the boat if any spot in list of contiguous is already a boat in board

            if player == "cpu":
                for spot in list_of_contiguous(random_boat):
                    if variables.cpu_board_boats[spot] == "O":
                        random_boat.clear() #Restart the boat if any spot in list of contiguous is already a boat in board
                        continue
    if player == "p1":
        variables.p1_boats_list.append(random_boat)
    elif player == "cpu":
        variables.cpu_boats_list.append(random_boat)
    return random_boat

def boat_placing(complete_location, contiguous, player):
    '''
    Places the new boat in the board depending on the player, replacing the empty space for an "O" in the index of the Np.array
    '''
    if player == "p1":                          #Places the new boat in the board depending on the player
        for spot in complete_location:
            variables.p1_board_boats[spot] = "O"                
        return variables.p1_board_boats

    if player == "cpu":
        for spot in complete_location:
            variables.cpu_board_boats[spot] = "O"                
        return variables.cpu_board_boats


def shoot(x, y, board, board2, shooter):
    '''
    Function that allows both players to shoot one spot of the opponent's board.
    If the shot hits a boat, the player who did it keeps the turn. Otherwise, it will change.
    Will print the both shots and boats board in each turn
    '''
    variables.cpu_lives
    variables.p1_lives
    if board[(x,y)] == "O":
        print("Hit!")
        board[(x,y)] = "X" #If the given coordinates are part of a boat in the map, changes it "O", into "X"
        if shooter == "cpu":
            variables.p1_lives = variables.p1_lives - 1 #Opponent loses a life after each right shot
            print("Mis barcos")
            print(board)
            print("Disparos")
            print(board2)
            if variables.p1_lives == 0:
                print("No boats left, game over!")
        elif shooter == "p1":
            board2[(x,y)] = "X"
            print("Mis barcos")
            print(variables.p1_board_boats)
            print("Disparos")
            print(board2)
            variables.cpu_lives = variables.cpu_lives - 1
            print(variables.cpu_lives)
            if variables.cpu_lives == 0:
                print("Your opponent has no boats, you win!")
            
    elif board[(x,y)] == " ":
        print("Water")
        board[(x,y)] = "-" #If the given coordinates are not part of a boat in the map, changes it " ", into "-"
        variables.Turn = not variables.Turn
        if shooter == "cpu":
            print("Mis barcos")
            print(board)
            print("Disparos")
            print(board2)
            return variables.Turn, board, variables.cpu_lives, variables.p1_lives
        if shooter == "p1":
            board2[(x,y)] = "-"
            print("Mis barcos")
            print(variables.p1_board_boats)
            print("Disparos")
            print(board2)
            return variables.Turn, board, board2, variables.cpu_lives, variables.p1_lives
    return variables.Turn, board, variables.cpu_lives, board2, variables.p1_lives