from tkinter import *
from tkinter import ttk

import requests
def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a09a6922b205bb1701b502ebb0a3612f").json()
    wc1.config(text=data["weather"][0]["main"])
    wtemp1.config(text=str(int(data["main"]["temp"]-273.15))+"ºC")
    wp1.config(text=data["main"]["pressure"])
    wd1.config(text=data["weather"][0]["description"])

win= Tk()
win.title("WHETHER APP")
win.config(bg ="sky blue")
win.geometry("500x570")

name_label=Label(win,text="whether App", font=("Arial" ,40, "bold"))
name_label.place(x=25,y=50,height=50,width=450)
listname= ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

city_name=StringVar()

com=ttk.Combobox(win,text="whether app",values=listname,font=("Arial",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

wc=Button(win,text="Wheather cliamate",font=("Arial",17,"bold"))
wc.place(y=260,height=50,width=232,x=25)
wc1=Button(win,text="",font=("Arial",17,"bold"))
wc1.place(y=260,height=50,width=232,x=260)
       
wd=Button(win,text="whether description",font=("Arial",17,"bold"))
wd.place(y=330,height=50,width=232,x=25)
wd1=Button(win,text="",font=("Arial",17,"bold"))
wd1.place(y=330,height=50,width=232,x=260)
       
wtemp=Button(win,text="Temperature",font=("Arial",17,"bold"))
wtemp.place(y=400,height=50,width=232,x=25)
wtemp1=Button(win,text="",font=("Arial",17,"bold"))
wtemp1.place(y=400,height=50,width=232,x=260)

wp=Button(win,text="pressure",font=("Arial",17,"bold"))
wp.place(y=470,height=50,width=232,x=25)
wp1=Button(win,text="",font=("Arial",17,"bold"))
wp1.place(y=470,height=50,width=232,x=260)

wc=Button(win,text="Done",font=("Arial",17,"bold"),command=data_get)
wc.place(y=190,height=50,width=100,x=200)

win.mainloop()

