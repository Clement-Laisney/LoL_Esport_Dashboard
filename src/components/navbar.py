from dash import html, dcc, Input, Output, State, callback, callback_context
from utils import validate_gamename_and_tagline, RiotAPI

api = RiotAPI()


def searchBar():
    return html.Div(
        className="w-full max-w-lg top-0 h-16 flex items-center pr-4 space-x-2",
        children=[
            dcc.Input(
                type="text",
                placeholder="Username #EUW",
                id="top_navbar_search_bar",
                className="w-full px-4 py-2 bg-[var(--light-variant-primary)] text-[var(--light-onprimary)] placeholder:text-gray-300 text-sm rounded-md focus:outline-none focus:ring focus:ring-[var(--light-secondary)]",
            ),
            html.Button(
                className="ml-2 bg-[var(--light-secondary)] hover:bg-[var(--light-variant-secondary)] text-[var(--light-onsecondary)] px-3 py-2 rounded-md text-sm font-medium focus:outline-none",
                id="top_navbar_search_button",
                children="Search",
            ),
        ],
    )


def topNavbar():
    return html.Nav(
        className="bg-[var(--light-primary)] text-[var(--light-onprimary)] sticky top-0 w-full shadow-lg z-10",
        children=[
            html.Div(
                className="max-w-lg mx-auto flex items-center justify-between px-4 py-2 gap-4",
                children=[
                    dcc.Link(
                        href="/",
                        className="flex items-center",
                        children=[
                            html.Img(
                                className="h-8 w-8",
                                src="/assets/logos/Penta_icon.png",
                                alt="Pentalytics logo",
                            ),
                            html.Span(
                                className="ml-3 text-xl font-bold hidden md:inline",
                                children="Pentalytics",
                            ),
                        ],
                    ),
                    html.Div(
                        className="flex items-center justify-center flex-grow",
                        children=[searchBar()],
                    ),
                    dcc.Location(id="player_location", refresh="callback-nav"),
                ],
            )
        ],
    )


@callback(
    Output("player_location", "href"),
    Input("top_navbar_search_bar", "n_submit"),
    Input("top_navbar_search_button", "n_clicks"),
    State("top_navbar_search_bar", "value"),
    prevent_initial_call=True,
)
def search_player(n_submit, n_click, input_string):
    if (n_click or n_submit) and validate_gamename_and_tagline(
        input_string=input_string
    ):
        # split gamename and tagline
        gamename = input_string.split("#")[0].strip(" ")
        tagline = input_string.split("#")[-1].strip(" ")

        return f"/player/{gamename}-{tagline}"
