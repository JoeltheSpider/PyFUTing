from player import Player, Rating, Pace, Shooting, Passing, Dribbling, Defending, Physicality
from datetime import datetime

class Maker():
    def make_pace(self, entity):
        pace = Pace()
        pace.base = int(entity[2*0].get_text().strip("\n "))
        pace.accelaration = int(entity[2*1].get_text().strip("\n "))
        pace.speed = int(entity[2*2].get_text().strip("\n "))
        return pace
    
    def make_shooting(self, entity):
        shooting = Shooting()
        shooting.base = int(entity[2*0].get_text().strip("\n "))
        shooting.positioning = int(entity[2*1].get_text().strip("\n "))
        shooting.finishing = int(entity[2*2].get_text().strip("\n "))
        shooting.power = int(entity[2*3].get_text().strip("\n "))
        shooting.long = int(entity[2*4].get_text().strip("\n "))
        shooting.volley = int(entity[2*5].get_text().strip("\n "))
        shooting.penalty = int(entity[2*6].get_text().strip("\n "))
        return shooting
    
    def make_passing(self, entity):
        passing = Passing()
        passing.base = int(entity[2*0].get_text().strip("\n "))
        passing.vision = int(entity[2*1].get_text().strip("\n "))
        passing.crossing = int(entity[2*2].get_text().strip("\n "))
        passing.freekick = int(entity[2*3].get_text().strip("\n "))
        passing.short = int(entity[2*4].get_text().strip("\n "))
        passing.long = int(entity[2*5].get_text().strip("\n "))
        passing.curve = int(entity[2*6].get_text().strip("\n "))
        return passing
    
    def make_dribbling(self, entity):
        dribbling = Dribbling()
        dribbling.base = int(entity[2*0].get_text().strip("\n "))
        dribbling.agility = int(entity[2*1].get_text().strip("\n "))
        dribbling.balance = int(entity[2*2].get_text().strip("\n "))
        dribbling.reaction =  int(entity[2*3].get_text().strip("\n "))
        dribbling.control = int(entity[2*4].get_text().strip("\n "))
        dribbling.dribbling = int(entity[2*5].get_text().strip("\n "))
        dribbling.composure = int(entity[2*6].get_text().strip("\n "))
        return dribbling
    
    def make_defending(self, entity):
        defending = Defending()
        defending.base = int(entity[2*0].get_text().strip("\n "))
        defending.interception = int(entity[2*1].get_text().strip("\n "))
        defending.heading = int(entity[2*2].get_text().strip("\n "))
        defending.awarness =  int(entity[2*3].get_text().strip("\n "))
        defending.standing = int(entity[2*4].get_text().strip("\n "))
        defending.sliding = int(entity[2*5].get_text().strip("\n "))
        return defending
    
    def make_physicality(self, entity):
        physicality = Physicality()
        physicality.base = int(entity[2*0].get_text().strip("\n "))
        physicality.jumping = int(entity[2*1].get_text().strip("\n "))
        physicality.stamina = int(entity[2*2].get_text().strip("\n "))
        physicality.strength =  int(entity[2*3].get_text().strip("\n "))
        physicality.aggression = int(entity[2*4].get_text().strip("\n "))
        return physicality
    
    def make_rating(self, page):
        rating = Rating()
        rating.pace =  self.make_pace(page[0].find_all(class_="stat_val"))
        rating.shooting = self.make_shooting(page[1].find_all(class_="stat_val"))
        rating.dribbling = self.make_dribbling(page[2].find_all(class_="stat_val"))
        rating.passing = self.make_passing(page[3].find_all(class_="stat_val"))
        rating.defending = self.make_defending(page[4].find_all(class_="stat_val"))
        rating.physicality = self.make_physicality(page[5].find_all(class_="stat_val"))
        return rating
    
    def make_player(self, page):
        """
        Gets a player's page and gives out a player object
        """
        player = Player()
        face = page.find("div",id="info_content").find_all("td")
        player.name = face[0].get_text().strip()
        player.club = face[1].get_text().strip()
        player.nation = face[2].get_text().strip()
        player.league = face[3].get_text().strip()
        player.sf = int(face[4].get_text().strip())
        player.wf = int(face[5].get_text().strip())
        player.ir = int(face[6].get_text().strip())
        player.foot = face[7].get_text().strip()
        player.height = float(face[8].get_text().split("|")[0].strip("cm "))
        player.weight = float(face[9].get_text().strip(""))
        player.version = face[10].get_text().strip()
        player.def_wr = face[11].get_text().strip()
        player.att_wr = face[12].get_text().strip()
        player.added_on = datetime.strptime(face[13].get_text().strip()[2:], "%y-%m-%d")
        player.real_face = face[15].get_text().strip()=="icon-checkmark text-success"
        player.body_type = face[16].get_text().strip()
        player.age = face[17].get_text().strip(" years old \n\r")
        player.rating = self.make_rating([sub for sub in page.find("div",id="stats_box").find(class_="stats-inner col-md-12").find(class_="row").children])
        player.href = "/"+page.find(id="share_player_link")["value"].strip("https://www.futbin.com/")
        player.pid = int(page.find(id="page-info")["data-player-resource"])
        return player