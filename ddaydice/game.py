

class Game( object ):
    def __init__( self ):
        self.mission = None  # Omaha, Gold, Utah, etc
        self.players = []
        self.player_sector = {} # { Player: Sector }

        # global specialists and items.  Players have own list of specialists unique to them.
        self.available_specialists = []
        self.available_items = []

        # Variations
        self.available_soldier_mulligan = 0


    def reset( self ):
        self.mission = None
        self.players = []
        self.available_specialists = []
        self.available_items = []
        self.available_soldier_mulligan = 0

