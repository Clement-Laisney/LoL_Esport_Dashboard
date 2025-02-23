from dash import html, register_page
from components import playerCardboard, rankCardboard
from utils import retrieve_player_data

register_page(__name__, path_template="/player/<gamename>-<tagline>")


def layout(gamename=None, tagline=None, **kwargs):
    if gamename and tagline:
        playerdata = retrieve_player_data(gamename=gamename, tagline=tagline)
        return html.Div(
            className="container md:flex justify-center w-full mx-auto p-6 space-y-6 md:space-x-10 md:space-y-0",
            children=[
                playerCardboard(
                    gamename=playerdata.get("gameName"),
                    tagline=playerdata.get("tagLine"),
                    level=f"Level {playerdata.get('summonerLevel')}",
                    avatar_src=f"https://ddragon.leagueoflegends.com/cdn/15.4.1/img/profileicon/{playerdata.get('profileIconId')}.png",
                ),
                rankCardboard(playerdata.get("league")),
            ],
        )
