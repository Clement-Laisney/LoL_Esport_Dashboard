from dash import html, dcc, callback, Input, Output
from utils import RiotAPI

api = RiotAPI()


def playerCardboard():
    return html.Div(
        className="bg-white text-white rounded-2xl shadow-lg p-6 w-80",
        children=[
            # Avatar
            html.Div(
                className="flex items-center space-x-4",
                children=html.Img(
                    className="w-16 h-16 rounded-full border-2 border-blue-500",
                    alt="Player Avatar",
                    src="https://via.placeholder.com/80",
                    id="player_avatar",
                ),
            ),
            # Player info
            html.Div(
                children=[
                    html.H2(
                        className="text-xl font-bold text-black",
                        children="GameName",
                        id="player_gamename",
                    ),
                    html.P(
                        className="text-gray-400 text-sm",
                        children="#tagline",
                        id="player_tagline",
                    ),
                    html.Div(
                        className="mt-4",
                        children=html.Span(
                            className="px-3 py-1 bg-blue-600 rounded-full text-sm font-semibold",
                            children="Level 0",
                            id="player_level",
                        ),
                    ),
                ]
            ),
        ],
    )


@callback(
    Output("player_tagline", "children"),
    Output("player_gamename", "children"),
    Output("player_avatar", "src"),
    Output("player_level", "children"),
    Input("account_information_store", "data"),
)
def update_player_cardboard(playerdata):
    if playerdata:
        sumonnerdata = api.get_summoner_by_puuid(puuid=playerdata["puuid"])
        return (
            f"#{playerdata["tagLine"]}",
            playerdata["gameName"],
            f"https://ddragon.leagueoflegends.com/cdn/15.2.1/img/profileicon/{sumonnerdata['profileIconId']}.png",
            f"Level {sumonnerdata["summonerLevel"]}",
        )
    else:
        return "#EUW", "Username", "https://avatar.iran.liara.run/public/41", "Level 25"
