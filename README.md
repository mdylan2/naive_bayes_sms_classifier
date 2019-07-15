# Naive Bayes Spam Classifier for SMS
## Description
This repository contains the Python code used to build a Naive Bayes SMS Spam Classifier along with a Dash front end. 
Users can type in a message in a text box and the model will print whether or not the given message is spam.

The application was designed using Pandas, Scikit Learn and Dash.

## Files
Here's a list of files in the directories:
### `FrontEnd`
- `app.py`: Contains the code for the Dash front end
- `model.py`: Contains the code for the text parser used in the model
- `assets`: Directory that contains files used in the front end, including the backgrounds, CSS, and the saved ML model

### `Notebook`
This directory contains the notebook and data used to generate the model
- `sms-classifier.ipynb`: The notebook that describes how the model was generated. After running the entire notebook, the model should save inside the
`FrontEnd/assets/ml_models` folder
- `input`: Contains the spam/non-spam data used to train the model

## Usage
In order to start the Dash application, do the following:
1) Clone the repo
```
git clone https://github.com/mdylan2/naive_bayes_sms_classifier.git
```
2) Navigate into the folder, set up a virtual environment and activate it
3) Once you've activated the virtual environment, install the requirements
```
pip install -r requirements.txt
```
4) Navigate into the FrontEnd folder and run the following command:
```
python app.py
```

## Questions Or Contributions
Always open to any questions or contributions! Please reach out to me on Github.
