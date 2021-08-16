import pickle as pk
import numpy as np
import pandas as pd
from flask import Flask, request, render_template

# Flask constructor
application = Flask(__name__)
@application.route('/')
def home():
  return render_template("index.html")

# A decorator used to tell the application
# which URL is associated function
# prediction function


filename = 'finalized_titanic_model.pk'
loaded_model = pk.load(open(filename, 'rb'))


@application.route('/result', methods=['POST'])
def result():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        Pclass = float(request.form.get("Pclass"))
        Age = float(request.form.get("Age"))
        # getting input with name = lname in HTML form
        SibSp = float(request.form.get("SibSp"))
        Parch = float(request.form.get("Parch"))
        Fare = float(request.form.get("Fare"))
        Cabin_missing = request.form.get("Cabin_missing")
        Age_missing = request.form.get("Age_missing")
        Ticket_length = float(request.form.get("Ticket_length"))
        Sex = request.form.get("Sex")
        Embarked = request.form.get("Embarked")
        if Cabin_missing == "yes":
            ye = 1
        else:
            ye = 0
        if Age_missing == "yes":
            am = 1
        else:
            am = 0
        if Sex == "male":
            fe = 0;
            ma = 1;
        else:
            fe = 1;
            ma = 0;
        if Embarked == "Embarked_S":
            Embarked_S = 1
            Embarked_C = 0
        elif Embarked == "Embarked_C":
            Embarked_S = 0
            Embarked_C = 1
        else:
            Embarked_S = 0
            Embarked_C = 0

        predictionresult = loaded_model.predict(
            [[Pclass, Age, SibSp, Parch, Fare, Ticket_length, ye, am, fe, Embarked_S, Embarked_C]])
        if int(predictionresult) == 1:
            predictionresult = 'SURVIVED'
        else:
            predictionresult = ' NOT SURVIVED'

    return render_template("result.html", prediction=predictionresult)

if __name__ == '__main__':
    application.run(debug=True)
    application.config["TEMPLATES_AUTO_RELOAD"]=True
