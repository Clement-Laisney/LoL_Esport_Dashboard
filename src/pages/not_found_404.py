from dash import html, register_page, dcc

register_page(__name__)

layout = html.Div(
    className="text-center justify-center",
    children=[
        html.Img(
            className="w-64 h-64 mx-auto mb-4",
            src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhtNnlxOWlhZGFwcm5kM2o0OGdzanVid3phZzluaGduMHd2aGY3MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/jWexOOlYe241y/giphy.gif",
        ),
        html.H1(className="text-4xl font-bold mb-2", children="Oops! Page Not Found"),
        html.P(
            className="text-[var(--light-text-secondary)] dark:text-[var(--dark-text-secondary)] mb-6",
            children="Sorry, the page you are looking for does not exist.",
        ),
        dcc.Link(
            href="/",
            className="bg-[var(--light-secondary)] text-white px-4 py-2 rounded hover:bg-[var(--light-variant-secondary)]",
            children="Go Back Home",
        ),
    ],
)
