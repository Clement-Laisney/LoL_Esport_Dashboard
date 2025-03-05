from dash import html


def itemHistory(itemList: list[int], isWin: bool):
    component_list = []
    for item in itemList:
        if item == 0:
            component_list.append(
                html.Div(
                    className=f"h-6 w-6 rounded-md opacity-40 {'bg-[var(--win-text-color)]' if isWin else 'bg-[var(--lose-text-color)]'}"
                )
            )
        else:
            component_list.append(
                html.Img(
                    className="h-6 w-6 rounded-md",
                    src=f"/assets/images/item/{item}.png",
                )
            )
    return component_list
