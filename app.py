from flask import Flask
from flask import Flask, request, make_response
import os, json
from flask_cors import CORS,cross_origin
from weather_data import WeatherData

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

# geting and sending response to dialogflow
@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    
    print(json.dumps(req))

    res = object.processRequest(req)

    res = json.dumps(res)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == '__main__':
    object=WeatherData()
    #port = int(os.getenv('PORT', 5000))
    #print("Starting app on port %d" % port)
    app.run(debug=True)

#if __name__=='__main__':
    #app.run(host='0.0.0.0',port=8080)
