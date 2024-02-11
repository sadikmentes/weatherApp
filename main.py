import tkinter
from tkinter import *
from PIL import  ImageTk,Image
import requests


url = 'https://api.openweathermap.org/data/2.5/weather'
apiKey = 'fb1aca0210da0251690e24cb78a50c82'
iconUrl = 'https://openweathermap.org/img/wn/{}@2x.png'


def getWeather(city):
    params ={'q':city,'appid':apiKey,'lang':'tr'}
    data = requests.get(url,params=params).json()
    if data :
        city = data['name'].capitalize()
        country=data['sys']['country']
        temp=int(data['main']['temp']-273.15)
        icon = data['weather'][0]['icon']
        condition =data['weather'][0]['description']
        return city, country, temp, icon, condition


def main():
    city = myentry.get()
    weather = getWeather(city)
    if weather:
        locationLabel['text']='{},{}'.format(weather[0],weather[1])
        tempLabel['text'] ='{}°C'.format(weather[2])
        conditionsLabel['text'] = weather[4]
        icon =ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather[3]),stream=True).raw))
        iconLabel.config(image=icon)
        iconLabel.image = icon

my_font ="Arial", "24", "italic"
myColor = 'light gray'

window = tkinter.Tk()
window.geometry('350x450')
window.title('Hava Durumu')
window.config(bg=myColor)

myentry =Entry(window,font=my_font)
myentry.pack(fill=BOTH,ipady=8,padx=20, pady=10)
searchButton = Button(window, text="Arama", font=my_font, bg='#fffcbd', command=main)
searchButton.pack(fill=BOTH,ipady=1,padx=50)

iconLabel=Label(window,font=my_font,bg=myColor)
iconLabel.pack()

locationLabel=Label(window,font=my_font,bg=myColor)
locationLabel.pack()

tempLabel =Label(window,font=my_font,bg=myColor)
tempLabel.pack(pady=5)

conditionsLabel = Label(window,font=my_font,bg=myColor)
conditionsLabel.pack()



window.mainloop()





