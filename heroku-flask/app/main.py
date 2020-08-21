from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__) 
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/") 
def home_view(): 
        return render_template('index.html')

@app.route("/civilization") 
def get_civilization_information():
    civilization = request.args.get('civilization') 
    print("civilization: ", civilization)
    url = "https://age-of-empires-2-api.herokuapp.com/api/v1/civilization/" + civilization
    response = requests.request("GET", url)
    print("response: ", response)
    return response.text.encode('utf8')
    

