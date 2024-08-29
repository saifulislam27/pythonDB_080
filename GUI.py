import tkinter as tk 
from tkinter import *

jendela = tk.Tk()
jendela.title("Aplikasi Prodi Pilihan") 

jendela.configure(bg='#123456') 
matematika = tk.DoubleVar() 
inggris = tk.DoubleVar() 
geografi = tk.DoubleVar()


def prediksi() :
 if int(geografi.get()) < 75 or int(inggris.get()) < 75 or int(matematika.get()) < 75 :
     hasil_label.config(text="Tidak Lulus")
 elif int(matematika.get()) > int(geografi.get()) and int(matematika.get()) > int(inggris.get()) :
     hasil_label.config(text="Kedokteran")
 elif int(geografi.get()) > int(matematika.get()) and int(geografi.get()) > int(inggris.get()) :
     hasil_label.config(text="Teknik")
 elif int(inggris.get()) > int(geografi.get()) and int(inggris.get()) > int(matematika.get()) :
     hasil_label.config(text="Bahasa")

geografi_label = tk.Label(master=jendela, text=f'Nilai Geografi',
    font=('Inter', 12), fg='#FFFFFF', bg='#0C356A') 
geografi_label.place (relx=0.5, rely=0.15, anchor='center') 

geografi = tk.Entry(master=jendela, font=('Inter', 12), width=30, fg='#FFFFFF',
    bg='#0C356A', highlightcolor='#FFF0CE', highlightthickness=2,textvariable=geografi) 
geografi.place (relx=0.5, rely=0.22, anchor='center') 

matematika_label = tk.Label(master=jendela, text=f'Nilai Matematika',
    font=('Inter', 12), fg='#FFFFFF', bg='#0C356A') 
matematika_label.place (relx=0.5, rely=0.28, anchor='center')

matematika = tk.Entry(master=jendela, font=('Inter', 12), width=30, fg='#FFFFFF',
    bg='#0C356A', highlightcolor="#FFF0CE", highlightthickness=2,textvariable=matematika)
matematika.place (relx=0.5, rely=0.32, anchor='center')

bahasa_inggris_label = tk.Label(master=jendela, text=f'Nilai bahasa inggris',
    font=('Inter', 12), fg='#FFFFFF', bg='#0C356A')
bahasa_inggris_label.place (relx=0.5, rely=0.38, anchor='center')

bahasa_inggris = tk.Entry(master=jendela, font=('Inter', 12), width=30, fg='#FFFFFF',
    bg='#0C356A', highlightcolor="#FFF0CE", highlightthickness=2, textvariable=inggris)
bahasa_inggris.place (relx=0.5, rely=0.42, anchor='center')

prediksi_button = tk.Button(jendela, text='prediksi', command=prediksi)
prediksi_button.pack()

hasil_label = tk.Label(jendela, text= prediksi)
hasil_label.pack(pady=20)

jendela.mainloop()