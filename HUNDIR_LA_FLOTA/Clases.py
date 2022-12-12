class Boat:

    def __init__(self, size:int, player:str):
        self.size = size
        self.player = player
        self.lives = size
        self.complete_location = random_boats_generator(size, self.player)
        self.contiguous = list_of_contiguous(self.complete_location)
        self.placing = boat_placing(self.complete_location, self.contiguous, self.player)
