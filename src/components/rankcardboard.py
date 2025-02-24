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
        className="font-semibold custom-tab",
        selected_className="font-semibold selected-custom-tab",
        children=[
            html.Div(
                className="p-4 flex flex-col items-center",
                children=[
                    html.Img(
                        className="w-24 h-24 rounded-full",
                        src=tierimg,
                        alt="Division",
                    ),
                    html.H3(
                        className="mt-2 text-xl font-bold",
                        children=f"{tier} {rank}",
                    ),
                    html.P(
                        className="text-[var(--light-text-secondary)] dark:text-[var(--dark-text-secondary)]",
                        children=f"{LP} LP",
                    ),
                    html.P(
                        className="text-[var(--light-text-secondary)] dark:text-[var(--dark-text-secondary)]",
                        children=[
                            f"Victory rate: {round(wins/(wins+losses)*100)}%",
                        ],
                    ),
                    html.P(
                        className="text-[var(--light-text-secondary)] dark:text-[var(--dark-text-secondary)]",
                        children=[
                            f"{wins}V {losses}L",
                        ],
                    ),
                ],
            )
        ],
    )


def rankCardboard(leaguedata: list[dict]):
    return html.Div(
        className="bg-[var(--light-surface)] text-[var(--light-text-primary)] dark:bg-[var(--dark-surface)] dark:text-[var(--dark-text-primary)] mx-auto shadow-lg rounded-lg overflow-hidden w-full min-w-[22rem]",
        children=[
            dcc.Tabs(
                className="w-full",
                mobile_breakpoint=0,
                children=[
                    rankTab(
                        tabname="Ranked Solo/Duo"
                        if data.get("queueType") == "RANKED_SOLO_5x5"
                        else "Ranked Flex",
                        tierimg=f"/assets/images/tier_emblems/{data.get("tier")}.png",
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
