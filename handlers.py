import requests
from bot_config import SPORTS_GAME_ODDS_API_KEY

def get_odds():
    url = "https://app.sportsgameodds.com/api/odds"
    headers = {"X-API-Key": SPORTS_GAME_ODDS_API_KEY}
    params = {
        "sport": "soccer",
        "region": "eu",
        "mkt": "h2h"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        results = []

        for game in data.get("data", [])[:5]:
            home = game.get("home_team", "N/A")
            away = game.get("away_team", "N/A")
            sites = game.get("sites", [])
            odds_info = ", ".join(f"{site['site_nice']}: {site['odds']['h2h']}" for site in sites[:2])
            results.append(f"{home} vs {away} ➤ {odds_info}")

        return "\n\n".join(results) if results else "Nenhuma odd encontrada no momento."
    
    except Exception as e:
        return f"Erro ao obter odds: {e}"
