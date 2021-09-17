# Load libraries
import flask
import pandas as pd
import numpy as np
from keras.models import load_model
import joblib
from flask_cors import cross_origin
# Instantiate flask
app = flask.Flask(__name__)

# Define welcome api function
@app.route("/")
def index():
    response = flask.jsonify({
       "statusCode": 200,
       "response": "Welcome to the ML REST API.:)"
    })

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
	
	
# Define a predict function as an endpoint
@app.route("/predict", methods=["GET", "POST","OPTIONS"])
@cross_origin()
def predict():
    data = {"result": None}
    
    if flask.request.method in ["POST","OPTIONS"]:
        #print(flask.request,dir(flask.request))
        params = flask.request.json
        #print(params,flask.request.get_data(),flask.request.get_json(),flask.request.data)
        print(params)
        if params == None:
            params = flask.request.args

        # if parameters are found, return a prediction
        if params != None:
            query=pd.DataFrame(params,index=['i',])
            query=query.reindex(columns=model_columns)
            query=query.to_numpy()
            predictions=model.predict(query)
            response=result_columns[predictions.argmax()]
            data["result"] = response
    else:
        data["body"] = "Provide a JSON Dict for prediction."
    # return a response in json format
    print(data)
    response=flask.jsonify(data)

    print(response)
    return response
	
if __name__ == "__main__":
    model=load_model("predictor.h5")
    model_columns=joblib.load("columns.pkl")
    result_columns=joblib.load("result_columns.pkl")
    print(model_columns,result_columns)
    # Run App
    app.run(host="0.0.0.0", port=5555