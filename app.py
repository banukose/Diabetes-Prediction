
from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np


app = Flask(__name__, template_folder = "templates")

@app.route("/")

@app.route("/Diabetes")
def cancer():
    return render_template("diabetes.html")

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if (size == 6):
        loaded_model = joblib.load("./diabetes_model.pkl")
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route("/predict", methods= ["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        
        if (len(to_predict_list) == 6):
            result = ValuePredictor(to_predict_list, 6)
            
    if(int(result)==1):
        prediction = "You have chances of getting the disease. Please consult the doctor immediately."
    else:
        prediction = "You have no dangerous symptoms of the disease."
    return(render_template("result.html", prediction_text=prediction))       

if __name__ == "__main__":
    app.run(debug=True)
    
            