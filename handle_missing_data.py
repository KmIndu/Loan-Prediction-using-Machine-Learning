import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tkinter as tk
from IPython.display import display

from read_and_visualize_data import read_and_visualize_data

def handle_missing_data():
    df=pd.read_csv("Dataset/train.csv")

    display(df.isnull().sum())

    df['LoanAmount']=df['LoanAmount'].fillna(df['LoanAmount'].mean())
    df['Loan_Amount_Term']=df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean())
    df['Credit_History']=df['Credit_History'].fillna(df['Credit_History'].mean())

    df['Gender']=df['Gender'].fillna(df['Gender'].mode()[0])
    df['Married']=df['Married'].fillna(df['Married'].mode()[0])
    df['Dependents']=df['Dependents'].fillna(df['Dependents'].mode()[0])
    df['Self_Employed']=df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])

    display(df.isnull().sum())

    print("Handled numerical and categorical missing data successfully")
    tk.Label(text="Handled numerical and categorical missing data successfully", width=48, height=2, bg='green', fg='white').place(relx=0.6, rely=0.2)
    
    