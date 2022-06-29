import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tkinter as tk
from IPython.display import display

import seaborn as sns

def data_transformation():
    df=pd.read_csv("Dataset/train.csv")

    df['LoanAmount']=df['LoanAmount'].fillna(df['LoanAmount'].mean())
    df['Loan_Amount_Term']=df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean())
    df['Credit_History']=df['Credit_History'].fillna(df['Credit_History'].mean())

    display(df.columns)

    df['TotalIncome']=df['ApplicantIncome']+df['CoapplicantIncome']
    display(df.head())

    df['ApplicantIncomeLog']=np.log(df['ApplicantIncome'])
    sns.distplot(df.ApplicantIncomeLog)

    plt.show()

    # df['CoapplicantIncomeLog']=np.log(df['CoapplicantIncome'])
    # sns.distplot(df.CoapplicantIncomeLog)
    # plt.show()

    df['LoanAmountLog']=np.log(df['LoanAmount'])
    sns.distplot(df.LoanAmountLog)
    plt.show()

    df['Loan_Amount_TermLog']=np.log(df['Loan_Amount_Term'])
    sns.distplot(df.Loan_Amount_TermLog)
    plt.show()


    df['TotalIncomeLog']=np.log(df['TotalIncome'])
    sns.distplot(df.TotalIncomeLog)
    plt.show()

    display(df.head())

    cols = ['ApplicantIncome', 'CoapplicantIncome', "LoanAmount", "Loan_Amount_Term", "TotalIncome", 'Loan_ID']
    df = df.drop(columns=cols, axis=1)

    display(df.head())

    display(df.describe())

    print("Data transformed successfully")
    tk.Label(text="Data transformed successfully", width=48, height=2, bg='green', fg='white').place(relx=0.6, rely=0.4)