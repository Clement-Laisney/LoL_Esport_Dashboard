from dash import Dash, html, callback, Input, Output
from components import topNavBar, playerCardboard, rankCardboard

# call the ability to add external scripts
external_scripts = [
    # add the tailwind cdn url hosting the files with the utility classes
    {"src": "https://cdn.tailwindcss.com"},
]

app = Dash(
    __name__,
    external_scripts=external_scripts,
)

app.layout = html.Div(
    className="bg-[var(--light-bg)] text-[var(--light-text-primary)] dark:bg-[var(--dark-bg)] dark:text-[var(--dark-text-primary)] flex flex-col items-center min-h-screen",
    children=[
        topNavBar(),
        html.Div(
            className="w-full",
            id="main",
        ),
    ],
)


@callback(Output("main", "children"), Input("account_information_store", "data"))
def display_playerCardboard(playerdata):
    if playerdata:
        return html.Div(
            className="container md:flex justify-center w-full mx-auto p-6 space-y-6 md:space-x-10 md:space-y-0",
            children=[
                playerCardboard(
                    gamename=playerdata.get("gameName"),
                    tagline=playerdata.get("tagLine"),
                    level=f"Niveau {playerdata.get('summonerLevel')}",
                    avatar_src=f"https://ddragon.leagueoflegends.com/cdn/15.4.1/img/profileicon/{playerdata.get('profileIconId')}.png",
                ),
                rankCardboard(playerdata.get("league")),
            ],
        )
    else:
        return html.Div(
            className="flex flex-col justify-center h-screen ",
            children=[
                html.H1(
                    className="text-4xl font-bold mb-4 text-center",
                    children=["Bienvenue sur notre Dashboard !"],
                ),
                html.P(
                    className="text-lg text-[var(--light-text-secondary)] dark:text-[var(--dark-text-secondary)] mb-6 text-center",
                    children=[
                        "Pour commencer, veuillez effectuer une recherche "
                        "en utilisant la barre de recherche ci-dessus."
                    ],
                ),
            ],
        )


if __name__ == "__main__":
    app.run(debug=True)
