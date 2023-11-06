import requests

url = "http://localhost:9696/predict_pistachio"
pistachio = {
    "area": 78466,
    "perimeter": 2356.908,
    "major_axis": 445.9131,
    "minor_axis": 258.5125,
    "eccentricity": 0.8148,
    "eqdiasq": 316.0791,
    "solidity": 0.8662,
    "covex_area": 90591,
    "extent": 0.6123,
    "aspect_ratio": 1.7249,
    "roundness": 0.1775,
    "compactness": 0.7088,
    "shapefactor_1": 0.0057,
    "shapefactor_2": 0.0033,
    "shapefactor_3": 0.5024,
    "shapefactor_4": 0.8667
}

response = requests.post(url, json=pistachio).json()
print(response)