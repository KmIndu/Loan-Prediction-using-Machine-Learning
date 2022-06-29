import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tkinter as tk
from IPython.display import display

from sklearn.model_selection import train_test_split

def train_test_splitting():
    df=pd.read_csv("Dataset/train.csv")

    df['LoanAmount']=df['LoanAmount'].fillna(df['LoanAmount'].mean())
    df['Loan_Amount_Term']=df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean())
    df['Credit_History']=df['Credit_History'].fillna(df['Credit_History'].mean())

    df['Gender']=df['Gender'].fillna(df['Gender'].mode()[0])
    df['Married']=df['Married'].fillna(df['Married'].mode()[0])
    df['Dependents']=df['Dependents'].fillna(df['Dependents'].mode()[0])
    df['Self_Employed']=df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])

    df['TotalIncome']=df['ApplicantIncome']+df['CoapplicantIncome']
    df['ApplicantIncomeLog']=np.log(df['ApplicantIncome'])
    df['LoanAmountLog']=np.log(df['LoanAmount'])
    df['Loan_Amount_TermLog']=np.log(df['Loan_Amount_Term'])
    df['TotalIncomeLog']=np.log(df['TotalIncome'])

    cols = ['ApplicantIncome', 'CoapplicantIncome', "LoanAmount", "Loan_Amount_Term", "TotalIncome", 'Loan_ID']
    df = df.drop(columns=cols, axis=1)


    d1 = pd.get_dummies(df['Gender'], drop_first= True)
    d2 = pd.get_dummies(df['Married'], drop_first= True)
    d3 = pd.get_dummies(df['Dependents'], drop_first= True)
    d4 = pd.get_dummies(df['Education'], drop_first= True)
    d5 = pd.get_dummies(df['Self_Employed'], drop_first= True)
    d6 = pd.get_dummies(df['Property_Area'], drop_first= True)



    df1 = pd.concat([df, d1, d2, d3, d4, d5, d6], axis = 1)
    df=df1

    cols = ['Gender', 'Married', "Dependents", "Education", "Self_Employed", 'Property_Area']
    df = df.drop(columns=cols, axis=1)

    display(df.head())

    x = df.drop(columns=['Loan_Status'], axis=1)
    y = df['Loan_Status']

    display(x)
    display(y)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

    display(x_train.head())
    display(y_test.head())

    print("Training Testing data splitted successfully")
    tk.Label(text="Training Testing data splitted successfully", width=48, height=2, bg='green', fg='white').place(relx=0.6, rely=0.7)