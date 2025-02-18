from dash import html, dcc, Input, Output, State, callback
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
                className="w-full px-4 py-2 bg-gray-700 text-white text-sm rounded-md focus:outline-none focus:ring focus:ring-blue-500",
                debounce=True,
            ),
            html.Button(
                className="ml-2 bg-blue-600 hover:bg-blue-700 text-white px-3 py-2 rounded-md text-sm font-medium focus:outline-none",
                id="top_navbar_search_button",
                children="Search",
            ),
            # Stores Account information
            dcc.Store(id="account_information_store"),
        ],
    )


@callback(
    Output("account_information_store", "data"),
    Input("top_navbar_search_bar", "n_submit"),
    Input("top_navbar_search_button", "n_clicks"),
    State("top_navbar_search_bar", "value"),
)
def search_player(n_submit, n_click, input_string):
    if (n_click or n_submit) and validate_gamename_and_tagline(
        input_string=input_string
    ):
        # split gamename and tagline
        gamename = input_string.split("#")[0].strip(" ")
        tagline = input_string.split("#")[-1].strip(" ")

        data = api.get_account_by_riot_id(gameName=gamename, tagLine=tagline)

        summoner_data = api.get_summoner_by_puuid(puuid=data.get("puuid"))

        return data | summoner_data


def topNavBar():
    return html.Nav(
        className="bg-gray-800 text-white sticky top-0 z-50 shadow-lg",
        children=[
            html.Div(
                className="container max-w-xl mx-auto flex items-center justify-between px-4 py-2 gap-4",
                children=[
                    html.A(
                        className="flex items-center",
                        children=[
                            html.Img(
                                className="h-8 w-8",
                                src="assets/logos/Penta_icon.png",
                                alt="Pentalytics logo",
                            ),
                            html.Span(
                                className="ml-3 text-xl font-bold",
                                children="Pentalytics",
                            ),
                        ],
                    ),
                    html.Div(
                        className="flex items-center justify-center flex-grow",
                        children=[searchBar()],
                    ),
                ],
            )
        ],
    )
