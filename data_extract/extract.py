# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:20:53 2021

@author: Joel 
"""


import requests
from bs4 import BeautifulSoup
from datetime import datetime 

delta = 1 #no of pages to go though

#############
# DATA INPUT: Player table row 
def get_current_price(player):
    return player.find_all("td")[4].get_text().strip()

def get_name(player):
    return player.find("img")["alt"]
    
def get_link(player):
    return player.find("a")["href"]

def get_player_version(player):
    return player.find_all("td")[3].get_text().strip()
#############


def get_price_history(player_id):
    r = requests.get('https://www.futbin.com/21/playerGraph?type=daily_graph&year=21&player={0}'.format(player_id))
    data = r.json()["pc"]
    price_history = []
    for price in data:
        date = datetime.utcfromtimestamp(price[0] / 1000).strftime('%Y-%m-%d')
        price = price[1]
        price_history.append([date,price])
    return price_history

def load_player_page(link):    
    url = "http://futbin.com"+link
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def load_gold_players_page(page_no): #page_no > 1
    url = 'https://www.futbin.com/21/players/'+"?page="+str(i)+"&version=gold"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def load_players_page(page_no): #page_no > 1
    url = 'https://www.futbin.com/21/players/'+"?page="+str(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

trade_info = {}
for i in range(delta):
    soup = load_gold_players_page(i+1)
    players = soup.find("table",id="repTb").find("tbody").find_all("tr")
    for player in players:
        link = get_link(player)
        name = get_name(player)
        print("Name:", name, ", href: ", link)
        
        soup = load_player_page(link)
        
        player_id = soup.find(id="page-info")["data-player-resource"]
        price_history = get_price_history(player_id)
        trade_info[name] = {"price": price_history, "id":player_id}
        