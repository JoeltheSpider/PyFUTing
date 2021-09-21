import requests
from bs4 import BeautifulSoup
from datetime import datetime 

class PlayerReq:
    """
    Player related request making part of the extract module
    """
    def __init__(self, console="pc", year="21"):
        self.DAILY_GRAPH_LINK = "https://www.futbin.com/"+year+"/playerGraph?type=daily_graph&year=21&player={0}"
        self.PLAYERS_LINK = "https://www.futbin.com/"+year+"/players/"
        self.console = console
        
    def get_price_history(self, player_id, type="daily"):
        """
            Returns dict of time, price for player.
            (Currently daily price update is only supported)
            #TODO: Update for hourly
        """
        r = requests.get(self.DAILY_GRAPH_LINK.format(player_id))
        data = r.json()[self.console]
        price_history = []
        for price in data:
            date = datetime.utcfromtimestamp(price[0] / 1000).strftime('%Y-%m-%d')
            price = price[1]
            price_history.append([date,price])
        return price_history
    
    def load_player_page(self, link):
        """
            Loads player's futbin page.
        """
        url = "http://futbin.com"+link
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup
    
    def load_players_page_by_name(self, player_name):
        """
            Loads players page by name.
            page_no >= 1
        """
        url = self.PLAYERS_LINK +"?page=1&search=" + player_name
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup
    
    def load_players_page(self, page_no, version="all"):
        """
            Loads players page.
            page_no >= 1
        """
        url = self.PLAYERS_LINK +"?page="+str(page_no)+"&version=%s"%version
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup