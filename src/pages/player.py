from dash import html, register_page
from components import playerCardboard, rankCardboard, matchHistory
from utils import retrieve_player_data

register_page(__name__, path_template="/player/<gamename>-<tagline>")


def layout(gamename=None, tagline=None, **kwargs):
    if gamename and tagline:
        playerdata = retrieve_player_data(gamename=gamename, tagline=tagline)
        return html.Div(
            className="container flex flex-col gap-8 mx-auto md:max-w-6xl",
            children=[
                html.Div(
                    className="grid grid-cols-1 md:grid-cols-2 gap-6 justify-item-center",
                    children=[
                        playerCardboard(
                            gamename=playerdata.get("gameName"),
                            tagline=playerdata.get("tagLine"),
                            level=f"Level {playerdata.get('summonerLevel')}",
                            avatar_src=f"https://ddragon.leagueoflegends.com/cdn/15.4.1/img/profileicon/{playerdata.get('profileIconId')}.png",
                        ),
                        rankCardboard(playerdata.get("league")),
                    ],
                ),
                html.Div(
                    className="grid grid-cols-1 md:grid-cols-2 gap-6 justify-item-center",
                    children=[
                        matchHistory(),
                    ],
                ),
            ],
        )
