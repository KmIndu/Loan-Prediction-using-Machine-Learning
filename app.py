import flask
from flask import Flask, escape, request, render_template
import pickle
import numpy as np

import mysql.connector

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method ==  'POST':
        gender = flask.request.form['gender']
        married = flask.request.form['married']
        dependents = flask.request.form['dependents']
        education = flask.request.form['education']
        self_employed = flask.request.form['self_employed']
        credit_history = int(flask.request.form['credit_history'])
        property_area = flask.request.form['property_area']
        applicantincome = float(flask.request.form['applicantincome'])
        coapplicantincome = float(flask.request.form['coapplicantincome'])
        loanamount = float(flask.request.form['loanamount'])
        loan_amount_term = int(flask.request.form['loan_amount_term'])

        # gender
        if (gender == "Male"):
            male=1
        else:
            male=0
        
        # married
        if(married=="Yes"):
            married_yes = 1
        else:
            married_yes=0

        # dependents
        if(dependents=='1'):
            dependents_1 = 1
            dependents_2 = 0
            dependents_3 = 0
        elif(dependents == '2'):
            dependents_1 = 0
            dependents_2 = 1
            dependents_3 = 0
        elif(dependents=="3+"):
            dependents_1 = 0
            dependents_2 = 0
            dependents_3 = 1
        else:
            dependents_1 = 0
            dependents_2 = 0
            dependents_3 = 0  

        # education
        if (education=="Not Graduate"):
            not_graduate=1
        else:
            not_graduate=0

        # self_employed
        if (self_employed == "Yes"):
            self_employed_yes=1
        else:
            self_employed_yes=0

        # property_area

        if(property_area=="Semiurban"):
            semiurban=1
            urban=0
        elif(property_area=="Urban"):
            semiurban=0
            urban=1
        else:
            semiurban=0
            urban=0


        applicantincomelog = np.log(applicantincome)
        totalincomelog = np.log(applicantincome+coapplicantincome)
        loanamountlog = np.log(loanamount)
        loan_amount_termlog = np.log(loan_amount_term)

        prediction = model.predict([[credit_history , applicantincomelog, loanamountlog, loan_amount_termlog, totalincomelog, male, married_yes, dependents_1, dependents_2, dependents_3, not_graduate, self_employed_yes,semiurban, urban]])

        # print(prediction)

        if(prediction=="N"):
            prediction="😔😔Unfortunatly you are not eligible for taking loan.😔😔"
        else:
            prediction="🎊🎊Congratulations! You are eligibile for taking loan!🎊🎊"


        return render_template("prediction.html", prediction_text="{}".format(prediction))

    else:
        return render_template("prediction.html")

@app.route('/about')
def about():
    return (flask.render_template('about.html'))

@app.route('/contact', methods =["GET", "POST"])
def contact():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="loan_db"
    )
    mycursor=mydb.cursor()
    if request.method == "POST":
       result=request.form.to_dict()
       user = request.form["user"]
       email = request.form["email"]
       mobile = request.form["mobile"]
       comments = request.form["comments"]
       mycursor.execute("insert into infofromcontactus(user, email, mobile, comments) values(%s, %s, %s, %s)", (user, email, mobile, comments))
       mydb.commit()
       mycursor.close()
       return "Your response is successfully submitted !"
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)