from dash import Dash, html, callback, Input, Output
from components import topNavBar, playerCardboard

# call the ability to add external scripts
external_scripts = [
    # add the tailwind cdn url hosting the files with the utility classes
    {"src": "https://cdn.tailwindcss.com"}
]

app = Dash(__name__, external_scripts=external_scripts)

app.layout = html.Div(
    className="min-h-screen bg-slate-50 dark:bg-black dark:text-white",
    children=[topNavBar()],
)


if __name__ == "__main__":
    app.run(debug=True)
