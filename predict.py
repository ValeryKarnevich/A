import pickle
from flask import Flask
from flask import request
from flask import jsonify
import numpy as np

model_file_name = 'model.bin'

with open(model_file_name, 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask('pistachio')

@app.route('/predict_pistachio', methods=['POST'])
def predict():
    pistachio = request.get_json()
    pistachio_values_list = list(pistachio.values())
    X = np.array(pistachio_values_list).reshape(1, -1)

    y_pred = model.predict_proba(X)[0, 1]

    if y_pred >= 0.5:
        pistachio_type = 'Kirmizi'
    else:
        pistachio_type = 'Siit'

    result = {
        'kirmizi_probability': float(y_pred),
        'pistachio_type': pistachio_type
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)