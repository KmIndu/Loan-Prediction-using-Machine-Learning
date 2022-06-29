import tkinter as tk
from tkinter import *
import PIL
from PIL import ImageTk

import read_and_visualize_data
import handle_missing_data
import exploratory_data_analysis
import data_transformation
import handling_categorical_data
import test_dataset
import train_test_split
import train_model

def main():
    master = tk.Tk()
    master.title("Loan Eligibility Prediction")
    image2 = PIL.Image.open('static/images/backpic.jpg')
    image2 = image2.resize((1370, 750))
    image1 = ImageTk.PhotoImage(image2)
    background_label = tk.Label(master, image=image1)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    master.geometry("1480x700+0+0")

    label = Label(master, text="GENERATING MACHINE LEARNING MODEL FOR LOAN PREDICTION. ")
    label.config(font=("Arial", 31, "bold"))
    label.grid(row=0, column=0)

    tk.Button(text='Read and Visualize the data', command=lambda: read_and_visualize_data.read_and_visualize_data(), width=40, height=2, bg='red', fg='white').place(relx=0.3, rely=0.1)
    
    tk.Button(text='Handle numerical and categorical missing data', command=lambda: handle_missing_data.handle_missing_data(), width=40, height=2, bg='red', fg='white').place(relx=0.3, rely=0.2)

    tk.Button(text='Exploratory Data Analysis', command=lambda:exploratory_data_analysis.exploratory_data_analysis(), width=40, height=2, bg='red', fg='white').place(relx=0.3, rely=0.3)

    tk.Button(text='Data Transformation', command=lambda: data_transformation.data_transformation(), width=40, height=2, bg='red', fg='white').place(relx=0.3, rely=0.4)

    tk.Button(text='Handling Categorical Data', command=lambda: handling_categorical_data.handling_categorical_data(), width=40, height=2, bg='red', fg='white').place(relx=0.3, rely=0.5)

    tk.Button(text='Test Dataset', command=lambda: test_dataset.test_dataset(), width=40, height=2, bg='red', fg='white').place(relx=0.3, rely=0.6)

    tk.Button(text='Train Test Split', command=lambda: train_test_split.train_test_splitting(), width=40, height=2, bg='red', fg='white').place(relx=0.3, rely=0.7)

    tk.Button(text='Random Forest Classifier', command=lambda: train_model.random_forest_classifier(), width=20, height=2, bg='red', fg='white').place(relx=0.01, rely=0.8)
    tk.Button(text='Decision Tree Classifier', command=lambda: train_model.decision_tree_classifier(), width=20, height=2, bg='red', fg='white').place(relx=0.2, rely=0.8)
    tk.Button(text='Logistic Regression', command=lambda: train_model.logistic_regression(), width=20, height=2, bg='red', fg='white').place(relx=0.4, rely=0.8)

    master.mainloop()


if __name__ == '__main__':
    main()
