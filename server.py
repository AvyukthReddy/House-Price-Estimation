from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np

df = pd.DataFrame()

ll = pd.read_csv("artifacts/locations.csv")
__locations = ll['locations'].to_list()

app = Flask(__name__)

model = pickle.load(open("./artifacts/house_prices_model.pickle", 'rb'))

@app.route('/')
def home():
    locs = ll['locations']
    return render_template('index.html', locs=locs)

def get_estimated_price(sqft, location, bhk, bath):
    loc_index = __locations.index(location)+3
    x = np.zeros(len(__locations)+3)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(model.predict([x])[0], 2)

@app.route('/predict', methods=['POST'])
def predict():
    total_sqft = float(request.form.get('total_sqft'))
    bhk = int(request.form.get('bhk'))
    bath = int(request.form.get('bath'))
    loc = request.form.get('loc')
    prediction = "₹ "
    if int(total_sqft) < 450:
        prediction = "Minimum Area: 450 sft"
    else:
        prediction += str(get_estimated_price(total_sqft, loc, bhk, bath))+" Lakh"
    return prediction

if __name__ == "__main__":
    app.run()
