import numpy as np
import pandas as pd
import requests
import datetime as dt
from MDate import MDate
from bs4 import BeautifulSoup

class PokemonStats():
    def __init__(self, name):
        self.name = name
        self.usage_data = []
        try:
            self.full_data = pd.read_csv("{pokemon}_usage_stats.csv".format(pokemon=self.name))
            self.full_data.set_index("date", inplace=True)
            print("Usage information loaded")
        except:
            print("Info loading failed; data is None")
            self.full_data = None


    def get_stats(self, format, year=2014, month=1):
        if year < 2014:
            year = 2014
        if month < 1:
            month = 1
        elif month > 12:
            month = 12
        
        url = "https://www.smogon.com/stats/"
        r = requests.get(url)
        html_doc = r.text
        soup = BeautifulSoup(html_doc, features="html.parser")
        links = soup.find_all("a")

        for link in links[1:]:
            year = int(link.text[0:4])
            month = int(link.text[5:7])
            date = MDate(year, month, 1)
            print(date)
            self._find_stats(date, format)

        self.full_data = pd.DataFrame(self.usage_data)
        self.full_data.set_index("date", inplace=True)
        self.full_data.to_csv('{pokemon}_{format}_usage_stats.csv'.format(pokemon=self.name, format=format))
  

    def _find_stats(self, date, format):
        url = "https://www.smogon.com/stats/{}/".format(str(date))
        r = requests.get(url)
        html_doc = r.text
        soup = BeautifulSoup(html_doc, features="html.parser")
        links = soup.find_all("a")
        if format == "ou":
            ratings = [0, 1500, 1695, 1825]
        else:
            ratings = [0, 1500, 1630, 1760]
        index = 0
        for link in links:
            if link.text.find(format) != -1:
                new_data = self._pull_stats(url+link.text, date)
                new_data["rating"] = ratings[index]
                new_data["format"] = format
                new_data["pokemon"] = self.name
                self.usage_data.append(new_data)
                index += 1
                if index > 3:
                    index = 0
        
        
    
    def _pull_stats(self, link, date):
        r = requests.get(link)
        html_doc = r.text
        document = html_doc.split("\n")

        total_battles = document[0].split(" ")[-1]               # Formatting to pull just the number and remove newline character at end

        document = document[5:]                                  # Skip header of table
        
        try:
            for line in document:
                pokemon_stats = line.replace(" ", "").split("|")
                if pokemon_stats[2] == self.name:
                    usage_rank = pokemon_stats[1]
                    use_percent = pokemon_stats[3].replace("%", "")
                    use_amount = pokemon_stats[4]
                    data = {"date":str(date), "rank":usage_rank, "usage_percent":use_percent, "usage_amount":use_amount, "total":total_battles}
                    break        
        except:
            print("hit except")
            data = {"date":np.NaN, "rank":np.NaN, "usage_percent":np.NaN, "usage_amount":np.NaN, "total":np.NaN}

        if data['rank'] is np.NaN:
            print("Pokemon Statistics Not Found")
            return data
        else:
            return data
        