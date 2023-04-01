import functions

class Boat:

    def __init__(self, size:int, player:str):
        """
        Initialize a new Boat instance with the given size and player.

        :param size: The size of the boat (i.e. the number of cells it occupies on the game board)
        :param player: The player who controls the boat

        Individual attributes:
            Lives, complete_location (list), contiguous (list), placing
        """
        self.size = size
        self.player = player
        self.lives = size
        self.complete_location = functions.random_boats_generator(size, self.player)
        self.contiguous = functions.list_of_contiguous(self.complete_location)
        self.placing = functions.boat_placing(self.complete_location, self.contiguous, self.player)

def boats_cpu():
    '''
    Function to create, validate and place all cpu boats in the board, through the boat class
    '''
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
    '''
    Function to create, validate and place all p1 boats in the board, through the boat class
    '''

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