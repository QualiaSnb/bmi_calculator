from tkinter import *

calculator_window = Tk()
calculator_window.geometry("250x150")
calculator_window.title("BMI Calculator")

result = ""
def bmi_calculator():
    global result
    w = weight_entry.get()
    h1 = height_entry.get()
    def result_string():
        global result
        if bmi < 16:
            result = f"{bmi} is your body mass index. \nYou are severely underweight."
        elif 16 <= bmi < 18.4:
            result = f"{bmi} is your body mass index. \nYou are underweight."
        elif 18.5 <= bmi < 24.9:
            result = f"{bmi} is your body mass index. \nYou are normal."
        elif 25.0 <= bmi < 29.9:
            result = f"{bmi} is your body mass index. \nYou are overweight."
        elif 30.0 <= bmi < 34.9:
            result = f"{bmi} is your body mass index. \nYou are moderately obese."
        elif 35.0 <= bmi < 39.9:
            result = f"{bmi} is your body mass index. \nYou are severely obese."
        elif bmi >= 40:
            result = f"{bmi} is your body mass index. \nYou are morbidly obese."
    if w == "" or h1 == "":
        result_label.config( text= "Enter both weight and height!")
    else:
        try:
            h2 = float(h1) / 100
            w2 = float(w)
            bmi = int(w2 / (h2 * h2))
            print(bmi)
            result_string()
            result_label.config(text= f"{result}",font=("ariel", 10,"normal"))
            print(result)

        except:
            result_label.config( text= "Enter a valid number!")



weight_label = Label(text="Enter your weight (kg)", font=("ariel", 10,"bold"))
weight_label.pack()

weight_entry = Entry()
weight_entry.pack()

height_label = Label(text="Enter your height (cm)", font=("ariel", 10,"bold"))
height_label.pack()

height_entry = Entry()
height_entry.pack()

calculate_button = Button(text= "Calculate", command= bmi_calculator)
calculate_button.pack()

result_label = Label()
result_label.pack()

calculator_window.mainloop()