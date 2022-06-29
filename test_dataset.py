import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tkinter as tk
from IPython.display import display

def test_dataset():
    test = pd.read_csv("Dataset/test.csv")
    # filling numerical missing data
    test['LoanAmount']=test['LoanAmount'].fillna(test['LoanAmount'].mean())
    test['Loan_Amount_Term']=test['Loan_Amount_Term'].fillna(test['Loan_Amount_Term'].mean())
    test['Credit_History']=test['Credit_History'].fillna(test['Credit_History'].mean())

    # filling categorical missing data
    test['Gender']=test['Gender'].fillna(test['Gender'].mode()[0])
    test['Married']=test['Married'].fillna(test['Married'].mode()[0])
    test['Dependents']=test['Dependents'].fillna(test['Dependents'].mode()[0])
    test['Self_Employed']=test['Self_Employed'].fillna(test['Self_Employed'].mode()[0])

    test['Total_income'] = test['ApplicantIncome']+test['CoapplicantIncome']

    # apply log transformation to the attribute
    test['ApplicantIncomeLog'] = np.log(test['ApplicantIncome'])

    test['CoapplicantIncomeLog'] = np.log(test['CoapplicantIncome'])

    test['LoanAmountLog'] = np.log(test['LoanAmount'])

    test['Loan_Amount_Term_Log'] = np.log(test['Loan_Amount_Term'])

    test['Total_Income_Log'] = np.log(test['Total_income'])

    cols = ['ApplicantIncome', 'CoapplicantIncome', "LoanAmount", "Loan_Amount_Term", "Total_income", 'Loan_ID', 'CoapplicantIncomeLog']
    test = test.drop(columns=cols, axis=1)

    t1 = pd.get_dummies(test['Gender'], drop_first= True)
    t2 = pd.get_dummies(test['Married'], drop_first= True)
    t3 = pd.get_dummies(test['Dependents'], drop_first= True)
    t4 = pd.get_dummies(test['Education'], drop_first= True)
    t5 = pd.get_dummies(test['Self_Employed'], drop_first= True)
    t6 = pd.get_dummies(test['Property_Area'], drop_first= True)



    df1 = pd.concat([test, t1, t2, t3, t4, t5, t6], axis = 1)
    test=df1

    cols = ['Gender', 'Married', "Dependents", "Education", "Self_Employed", 'Property_Area']
    test = test.drop(columns=cols, axis=1)

    print("Successful")
    tk.Label(text="Successful", width=48, height=2, bg='green', fg='white').place(relx=0.6, rely=0.6)