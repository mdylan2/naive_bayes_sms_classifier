import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from model import textParser
from sklearn.externals import joblib


app = dash.Dash(__name__)
app.server.config["SERVE_LOCALLY"] = True

navbar = dbc.NavbarSimple(
        brand="Spam Classifier",
        brand_href="#",
        sticky='top',    
        dark = True,
        color = 'primary',
    )

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
                html.P(dbc.Button(html.A("GitHub", href = "https://github.com/mdylan2/naive_bayes_sms_classifier"), color="primary"), className="lead")
            ],
        )



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


app.layout = html.Div([navbar, dbc.Container([jumbotron, body], className = "main")])


@app.callback(
    Output("classify","children"),
    [Input("letsgo","n_clicks")],
    [State("text-input","value")]
)
def classify(n_clicks, text):
    if n_clicks is None:
        return ""
    if n_clicks > 0:
        if text == "":
            return "Please enter some text"
        else:
            answer = model.predict([text])
            if answer == 1:
                return dbc.Button("Spammer. Do not respond.", color = "danger", block = True, size = "lg")
            elif answer == 0:
                return dbc.Button("Not a spammer. Respond to this person.", color = "success", block = True, size = "lg")
            else:
                return "Error with the Model. Please try again later. :)"

if __name__ == '__main__':
    model = joblib.load('assets/ml_models/training_pipeline.sav')
    app.server.run(debug=False)