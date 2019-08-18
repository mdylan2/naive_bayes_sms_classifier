# Importing modules
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

# The navbar HTML
navbar = dbc.NavbarSimple(
        brand="Spam Classifier",
        brand_href="#",
        sticky='top',    
        dark = True,
        color = 'primary',
    )

# The jumbotron HTML
jumbotron = dbc.Jumbotron(
            [
                html.H1("Spam Classifier", className="display-3"),
                html.P(
                    "Author: Dylan Mendonca",
                    className="lead",
                ),
                html.Hr(className="my-2"),
                html.P(
                    "A Naive Classifier Built on Python"
                ),
                html.P(dbc.Button("GitHub", color="primary"), className="lead")
            ],
        )

# The Main Body HTML
body = html.Div(
    [
        dbc.Row(
            [
                dcc.Loading(
                    [
                        dbc.Col(
                            [

                            ], id = "classify"
                        )
                    ]
                )   
            ], className = "mt-3"
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.FormGroup(
                            dbc.Textarea(
                                id="text-input",
                                value=None
                            )
                        )
                    ]
                )
            ], className = "mt-3"
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Button("Let's Go!", id = "letsgo", color = "primary")
                    ],
                )
            ], className = "mt-2", justify = "end"
        )
    ]
)

# Compiled layout 
layout = html.Div([navbar, dbc.Container([jumbotron, body], className = "main")])