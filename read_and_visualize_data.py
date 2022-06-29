import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tkinter as tk
from IPython.display import display

def read_and_visualize_data():
    df=pd.read_csv("Dataset/train.csv")
    display(df)
    print("Read and Visualized the data successfully")
    tk.Label(text="Read and Visualized the data successfully", width=48, height=2, bg='green', fg='white').place(relx=0.6, rely=0.1)