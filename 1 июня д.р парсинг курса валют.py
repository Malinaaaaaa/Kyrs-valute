import os
import sys
import requests
from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import showerror


def show_currency():
    currency = entry.get()
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    data = response.json()
    currency_data = data["Valute"].get(currency)
    if currency_data:
        name = currency_data["Name"]
        nominal = currency_data["Nominal"]
        rate = currency_data["Value"] / nominal
        rate = round(rate, 3)
        #nominal = currency_data["Nominal"]
        current_info.config(text=f"1 {name} равен \n"
                            f"{rate} рублей")
    else:
        current_info.config(text="Неверная валюта")


window = Tk()
window.geometry("500x500")
window.title("Курс валюты")
window.resizable(False, False)
window.iconbitmap("Курс.валют.ico")

welcome_text = Label(window, text="Курс валют", font=("Time New Roman", 20, "bold"))
welcome_text.pack()

entry = Entry(window)
entry.pack(pady=10)
entry.focus()

btn = Button(window, text="Показать курс", command=show_currency)
btn.pack(pady=10)

picture = Label(window)
picture.pack()

current_info = Label(window, font=("Time new Roman", 20, "bold"))
current_info.pack()
window.mainloop()