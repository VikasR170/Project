# Importing Libraries

from tkinter import *
from tkinter import ttk
import requests
import datetime

def data_get():
    city = city_name.get()
    try:
        # API request to fetch weather data
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=33562e31646303a38c7f9374680f93d1"
        ).json()

        if data.get("cod") != 200:
            error_label.config(text="Invalid city name. Please try again!")
            return

        # Update labels with weather data
        error_label.config(text="")
        w_label1.config(text=data["weather"][0]["main"])
        wb_label2.config(text=data["weather"][0]["description"])
        temp_label3.config(text=str(round(data["main"]["temp"] - 273.15, 2)) + " °C")
        pressure_label4.config(text=str(data["main"]["pressure"]) + " hPa")
        humidity_label5.config(text=str(data["main"]["humidity"]) + " %")
        wind_label6.config(text=str(data["wind"]["speed"]) + " m/s")
        visibility_label7.config(text=str(data["visibility"]) + " m")
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M:%S')
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M:%S')
        sunrise_label8.config(text=sunrise)
        sunset_label9.config(text=sunset)

    except Exception as e:
        error_label.config(text="An error occurred. Please check your connection or API key!")

# Create the main window
win = Tk()
win.title("WeatherWise App")
win.config(bg="dark grey")
win.geometry("600x700")

name_label = Label(win, text="WeatherWise App", font=("Times New Roman", 30, "bold"))
name_label.place(x=50, y=20, height=50, width=500)

city_name = StringVar()

list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

com = ttk.Combobox(win, values=list_name, font=("Times New Roman", 25, "bold"), textvariable=city_name)
com.place(x=50, y=100, height=50, width=500)

button = Button(win, text="Fetch Weather", font=("Times New Roman", 15, "bold"), command=data_get)
button.place(y=160, height=50, width=200, x=200)

error_label = Label(win, text="", font=("Times New Roman", 12, "bold"), fg="red")
error_label.place(x=50, y=220, width=500)

# Weather details sections
Label(win, text="Weather Climate", font=("Times New Roman", 15)).place(x=50, y=260, height=40, width=210)
w_label1 = Label(win, text=" ", font=("Times New Roman", 15))
w_label1.place(x=280, y=260, height=40, width=210)

Label(win, text="Weather Description", font=("Times New Roman", 15)).place(x=50, y=310, height=40, width=210)
wb_label2 = Label(win, text=" ", font=("Times New Roman", 15))
wb_label2.place(x=280, y=310, height=40, width=210)

Label(win, text="Temperature (Celsius)", font=("Times New Roman", 15)).place(x=50, y=360, height=40, width=210)
temp_label3 = Label(win, text=" ", font=("Times New Roman", 15))
temp_label3.place(x=280, y=360, height=40, width=210)

Label(win, text="Pressure (hPa)", font=("Times New Roman", 15)).place(x=50, y=410, height=40, width=210)
pressure_label4 = Label(win, text=" ", font=("Times New Roman", 15))
pressure_label4.place(x=280, y=410, height=40, width=210)

Label(win, text="Humidity (%)", font=("Times New Roman", 15)).place(x=50, y=460, height=40, width=210)
humidity_label5 = Label(win, text=" ", font=("Times New Roman", 15))
humidity_label5.place(x=280, y=460, height=40, width=210)

Label(win, text="Wind Speed (m/s)", font=("Times New Roman", 15)).place(x=50, y=510, height=40, width=210)
wind_label6 = Label(win, text=" ", font=("Times New Roman", 15))
wind_label6.place(x=280, y=510, height=40, width=210)

Label(win, text="Visibility (m)", font=("Times New Roman", 15)).place(x=50, y=560, height=40, width=210)
visibility_label7 = Label(win, text=" ", font=("Times New Roman", 15))
visibility_label7.place(x=280, y=560, height=40, width=210)

Label(win, text="Sunrise (HH:MM:SS)", font=("Times New Roman", 15)).place(x=50, y=610, height=40, width=210)
sunrise_label8 = Label(win, text=" ", font=("Times New Roman", 15))
sunrise_label8.place(x=280, y=610, height=40, width=210)

Label(win, text="Sunset (HH:MM:SS)", font=("Times New Roman", 15)).place(x=50, y=660, height=40, width=210)
sunset_label9 = Label(win, text=" ", font=("Times New Roman", 15))
sunset_label9.place(x=280, y=660, height=40, width=210)

win.mainloop()
