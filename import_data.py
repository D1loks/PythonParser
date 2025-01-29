from teams.models import Team
from hockey_stats.main import HockeyTeamScraper

def import_teams():
    scraper = HockeyTeamScraper()
    teams = scraper.get_teams()
    
    for team_data in teams:
        Team.objects.create(
            name=team_data.name,
            year=team_data.year,
            wins=team_data.wins,
            losses=team_data.losses,
            win_percent=team_data.win_percent
        )

if __name__ == "__main__":
    import_teams()