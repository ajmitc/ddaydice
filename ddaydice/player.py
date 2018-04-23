

class Player( object ):
    GREEN = "Green"
    BLUE  = "Blue"
    RED   = "Red"
    TAN   = "Tan"

    def __init__( self, name ):
        self.name = name
        self.color = self.GREEN
        self.available_specialists = []
        self.specialists = []
        self.items = []
        self.soldiers = 0
        self.stars    = 0
        self.courage  = 0
        self.tools    = 0

