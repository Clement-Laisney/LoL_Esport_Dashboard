from dash import html, dcc


def rankTab(
    tabname="SOLO Queue",
    tierimg="assets/images/tier_emblems/PLATINUM.png",
    tier="Platinum",
    rank="III",
    LP=50,
    wins=30,
    losses=14,
):
    return dcc.Tab(
        label=tabname,
        className="text-[var(--light-onbg)] font-semibold",
        children=[
            html.Div(
                className="p-4 flex flex-col items-center",
                children=[
                    html.Img(
                        className="w-24 h-24 rounded-full border-4 border-white",
                        src=tierimg,
                        alt="Division",
                    ),
                    html.H3(
                        className="mt-2 text-xl font-bold",
                        children=f"{tier} {rank}",
                    ),
                    html.P(
                        className="text-gray-600",
                        children=f"{LP} LP",
                    ),
                    html.P(
                        className="text-gray-600",
                        children=[
                            f"Taux de Victoire: {round(wins/(wins+losses)*100)}%",
                        ],
                    ),
                    html.P(
                        className="text-gray-600",
                        children=[
                            f"{wins}V {losses}D",
                        ],
                    ),
                ],
            )
        ],
    )


def rankCardboard(leaguedata: list[dict]):
    return html.Div(
        className="bg-white shadow-lg rounded-lg overflow-hidden w-full max-w-md mx-auto",
        children=[
            dcc.Tabs(
                className="w-full",
                children=[
                    rankTab(
                        tabname="Classé Solo/Duo"
                        if data.get("queueType") == "RANKED_SOLO_5x5"
                        else "Classé Flexible",
                        tierimg=f"assets/images/tier_emblems/{data.get("tier")}.png",
                        tier=data.get("tier"),
                        rank=data.get("rank"),
                        LP=data.get("leaguePoints"),
                        wins=data.get("wins"),
                        losses=data.get("losses"),
                    )
                    for data in leaguedata
                ],
            )
        ],
    )
