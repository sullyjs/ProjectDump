import tkinter as tk
import requests
from tkinter import font


HEIGHT= 500
WIDTH = 600

def function(entry):
    print("this is the entry:" , entry)
    
def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        
        final_str = "City: %s \nConditions: %s \nTemperature (C): %s" % (name, desc, temp)
    except:
        final_str = "There was a problem retrieving that information"
    
    return final_str
        
    
    
#pro.openweathermap.org/data/2.5/forecast/hourly?q={city name},{country code}
#17d6db06c50f14cc3203e75e3055b591
    
def get_weather(city):
    weather_key = "17d6db06c50f14cc3203e75e3055b591"
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    
    label['text'] = format_response(weather)

root = tk.Tk()
root.title("Weather App")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#fix so it will fill whole screen

#bg_img = tk.PhotoImage(file='bg2.jpg')
bg_label = tk.Label(root, bg='black')
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#80c1ff", bd="5")
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40) #input
entry.place(relwidth=0.65, relheight=1)

#button = tk.Button(frame, text="Get Weather", font=40, command=Lambda: function(entry.get()))
button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
                       
label = tk.Label(lower_frame, font=("Calibri", 14), anchor='nw', justify='left', bd=-4)
label.place(relwidth=1, relheight=1)

root.mainloop()