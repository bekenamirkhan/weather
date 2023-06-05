from tkinter import *
import requests
from PIL import ImageTk, Image
from tkinter import messagebox
from datetime import datetime
from collections import deque

w = Tk()
w.geometry('800x400')
w.iconbitmap('icon.ico')
w.title("Погода")
w.resizable(0, 0)

# Cтек для предыдущих городов
previous_cities = deque(maxlen=5)


try:
    # Механизм

    def weather_data(query):
        res = requests.get('http://api.openweathermap.org/data/2.5/weather?' + query + '&appid=7b7a32784b896be7d397f14d890b8309')
        return res.json()

    # Пользовательский интерфейс

    Frame(w, width=800, height=50, bg='#353535').place(x=0, y=0)

    # Строка поиска
    img1 = ImageTk.PhotoImage(Image.open("search.png"))

    def on_enter(e):
        e1.delete(0, 'end')

    def on_leave(e):
        if e1.get() == '':
            e1.insert(0, 'Поиск города')

    e1 = Entry(w, width=21, fg='white', bg="#353535", border=0)
    e1.config(font=('Calibri (Body)', 12))
    e1.bind("<FocusIn>", on_enter)
    e1.bind("<FocusOut>", on_leave)
    e1.insert(0, 'Поиск города')
    e1.place(x=620, y=15)

    # Дата
    a = datetime.today().strftime('%B')
    b = (a.upper())
    q = datetime.now()

    now = datetime.now()

    c = now.strftime('%B')
    month = c[0:3]

    today = datetime.today()
    date = today.strftime("%d")

    def label(a):
        Frame(width=500, height=50, bg="#353535").place(x=0, y=0)

        l2 = Label(w, text=str(a), bg="#353535", fg="white")  
        l2.config(font=("Microsoft JhengHei UI Light", 18))
        l2.place(x=20, y=8)

        city = a
        query = 'q=' + city
        w_data = weather_data(query)
        result = w_data

        try:
            check = "{}".format(result['main']['temp'])
            celsius = "{}".format(result['main']['temp'])
        except:
            messagebox.showinfo("", "    Такой город не найден    ")

        c = (int(float(check))) - 273
        descp = ("{}".format(result['weather'][0]['description']))
        weather = ("{}".format(result['weather'][0]['main']))

        global img

        if c > 10 and weather == "Haze" or weather == "Clear":
            Frame(w, width=800, height=350, bg="#f78954").place(x=0, y=50)
            img = ImageTk.PhotoImage(Image.open("sunny1.png"))
            Label(w, image=img, border=0).place(x=170, y=130)
            bcolor = "#f78954"
            fcolor = "white"

        elif c > 10 and weather == "Clouds":
            Frame(w, width=800, height=350, bg="#7492b3").place(x=0, y=50)
            img = ImageTk.PhotoImage(Image.open("cloudy1.png"))
            Label(w, image=img, border=0).place(x=170, y=130)
            bcolor = "#7492b3"
            fcolor = "white"

        elif c <= 10 and weather == "Clouds":
            Frame(w, width=800, height=350, bg="#7492b3").place(x=0, y=50)
            img = ImageTk.PhotoImage(Image.open("cloudcold.png"))
            Label(w, image=img, border=0).place(x=170, y=130)
            bcolor = "#7492b3"
            fcolor = "white"

        elif c > 10 and weather == "Rain":
            Frame(w, width=800, height=350, bg="#60789e").place(x=0, y=50)
            img = ImageTk.PhotoImage(Image.open("rain1.png"))
            Label(w, image=img, border=0).place(x=170, y=130)
            bcolor = "#60789e"
            fcolor = "white"

        elif c <= 10 and weather == "Fog" or weather == "Clear":
            Frame(w, width=800, height=350, bg="white").place(x=0, y=50)
            img = ImageTk.PhotoImage(Image.open("cold.png"))
            Label(w, image=img, border=0).place(x=170, y=130)
            bcolor = "white"
            fcolor = "black"

        else:
            Frame(w, width=800, height=350, bg="white").place(x=0, y=50)
            label = Label(w, text=weather, border=0, bg='white')
            label.configure(font=(("Microsoft JhengHei UI Light", 18)))
            label.place(x=160, y=130)
            bcolor = "white"
            fcolor = "black"

        w_data = weather_data(query)
        result = w_data

        e = ("Влажность: {}".format(result['main']['humidity']))
        f = ("Давление: {}".format(result['main']['pressure']))
        b1 = b = ("Скорость ветра: {} м/c".format(result['wind']['speed']))

        l5 = Label(w, text=str(month + "  " + date), bg=bcolor, fg=fcolor)  
        l5.config(font=("Microsoft JhengHei UI Light", 25))
        l5.place(x=330, y=335)

        l4 = Label(w, text=str(str(e + "%")), bg=bcolor, fg=fcolor)  
        l4.config(font=("Microsoft JhengHei UI Light", 11))
        l4.place(x=510, y=135)

        l4 = Label(w, text=str(str(f + " hPa")), bg=bcolor, fg=fcolor)  
        l4.config(font=("Microsoft JhengHei UI Light", 11))
        l4.place(x=510, y=175)

        l4 = Label(w, text=str(str(b1)), bg=bcolor, fg=fcolor)  
        l4.config(font=("Microsoft JhengHei UI Light", 11))
        l4.place(x=510, y=215)

        l3 = Label(w, text=str(str(c) + "°C"), bg=bcolor, fg=fcolor)  
        l3.config(font=("Microsoft JhengHei UI Light", 40))
        l3.place(x=330, y=150)

        # Добавление города в стек
        previous_cities.appendleft(city)

        # Отображание предыдущих города
        previous_cities_label = Label(w, text="Предыдущие города:", bg="#353535", fg="white")
        previous_cities_label.config(font=("Microsoft JhengHei UI Light", 12))
        previous_cities_label.place(x=20, y=50)

        for i, prev_city in enumerate(previous_cities):
            city_label = Label(w, text=prev_city, bg="#353535", fg="white")
            city_label.config(font=("Microsoft JhengHei UI Light", 12))
            city_label.place(x=20, y=80 + i * 30)

    label(a="Алматы")

    def cmd1():
        b = str(e1.get())
        label(str(b))

    Button(w, image=img1, command=cmd1, border=0).place(x=750, y=10)

except:
    Frame(w, width=800, height=400, bg='white').place(x=0, y=0)
    global imgx
    imgx = ImageTk.PhotoImage(Image.open("nointernet.png"))

    Label(w, image=imgx, border=0).pack(expand=True)

w.mainloop()