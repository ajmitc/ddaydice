from mission import *

class ExerciseTiger( Mission ):
    def __init__( self, "Exercise Tiger", 1, "Slapton Sands, England.  April 27th, 1944. 0819." )
        sector1  = Sector(  1,  2, [ Sector.START_4_SOLDIERS ], start=True )
        sector2  = Sector(  2,  4, [ Sector.GAIN_SCOUT, Sector.GAIN_COURAGE ] )
        sector3  = Sector(  3,  4, [ Sector.GAIN_SHARPSHOOTER, Sector.GAIN_STAR ] )
        sector4  = Sector(  4,  6, [ Sector.MAX_1_TURN ] )
        sector5  = Sector(  5,  3, [ Sector.REQUIRE_CORPORAL, Sector.GAIN_TOOL, Sector.MACHINE_GUN] )
        sector6  = Sector(  6,  6, [ Sector.MAX_1_TURN ] )
        sector7  = Sector(  7,  8, [ Sector.LOSE_SPECIALIST, Sector.MACHINE_GUN, Sector.NO_DICE_LOCKED] )
        sector8  = Sector(  8,  8, [ Sector.MACHINE_GUN, Sector.ROLL_5_DICE ] )
        sector9  = Sector(  9, 10, [ Sector.NO_ITEMS_FOUND, Sector.MACHINE_GUN ] )
        sector10 = Sector( 10, 10, [ Sector.LOSE_SPECIALIST, Sector.MACHINE_GUN, Sector.GAIN_1D6_SOLDIERS ] )
        bunker   = Sector(  0, 12, [ Sector.MACHINE_GUN ], bunker=True )

        self.sectors = [ sector1, sector2, sector3, sector4, sector5, sector6, sector7, sector8, sector9, sector10, bunker ]

        # Thrsholds
        self.add_neighbor( sector1, sector2, Threshold( 1 ) )
        self.add_neighbor( sector1, sector3, Threshold( 1 ) )
        self.add_neighbor( sector2, sector3, Threshold( landmines=True ) )
        self.add_neighbor( sector2, sector4, Threshold( 2 ) )
        self.add_neighbor( sector2, sector5, Threshold( 2 ) )
        self.add_neighbor( sector3, sector5, Threshold( 2 ) )
        self.add_neighbor( sector3, sector6, Threshold( 2 ) )
        self.add_neighbor( sector4, sector5, Threshold() )
        self.add_neighbor( sector4, sector7, Threshold( 2 ) )
        self.add_neighbor( sector5, sector6, Threshold() )
        self.add_neighbor( sector5, sector7, Threshold( 2, landmines=True ) )
        self.add_neighbor( sector5, sector8, Threshold( 2, landmines=True ) )
        self.add_neighbor( sector6, sector8, Threshold( 2 ) )
        self.add_neighbor( sector7, sector8, Threshold() )
        self.add_neighbor( sector7, sector9, Threshold( 3, landmines=True ) )
        self.add_neighbor( sector8, sector10, Threshold( 3, landmines=True ) )
        self.add_neighbor( sector9, sector10, Threshold() )
        self.add_neighbor( sector9,  bunker, Threshold( 4 ) )
        self.add_neighbor( sector10, bunker, Threshold( 4 ) )

