import requests
from bs4 import BeautifulSoup
from datetime import datetime 

class ObjReq:
    """
    Objectives related request making part of the extract module.
    """
    def __init__(self):
        self.OBJ_LINK = "https://www.futbin.com/objectives/"

    def load_current_milestones(self):
        """
            Loads all current milestones objectives.
        """
        url = self.OBJ_LINK
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return [ms for ms in soup.find(class_="col-md-12 mainObjTab mainObjTabMilestones panel2").contents if ms!="\n"] #.find_all(class_="card mb-3 expandableGroupArea")

    def load_current_obj(self):
        """
            Loads all current objectives.
        """
        url = self.OBJ_LINK
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup.find(class_="objTab seasonTab").find_all(class_="groupAreaBlur")
    
    def load_current_player_obj(self):
        """
            Loads all current player objectives.
        """
        url = self.OBJ_LINK
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return [pl for pl in soup.find(class_="objTab seasonTab").find_all(class_="groupAreaBlur") if pl.find("a")!=None]
    
    def load_season_obj(self):
        """
            Loads all current season objectives.
            .find(class_="col-md-7 seasonDesc SeasonOption award-i").get_text().strip("\n ")
        """
        url = self.OBJ_LINK
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup.find(class_="col-md-12 mainObjTab mainObjTabSeason panel3").find(class_="stepper stepper-vertical ml0 pl-0").find_all("li",class_="")
    
    def load_season_player_obj(self):
        """
            Loads all current season player objectives.
            pl.find_all("a",class_="small-card-holder")[i]["href"]
        """
        temp = self.load_season_obj()
        return  temp[14],temp[29]