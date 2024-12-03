from tkinter import *
from tkinter import messagebox
import numpy as np
from MyDecisionTreeBear import MyDecisionTreeBear

window = Tk()
window.geometry("400x600")
window.title("Bear Prediction")
window.resizable(False, False)
window.configure(bg="#f0f0f0")

decisionTree = MyDecisionTreeBear()

def trainData():
    newSeedValue = int(seedsVar.get())
    decisionTree.preprocess_data(newSeedValue)
    decisionTree.trainData()
    messagebox.showinfo("Success", "Training Complete!")

def testData():
    text.delete("1.0", "end")

    result, accuracy, confusion_mat = decisionTree.testData()

    text.insert(END, 'Confusion Matrix:\n')
    text.insert(END, str(confusion_mat))
    text.insert(END, '\nAccuracy: ' + str(int(accuracy * 100)) + '%\n')

def makeNewPrediction():
    try:
        age = float(entry_age.get())
        gender = entry_gender.get().capitalize()
        month = entry_month.get().capitalize()
        year = int(entry_year.get())
        encounter_type = entry_type.get().capitalize()


        if gender not in ['Male', 'Female']:
            messagebox.showerror("Input Error", "Gender must be 'Male' or 'Female'.")
            return
        if encounter_type not in ['Wild', 'Captive']:
            messagebox.showerror("Input Error", "Encounter type must be 'Wild' or 'Captive'.")
            return

        prediction = decisionTree.makePrediction(age, gender, month, year, encounter_type)
        entry_prediction.delete(0, END)
        entry_prediction.insert(END, prediction)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid input.")

frame = Frame(window, bg="#ffffff", padx=20, pady=20)
frame.pack(pady=10)

label0 = Label(window, text="Bear Predictor", fg="blue", bg="#f0f0f0", font=("Arial", 18, "bold"))
label0.pack(pady=(10, 10))

label_seed = Label(frame, text="Enter Seed Value:", fg="red", font=("Arial", 12, "bold"))
label_seed.grid(row=0, column=0, columnspan=2)

list1 = ['1', '2', '3', '4', '5']
seedsVar = StringVar()
combo1 = OptionMenu(frame, seedsVar, *list1)
seedsVar.set("1")  # Default seed value
combo1.grid(row=1, column=0, sticky=W + E, padx=(0, 10))

button_train = Button(frame, text="Train Data", fg="black", font=("Arial", 10, "bold"), command=trainData)
button_train.grid(row=1, column=1, sticky=W + E)

button_test = Button(frame, text="Test Data", fg="black", font=("Arial", 10, "bold"), command=testData)
button_test.grid(row=2, column=0, columnspan=2, pady=(10, 0), sticky=W + E)

label_output = Label(frame, text="Output", fg="blue", font=("Arial", 10, "bold"))
label_output.grid(row=3, column=0, columnspan=2)

text = Text(frame, height=3, width=40, wrap=WORD)
text.grid(row=4, column=0, columnspan=2, pady=(5, 10))

label_new_data = Label(frame, text="Make New Prediction", fg="red", font=("Arial", 14, "bold"))
label_new_data.grid(row=5, column=0, columnspan=2, pady=(10, 5))

label_age = Label(frame, text="Age:", fg="blue", font=("Arial", 10, "bold"))
label_age.grid(row=6, column=0, sticky=W + E)
entry_age = Entry(frame, width=20)
entry_age.grid(row=6, column=1, sticky=W + E, pady=(0, 5))

label_gender = Label(frame, text="Gender (Male/Female):", fg="blue", font=("Arial", 10, "bold"))
label_gender.grid(row=7, column=0, sticky=W + E)
entry_gender = Entry(frame, width=20)
entry_gender.grid(row=7, column=1, sticky=W + E, pady=(0, 5))

label_month = Label(frame, text="Month (e.g. Mar):", fg="blue", font=("Arial", 10, "bold"))
label_month.grid(row=8, column=0, sticky=W + E)
entry_month = Entry(frame, width=20)
entry_month.grid(row=8, column=1, sticky=W + E, pady=(0, 5))

label_year = Label(frame, text="Year (e.g. 1999):", fg="blue", font=("Arial", 10, "bold"))
label_year.grid(row=9, column=0, sticky=W + E)
entry_year = Entry(frame, width=20)
entry_year.grid(row=9, column=1, sticky=W + E, pady=(0, 5))

label_type = Label(frame, text="Encounter Type (Wild/Captive):", fg="blue", font=("Arial", 10, "bold"))
label_type.grid(row=10, column=0, sticky=W + E)
entry_type = Entry(frame, width=20)
entry_type.grid(row=10, column=1, sticky=W + E, pady=(0, 5))

button_predict = Button(frame, text="Make Prediction", fg="black", font=("Arial", 10, "bold"), command=makeNewPrediction)
button_predict.grid(row=11, column=0, columnspan=2, pady=(10, 0), sticky=W + E)

label_prediction = Label(frame, text="Prediction:", fg="blue", font=("Arial", 10, "bold"))
label_prediction.grid(row=12, column=0, sticky=W + E)
entry_prediction = Entry(frame, width=20)
entry_prediction.grid(row=12, column=1, sticky=W + E)

mainloop()
