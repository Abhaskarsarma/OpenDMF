class Droplet:

    """
    Represents one droplet.
    """

    def __init__(self,
                 droplet_id,
                 row,
                 col,
                 volume=1.0):

        self.id = droplet_id
        self.row = row
        self.col = col
        self.volume = volume
        self.temperature = 25.0
        self.path = [(row, col)]
        self.distance = 0

    def move_to(self, row, col):

        self.row = row
        self.col = col
        self.path.append((row, col))
        self.distance += 1