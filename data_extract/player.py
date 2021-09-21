from datetime import datetime

"""
    Player data model
"""

class Pace(object):
    base = int()
    accelaration = int()
    speed = int()
    def __str__(self):
        return("Pace: %s\n\taccelaration: %s\tspeed: %s"%(self.base, self.accelaration, self.speed))

class Shooting(object):
    base = int()
    positioning = int()
    finishing = int()
    power = int()
    long  = int()
    volley = int()
    penalty = int()
    
    def __str__(self):
        return("Shooting: %s\n\tPositioning: %s\tFinishing: %s\tPower: %s\n\tLong: %s\tVolley: %s\tPenalty: %s"%(
            self.base,self.positioning,self.finishing,self.power,self.long,self.volley,self.penalty))

class Passing(object):
    base = int()
    vision = int()
    crossing = int()
    freekick = int()
    short = int()
    long = int()
    curve = int()
    def __str__(self):
        return("Passing: %s\n\tVision: %s\tCrossing: %s\tFreekick: %s\n\tShort: %s\tLong: %s\tCurve: %s"%(
            self.base,self.vision,self.crossing,self.freekick,self.short,self.long,self.curve))

class Dribbling(object):
    base = int()
    agility = int()
    balance = int()
    reaction = int()
    control = int()
    dribbling = int()
    composure = int()
    def __str__(self):
        return("Dribbling: %s\n\tAgility: %s\tBalance: %s\tReaction: %s\n\tControl: %s\tDribbling: %s\t Composure: %s"%(
            self.base,self.agility,self.balance,self.reaction,self.control,self.dribbling,self.composure))


class Defending(object):
    interception = int()
    heading = int()
    awarness = int()
    standing = int()
    sliding = int()
    def __str__(self):
        return("Defending: %s\n\tInterception: %s\tHeading: %s\tAwareness: %s\n\tStanding tackle: %s\tSlideing tackle: %s"%(
            self.base,self.interception,self.heading,self.awarness,self.standing,self.sliding))


class Physicality(object):
    jumping = int()
    stamina = int()
    strength = int()
    aggression = int()
    def __str__(self):
        return("Physicality: %s\n\tJumping: %s\tStamina: %s\n\tStrength: %s\tAggression: %s"%(
            self.base,self.jumping,self.stamina,self.strength,self.aggression))

    
class Rating(object):
    base = int()
    pace = Pace()
    shooting = Shooting()
    passing =  Passing()
    dribbling = Dribbling()
    defending = Defending()
    physicality = Physicality()
    def __str__(self):
        return ("PLAYER RATING: %s\n%s\n%s\n%s\n%s\n%s\n%s"%(
            self.base, self.pace, self.shooting, self.passing, self.dribbling, self.defending, self.physicality))

class Player(object):
    name = str()
    
    club = str()
    nation = str() 
    league = str() 
    
    sf = int() # skill foot
    wf = int() # weak foot 
    ir = int() # international reputation 
    
    foot = str() 
    height = float()
    weight = float()
    version = str()
    
    def_wr = str()
    att_wr = str()
    
    added_on = datetime(10,10,10)
    real_face = bool()
    body_type = str()
    age = str()
    
    rating = Rating()
    
    href = str()
    pid = int()
    
    def __str__(self):
        return("PLayer name: %s\nClub: %s\tNation: %s\tLeague: %s\nSkill foot: %s\tWeak foot: %s\tFoot: %s"\
               "\tInterational rep: %s\nHeight: %s cm\tWeight: %s kg\nDef WR: %s\tAtt WR: %s\nVersion: %s\tAdded on: %s\n"\
                "Real Face:%s\tBody type: %s\tAge: %s\nLink: %s\t Id: %s\n%s"%(
                self.name,self.club,self.nation,self.league,self.sf,self.wf,self.foot,self.ir,self.height,self.weight,
                self.def_wr,self.att_wr,self.version,self.added_on,self.real_face,self.body_type,self.age,
                self.href, self.pid, self.rating))