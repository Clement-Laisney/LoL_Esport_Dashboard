from dash import html, dcc, Input, Output, State, callback
from dash_svg import Svg, Path
from utils import validate_gamename_and_tagline, RiotAPI

api = RiotAPI()


def searchBar():
    return html.Div(
        className="absolute right-0 top-0 h-16 flex items-center pr-4 space-x-2",
        children=[
            dcc.Input(
                type="text",
                placeholder="Username #EUW",
                id="top_navbar_search_bar",
                className="bg-gray-700 text-white text-sm rounded-md px-3 py-2 focus:outline-none focus:ring focus:ring-blue-500",
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
    Input("top_navbar_search_button", "n_clicks"),
    Input("top_navbar_search_bar", "n_submit"),
    State("top_navbar_search_bar", "value"),
)
def search_player(n_clicks, n_submit, input_string):
    # check if input is in the right format
    if (n_clicks or n_submit) and validate_gamename_and_tagline(
        input_string=input_string
    ):
        # split nametag from tagline
        gamename = input_string.split("#")[0].strip(" ")
        tagline = input_string.split("#")[-1].strip(" ")

        data = api.get_account_by_riot_id(gameName=gamename, tagLine=tagline)
        return data


def topNavBar():
    return html.Nav(
        className="bg-gray-800 text-white fixed top-0 left-0 w-full z-50 shadow-lg",
        children=[
            html.Div(
                className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
                children=[
                    html.Div(
                        className="flex justify-around h-16",
                        children=[
                            # Logo,
                            html.Div(
                                className="flex-shrink-0 flex items-center",
                                children=[
                                    html.A(
                                        className="text-xl font-bold",
                                        href="#",
                                        children="Pentadata",
                                    ),
                                    # Navigation Links
                                    # html.Div(
                                    #     className="hidden md:flex space-x-4",
                                    #     children=[
                                    #         html.A(
                                    #             className="px-3 py-2 rounded-md text-sm font-medium hover:bg-gray-700",
                                    #             href="#",
                                    #             children="Home",
                                    #         )
                                    #     ],
                                    # ),
                                    searchBar(),
                                    # Mobile Menu Button
                                    # html.Div(
                                    #     className="md:hidden flex items-center",
                                    #     children=[
                                    #         html.Button(
                                    #             id="mobile-menu-button",
                                    #             className="text-gray-300 hover:text-white focus:outline-none focus:ring-2 focus:ring-white",
                                    #             children=[
                                    #                 Svg(
                                    #                     Path(
                                    #                         strokeLinecap="round",
                                    #                         strokeLinejoin="round",
                                    #                         strokeWidth=2,
                                    #                         d="M4 6h16M4 12h16m-7 6h7",
                                    #                     ),
                                    #                     className="h-6 w-6",
                                    #                     xmlns="http://www.w3.org/2000/svg",
                                    #                     fill=None,
                                    #                     viewBox="0 0 24 24",
                                    #                     stroke="currentColor",
                                    #                 )
                                    #             ],
                                    #         )
                                    #     ],
                                    # ),
                                    # # Mobile Menu*
                                    # html.Div(
                                    #     className="md:hidden hidden bg-gray-700",
                                    #     id="mobile-menu",
                                    #     children=[
                                    #         html.A(
                                    #             className="block px-4 py-2 text-sm text-gray-200 hover:bg-gray-600",
                                    #             href="#",
                                    #             children="Home",
                                    #         )
                                    #     ],
                                    # ),
                                ],
                            ),
                        ],
                    )
                ],
            )
        ],
    )
