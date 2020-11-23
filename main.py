from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
apiKey = '' #get your api key from openweather.com


def search(event=None):
    global cityLabel, imgLabel, tempLabel, weatherLabel
    global img
    City = city.get()

    try:
        weather = get_weather(City)
        cityLabel['text'] = f'{weather[0]}, {weather[1]}'
        img['file'] = f"F:\\Python\\PythonProjects\\Weather App\\WeatherIcons\\{weather[3]}@2x.png"
        tempLabel['text'] = '{:.2f}°C'.format(weather[2])
        weatherLabel['text'] = f"{weather[4]}"
    except Exception:
        messagebox.showerror("Error", "No such city found")


def get_weather(city):
    result = requests.get(url.format(city, apiKey))
    json = result.json()

    city = json["name"]
    country = json['sys']['country']
    temp_kelvin = json['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    icon = json['weather'][0]['icon']
    weather = json['weather'][0]['main']
    return (city, country, temp_celsius, icon, weather)


if __name__ == "__main__":
    root = Tk()
    root.geometry("700x350")
    root.title("Weather")

    Label(text="Weather App ~ By Krish Bista", font="Bebas 20 bold underline",
          fg='royal blue').pack(pady=10, anchor='n')

    city = Entry(root, font="Arial 20 bold", justify=CENTER,)
    city.pack(ipadx=50, pady=4)

    Button(text="Search", font="Verdena 15 bold",
           relief=GROOVE, width=12, bd=3, activebackground='khaki', bg='snow3', command=search).pack()

    root.bind("<Return>", search)

    cityLabel = Label(text='', font="bold 15")
    cityLabel.pack()

    img = PhotoImage(file='')
    imgLabel = Label(image=img)
    imgLabel.pack()

    tempLabel = Label(text='', font='arial 12')
    tempLabel.pack()

    weatherLabel = Label(text='', font='arial 12')
    weatherLabel.pack()
    root.mainloop()
