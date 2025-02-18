from dash import html, callback, Input, Output
from utils import RiotAPI

api = RiotAPI()


def playerCardboard(
    gamename="Username",
    tagline="#EUW",
    level="Level 0",
    avatar_src="https://avatar.iran.liara.run/public/41",
):
    return html.Div(
        className="shadow-lg rounded-lg overflow-hidden w-full max-w-xs sm:max-w-md md:max-w-lg lg:max-w-xl",
        children=[
            html.Div(
                className="p-4",
                children=[  # Avatar
                    html.Img(
                        className="w-32 h-32 mx-auto rounded-full border-4 border-white",
                        alt="Player Avatar",
                        src=avatar_src,
                        id="player_avatar",
                    ),
                    # Player info
                    html.H2(
                        className="mt-4 text-2xl font-bold text-center",
                        children=gamename,
                        id="player_gamename",
                    ),
                    html.P(
                        className="text-gray-600 text-center",
                        children=tagline,
                        id="player_tagline",
                    ),
                    html.Div(
                        className="mt-4 flex justify-center",
                        children=html.Span(
                            className="bg-blue-600 text-white text-sm font-semibold px-3 py-1 rounded-full shadow-md",
                            children=level,
                            id="player_level",
                        ),
                    ),
                ],
            ),
        ],
    )
