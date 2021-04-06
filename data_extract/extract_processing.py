# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:20:53 2021

@author: Joel 
"""
from player_req import PlayerReq

#TODO: add KeyboardInterrupt exception handling : should return data processed till that point. 
# Find a fancy way to do (generic wrappers?)
class ExtractProc:
    """
    Processsing part of extract module
    """
    def __init__(self, console="pc"):
        self.console = console
        self.fut = PlayerReq(console)
        
    def get_current_price(self, player):
        return player.find_all("td")[4].get_text().strip()
    
    def get_name(self, player):
        return player.find("img")["alt"]
        
    def get_link(self, player):
        return player.find("a")["href"]
    
    def get_player_version(self, player):
        return player.find_all("td")[3].get_text().strip()
    
    def get_player_id(self, player_page):
        """
        Returns player's permanent id
        """
        return player_page.find(id="page-info")["data-player-resource"]
    
    def iterate_players_trade(self, players):
        trade_data = []
        for player in players:
            link = self.get_link(player)
            name = self.get_name(player)
            print("Extracting name:", name, ", href: ", link)
            
            soup = self.fut.load_player_page(link)
            player_id = self.get_player_id(soup)
            
            price_history = self.fut.get_price_history(player_id)
            trade_data.append({"name":name, "price": price_history, "id":player_id,
                               "version": self.get_player_version(player)})
        return trade_data
    
    def get_trade_data(self, page_no=1, version="gold"):
        """
            Returns trade history of each player as dict.
            Output entry for each player:
                name:   Name of the player
                price:  Price history
                id:     Permanent id of the player
            
            usage:
                ExtractProc().get_trade_data(5, "fut-bd")
        """
        trade_data = []
        for i in range(page_no):
            soup = self.fut.load_players_page(i+1,"gold")
            players = soup.find("table",id="repTb").find("tbody").find_all("tr")
            trade_data.extend(self.iterate_players_trade(players))
        return trade_data
    
    def get_trade_data_by_name(self, player_name):
        """
            Returns trade history of the player for all cards
        """
        player_name = "%20".join(player_name.lower().split())
        soup = self.fut.load_players_page_by_name(player_name)
        
        players = soup.find("table",id="repTb").find("tbody").find_all("tr")
        trade_data = self.iterate_players_trade(players)
        return trade_data
    
    def get_name_id_map(self, player_name):
        """
            Returns card version - permanent id mapping for each player name.
            
            usage:
                ExtractProc().get_name_id_map("Lionel Messi")
        """
        player_name = "%20".join(player_name.lower().split())
        soup = self.fut.load_players_page_by_name(player_name)
        id_map = {}
        players = soup.find("table",id="repTb").find("tbody").find_all("tr")
        for player in players:
            link = self.get_link(player)
            name = self.get_name(player).strip()
            version = self.get_player_version(player)
            print("Extracting for ",name+' '+version)
            soup = self.fut.load_player_page(link)
            player_id = self.get_player_id(soup)
            
            id_map[name+' '+version] = player_id
        
        return id_map