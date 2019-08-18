# Importing modules
import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from sklearn.externals import joblib

# Importing local files
import view
from model import textParser

# Creating the server and serving local CSS
app = dash.Dash(__name__)
app.server.config["SERVE_LOCALLY"] = True

# Assigning the app layout
app.layout = view.layout

# Callback for classifying spam versus not spam
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

# Loading the model and running the app
if __name__ == '__main__':
    model = joblib.load('assets/ml_models/training_pipeline.sav')
    app.server.run(debug=True)