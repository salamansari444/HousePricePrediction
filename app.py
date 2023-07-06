# libraries to be installed
# flask, scikit-learn, pandas, pickle-mixin

import pandas as pd
import pickle
from flask import Flask, render_template, request


app = Flask(__name__, template_folder='template')
data = pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open("LinearModal.pkl", "rb"))


@app.route('/')
def index():
    location = sorted(data['Location'].unique())
    return render_template('index.html', Location=location)


@app.route('/predict', methods=['POST'])
def predict():
    locations = request.form.get('Location')
    bhk = request.form.get('bhk')
    sqft = request.form.get('total_sqft')
    lift = request.form.get('lift')
    car = request.form.get('car')

    print(locations, bhk, sqft)
    input = pd.DataFrame([[sqft, locations, bhk, lift, car]],
                         columns=['Area', 'Location', 'No. of Bedrooms', 'Lift Available', 'Car Parking'])
    prediction = pipe.predict(input)[0]

    return str(prediction)


if __name__ == '__main__':
    app.run(debug=True, port=5005)

# pip install gunicorn
# used to create a server in our code which will be responsible to connect the code to heroku

#pip freeze > requirement.txt