from dash import html
from utils import RiotAPI

api = RiotAPI()


def playerCardboard(
    gamename="Username",
    tagline="#EUW",
    level="Niveau 0",
    avatar_src="https://ddragon.leagueoflegends.com/cdn/15.4.1/img/profileicon/685.png",
):
    return html.Div(
        className="bg-[var(--light-surface)] text-[var(--light-onsurface)] dark:bg-[var(--dark-surface)] dark:text-[var(--dark-onsurface)] shadow-lg rounded-lg overflow-hidden w-full max-w-xs sm:max-w-md md:max-w-lg lg:max-w-xl",
        children=[
            html.Div(
                className="p-4",
                children=[  # Avatar
                    html.Img(
                        className="w-32 h-32 mx-auto rounded-full",
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
                        className="text-gray-600 dark:text-gray-300 text-center",
                        children=f"#{tagline}",
                        id="player_tagline",
                    ),
                    html.Div(
                        className="mt-4 flex justify-center",
                        children=html.Span(
                            className="bg-[var(--light-secondary)] text-[var(--light-onsecondary)] text-sm font-semibold px-3 py-1 rounded-full shadow-md",
                            children=level,
                            id="player_level",
                        ),
                    ),
                ],
            ),
        ],
    )
