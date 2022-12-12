def list_of_contiguous(random_boat):

    contiguous = []
    for spot in random_boat:
        for dx, dy in [(1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1), (-1, 0), (0, 1), (0, -1), (0, 0)]:
            nx, ny = spot[0] + dx, spot[1] + dy
            if nx >= 0 and nx < size and ny >= 0 and ny < size:
                if (nx,ny) in contiguous:
                    continue
                else:
                    contiguous.append((nx, ny))
    return contiguous

def random_boats_generator(size, player):
    random_boat = []

    while len(random_boat) < size:
        random_row = random.randint(0,9)
        random_column = random.randint(0,9)
        orien = random.choice(["North", "South", "East", "West"])
        random_boat.append((random_row, random_column))
        if size == 1:
            if player == "p1":
                for spot in list_of_contiguous(random_boat):
                    if p1_board_boats[spot] == "O":
                        random_boat.clear()
                        continue

            if player == "cpu":
                for spot in list_of_contiguous(random_boat):
                    if cpu_board_boats[spot] == "O":
                        random_boat.clear()
                        continue
                    
        while random_boat != [] and len(random_boat) != size:
            if orien == "North":
                random_row = random_row - 1
            if orien == "South":
                random_row = random_row + 1
            if orien == "East":
                random_column = random_column + 1
            if orien == "West":
                random_column = random_column - 1
            random_boat.append((random_row, random_column))
            if random_row >= 10 or random_column >= 10 or random_row <= 0 or random_column <= 0:
                random_boat.clear()
                continue
            
            if player == "p1":
                for spot in list_of_contiguous(random_boat):
                    if p1_board_boats[spot] == "O":
                        random_boat.clear()
                        continue

            if player == "cpu":
                for spot in list_of_contiguous(random_boat):
                    if cpu_board_boats[spot] == "O":
                        random_boat.clear()
                        continue
    if player == "p1":
        p1_boats_list.append(random_boat)
    elif player == "cpu":
        cpu_boats_list.append(random_boat)
    return random_boat

def boat_placing(complete_location, contiguous, player):
    if player == "p1":
        for spot in complete_location:
            p1_board_boats[spot] = "O"                
        return p1_board_boats

    if player == "cpu":
        for spot in complete_location:
            cpu_board_boats[spot] = "O"                
        return cpu_board_boats

def boats_cpu():

    boat1 = Boat(4, "cpu")
    boat2 = Boat(3, "cpu")
    boat3 = Boat(3, "cpu")
    boat4 = Boat(2, "cpu")
    boat5 = Boat(2, "cpu")
    boat6 = Boat(2, "cpu")
    boat7 = Boat(1, "cpu")
    boat8 = Boat(1, "cpu")
    boat9 = Boat(1, "cpu")
    boat10 = Boat(1, "cpu")

    boat10.placing



def boats_p1():

    boat11 = Boat(4, "p1")
    boat12 = Boat(3, "p1")
    boat13 = Boat(3, "p1")
    boat14 = Boat(2, "p1")
    boat15 = Boat(2, "p1")
    boat16 = Boat(2, "p1")
    boat17 = Boat(1, "p1")
    boat18 = Boat(1, "p1")
    boat19 = Boat(1, "p1")
    boat20 = Boat(1, "p1")

    boat20.placing


def shoot(spot, board, shooter):
    global cpu_lives
    global p1_lives
    if board[spot] == "O":
        print("Hit!")
        board[spot] = "X"
        if shooter == "cpu":
            p1_lives = p1_lives - 1
            if p1_lives == 0:
                print("No boats left, game over!")
        elif shooter == "p1":
            cpu_lives = cpu_lives - 1
            print(cpu_lives)
            if cpu_lives == 0:
                print("Your opponent has no botas, you won!")
            
    elif board[spot] == " ":
        print("Water")
        board[spot] = "-"
    return board, cpu_lives, p1_lives