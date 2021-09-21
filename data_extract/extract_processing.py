# objective: extract from sites and make player objects
from player_req import PlayerReq
from obj_req import ObjReq
from make_object import Player, Maker

#TODO: add KeyboardInterrupt exception handling : should return data processed till that point. 
# Find a fancy way to do (generic wrappers?)
class ExtractData:
    """
    Processsing part of extract module
    """
    def __init__(self, console="pc"):
        self.console = console
        self.fut = PlayerReq(console)
        self.futObj = ObjReq(console)
        self.maker = Maker()
        self.current_run = []

    ###########
    # from players page, cannot be used elsewhere
    # input is player row from futbin.com/players
    def get_current_price(self, player):
        return player.find_all("td")[4].get_text().strip()
    
    def get_name(self, player):
        return player.find("img")["alt"]
        
    def get_link(self, player):
        return player.find("a")["href"]
    
    def get_player_version(self, player):
        return player.find_all("td")[3].get_text().strip()
    ###########
    
    def get_player_id(self, player_page):
        """
        Returns player's permanent id
        """
        return player_page.find(id="page-info")["data-player-resource"]
    
    def iterate_players_trade_from_search(self, players):
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
    
    def iterate_players_trade_from_id(self, player_ids):
        trade_data = []
        for player_id in player_ids:
            price_history = self.fut.get_price_history(player_id)
            trade_data.append({"price": price_history, "id":player_id})
        return trade_data

    def make_player_objects(self):
        """
        main function
        """
        self.current_run = []
        try:
            i = 0
            while True:
                # check progress
                soup = self.fut.load_players_page(i+1,"all")
                players = soup.find("table",id="repTb").find("tbody").find_all("tr")[:2]
                # print([self.fut.load_player_page(self.get_link(player)) for player in players])
                for player in players:
                    print(self.get_name(player))
                    self.current_run.append(self.maker.make_player(self.fut.load_player_page(self.get_link(player))))
                i += 1
        except KeyboardInterrupt as e:
            return self.current_run
        return self.current_run
            
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
        try:
            for i in range(page_no):
                soup = self.fut.load_players_page(i+1,"gold")
                players = soup.find("table",id="repTb").find("tbody").find_all("tr")
                trade_data.extend(self.iterate_players_trade_from_search(players))
        except:
            pass
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
    
    def get_obj_players(self):
        """
            Returns each player page as list
        """
        players = []
        for player in self.futObj.load_player_obj():
            players.append(self.fut.load_player_page(player.find("a")["href"]))
        return players
    
    def get_milestone_players(self):
        """
            Returns each milestone player page as list
        """
        # players = []
        # for player_bunch in self.futObj.load_season_player_obj():
        #     for player in player_bunch.find_all("a")[1:]:
        #         players.append(self.fut.load_player_page(player["href"]))
        # return players
        # full player list not in futbin. 
        # If data is extracted from PlayerReq, not able to extract squad foundation players.
        # so disregard
        pass