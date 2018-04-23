

class Mission( object ):
    def __init__( self, name, number, desc ):
        self.name = name
        self.number = number
        self.description = desc
        self.sectors = []


class Sector( object ):
    START_4_SOLDIERS  = "Start with 4 Soldiers"
    REQUIRE_SCOUT     = "Scout Required"
    REQUIRE_CORPORAL  = "Corporal Required"
    LOSE_SPECIALIST   = "Lose Specialist"
    LOSE_MEDIC        = "Lose Medic"
    GAIN_SCOUT        = "Gain Scout"
    GAIN_SHARPSHOOTER = "Gain Sharpshooter"
    MAX_1_UNIT        = "Max 1 Unit"
    GAIN_COURAGE      = "Gain 1 Courage Per Roll"
    GAIN_STAR         = "Gain 1 Star Per Roll"
    GAIN_TOOL         = "Gain 1 Tool Per Roll"
    GAIN_1D6_SOLDIERS = "Gain 1d6 Soldiers on Arrival"
    MACHINE_GUN       = "Machine Gun"
    MACHINE_GUN_LOSE_SPECIALIST = "Machine Gun: Lose Specialist on 6"
    MAX_1_TURN        = "Max 1 Turn"
    NO_DICE_LOCKED    = "No Dice Locked"
    ROLL_5_DICE       = "Roll Only 5 Dice"
    NO_ITEMS_FOUND    = "No Items Found"

    def __init__( self, number, defense, attrs=[], bunker=False, start=False ):
        self.number = number
        self.defense = defense
        self.neighbors = {}  # { number: Threshold }
        self.attributes = attrs  # required specialists, dice modifiers, lost specialists, unit limitations, etc.
        self.bunker = bunker


    def add_neighbor( self, sector1, sector2, threshold ):
        sector1.neighbors[ sector2 ] = threshold
        sector2.neighbors[ sector1 ] = threshold


class Threshold( object ):
    def __init__( self, courage=0, landmines=False, barrier=False ):
        self.courage = courage
        self.landmines = landmines
        self.barrier = barrier

