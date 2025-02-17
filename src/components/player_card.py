from dash import html, callback, Input, Output
from utils import RiotAPI

api = RiotAPI()


def playerCardboard():
    return html.Div(
        className="shadow-lg rounded-lg overflow-hidden w-full max-w-xs sm:max-w-md md:max-w-lg lg:max-w-xl",
        children=[
            html.Div(
                className="p-4",
                children=[  # Avatar
                    html.Img(
                        className="w-32 h-32 mx-auto rounded-full border-4 border-white",
                        alt="Player Avatar",
                        src="https://via.placeholder.com/80",
                        id="player_avatar",
                    ),
                    # Player info
                    html.H2(
                        className="mt-4 text-2xl font-bold text-center",
                        children="GameName",
                        id="player_gamename",
                    ),
                    html.P(
                        className="text-gray-600 text-center",
                        children="#tagline",
                        id="player_tagline",
                    ),
                    html.Div(
                        className="mt-4 flex justify-center",
                        children=html.Span(
                            className="bg-blue-600 text-white text-sm font-semibold px-3 py-1 rounded-full shadow-md",
                            children="Level 0",
                            id="player_level",
                        ),
                    ),
                ],
            ),
            html.Div(children=[]),
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
            f"#{playerdata['tagLine']}",
            playerdata["gameName"],
            f"https://ddragon.leagueoflegends.com/cdn/15.2.1/img/profileicon/{sumonnerdata['profileIconId']}.png",
            f"Level {sumonnerdata['summonerLevel']}",
        )
    else:
        return "#EUW", "Username", "https://avatar.iran.liara.run/public/41", "Level 25"
