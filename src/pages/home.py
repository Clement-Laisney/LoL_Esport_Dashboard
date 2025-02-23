from dash import html, register_page

register_page(__name__, path="/")

layout = html.Div(
    className="flex flex-col justify-center h-screen ",
    children=[
        html.H1(
            className="text-4xl font-bold mb-4 text-center",
            children=["Welcome to Pentalytics Dashboard !"],
        ),
        html.P(
            className="text-lg text-[var(--light-text-secondary)] dark:text-[var(--dark-text-secondary)] mb-6 text-center",
            children=["To get started, please search using the search bar above."],
        ),
    ],
)
