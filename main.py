import requests
from bs4 import BeautifulSoup
import mysql.connector
from dataclasses import dataclass
import os
from dotenv import load_dotenv

@dataclass
class Team:
    name: str
    year: int
    wins: int
    losses: int
    win_percent: float

class HockeyTeamScraper:
    def __init__(self):
        self.url = "https://www.scrapethissite.com/pages/forms/"
        
    def get_teams(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        teams = []
        
        for team in soup.find_all('tr', class_='team'):
            name = team.find('td', class_='name').text.strip()
            year = int(team.find('td', class_='year').text.strip())
            wins = int(team.find('td', class_='wins').text.strip())
            losses = int(team.find('td', class_='losses').text.strip())
            win_percent = float(team.find('td', class_='pct').text.strip())
            
            teams.append(Team(name, year, wins, losses, win_percent))
            
        return teams

class HockeyTeamDatabase:
    def __init__(self):
        load_dotenv() 
        
        self.connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        self.cursor = self.connection.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS teams (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                year INT,
                wins INT,
                losses INT,
                win_percent FLOAT
            )
        """)
        self.connection.commit()
    
    def save_teams(self, teams: list[Team]):
        for team in teams:
            self.cursor.execute("""
                INSERT INTO teams (name, year, wins, losses, win_percent)
                VALUES (%s, %s, %s, %s, %s)
            """, (team.name, team.year, team.wins, team.losses, team.win_percent))
        self.connection.commit()
