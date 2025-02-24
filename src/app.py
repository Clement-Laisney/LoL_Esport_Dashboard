from dash import Dash, html, page_container, dcc
from components import topNavbar

# call the ability to add external scripts
external_scripts = [
    # add the tailwind cdn url hosting the files with the utility classes
    {"src": "https://cdn.tailwindcss.com"},
]

app = Dash(__name__, external_scripts=external_scripts, use_pages=True)

app.layout = html.Div(
    className="bg-[var(--light-bg)] text-[var(--light-text-primary)] dark:bg-[var(--dark-bg)] dark:text-[var(--dark-text-primary)] flex flex-col items-center min-h-screen",
    children=[
        topNavbar(),
        html.Div(
            className="container mx-auto mt-8",
            id="main",
            children=[
                page_container,
            ],
        ),
        dcc.Store(id="account_information_store"),
    ],
)


if __name__ == "__main__":
    app.run(debug=True)
