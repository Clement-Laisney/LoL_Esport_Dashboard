from dash import Dash, html, callback, Input, Output
from components import topNavBar, playerCardboard

# call the ability to add external scripts
external_scripts = [
    # add the tailwind cdn url hosting the files with the utility classes
    {"src": "https://cdn.tailwindcss.com"}
]

app = Dash(__name__, external_scripts=external_scripts)

app.layout = html.Div(
    [
        topNavBar(),
        html.Div(
            className="pt-20",  # Padding pour éviter le chevauchement avec la navbar
            children=[
                playerCardboard(),
                html.H1(
                    "Welcome to My App",
                    className="text-3xl font-bold text-center mt-10",
                ),
                html.P(
                    "This is a sample Dash app with a Tailwind CSS navbar and a search bar.",
                    className="text-center text-gray-600 mt-4",
                ),
                html.P(
                    "This is a sample Dash app with a Tailwind CSS navbar and a search bar.",
                    className="text-center text-gray-600 mt-4",
                    id="data_out",
                ),
            ],
        ),
    ]
)


@callback(Output("data_out", "children"), Input("account_information_store", "data"))
def test_get_data(data):
    return str(data)


if __name__ == "__main__":
    app.run(debug=True)
