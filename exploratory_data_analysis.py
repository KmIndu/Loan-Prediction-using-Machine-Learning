import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tkinter as tk
from IPython.display import display

import seaborn as sns

def exploratory_data_analysis():
    df=pd.read_csv("Dataset/train.csv")
    
    sns.countplot(df.Gender)
    plt.show()
    sns.countplot(df.Married)
    plt.show()
    sns.countplot(df.Dependents)
    plt.show()
    sns.countplot(df.Education)
    plt.show()
    sns.countplot(df.Property_Area)
    plt.show()
    sns.countplot(df.Loan_Status)
    plt.show()

    display(df.columns)

    sns.distplot(df.ApplicantIncome)
    plt.show()
    sns.distplot(df.CoapplicantIncome)
    plt.show()
    sns.distplot(df.LoanAmount)
    plt.show()
    sns.distplot(df.Loan_Amount_Term)
    plt.show()
    sns.distplot(df.Credit_History)
    plt.show()

    print("Exploratory data analysed successfully")
    tk.Label(text="Exploratory data analysed successfully", width=48, height=2, bg='green', fg='white').place(relx=0.6, rely=0.3)