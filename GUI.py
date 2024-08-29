import sqlite3
import tkinter as tk 
from tkinter import *

conn = sqlite3.connect('nilai_siswa.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS prodi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matematika REAL,
    bahasa_inggris REAL,
    geografi REAL,
    prediksi TEXT
)
''')
conn.commit()

jendela = tk.Tk()
jendela.title("Aplikasi Prodi Pilihan") 
jendela.configure(bg='#123456') 

matematika = tk.DoubleVar() 
inggris = tk.DoubleVar() 
geografi = tk.DoubleVar()

def prediksi():
    mat_value = int(matematika.get())
    geo_value = int(geografi.get())
    eng_value = int(inggris.get())
    
    if geo_value < 75 or eng_value < 75 or mat_value < 75:
        hasil = "Tidak Lulus"
    elif mat_value > geo_value and mat_value > eng_value:
        hasil = "Kedokteran"
    elif geo_value > mat_value and geo_value > eng_value:
        hasil = "Teknik"
    elif eng_value > geo_value and eng_value > mat_value:
        hasil = "Bahasa"
    
    hasil_label.config(text=hasil)
    
    cursor.execute('''
    INSERT INTO prodi (matematika, bahasa_inggris, geografi, prediksi)
    VALUES (?, ?, ?, ?)''', (mat_value, eng_value, geo_value, hasil))
    conn.commit()

geografi_label = tk.Label(master=jendela, text=f'Nilai Geografi',
    font=('Inter', 12), fg='#FFFFFF', bg='#0C356A') 
geografi_label.place (relx=0.5, rely=0.15, anchor='center') 

geografi = tk.Entry(master=jendela, font=('Inter', 12), width=30, fg='#FFFFFF',
    bg='#0C356A', highlightcolor='#FFF0CE', highlightthickness=2, textvariable=geografi) 
geografi.place (relx=0.5, rely=0.22, anchor='center') 

matematika_label = tk.Label(master=jendela, text=f'Nilai Matematika',
    font=('Inter', 12), fg='#FFFFFF', bg='#0C356A') 
matematika_label.place (relx=0.5, rely=0.28, anchor='center')

matematika = tk.Entry(master=jendela, font=('Inter', 12), width=30, fg='#FFFFFF',
    bg='#0C356A', highlightcolor="#FFF0CE", highlightthickness=2, textvariable=matematika)
matematika.place (relx=0.5, rely=0.32, anchor='center')

bahasa_inggris_label = tk.Label(master=jendela, text=f'Nilai bahasa inggris',
    font=('Inter', 12), fg='#FFFFFF', bg='#0C356A')
bahasa_inggris_label.place (relx=0.5, rely=0.38, anchor='center')

bahasa_inggris = tk.Entry(master=jendela, font=('Inter', 12), width=30, fg='#FFFFFF',
    bg='#0C356A', highlightcolor="#FFF0CE", highlightthickness=2, textvariable=inggris)
bahasa_inggris.place (relx=0.5, rely=0.42, anchor='center')

prediksi_button = tk.Button(jendela, text='prediksi', command=prediksi)
prediksi_button.pack()

hasil_label = tk.Label(jendela, text='')
hasil_label.pack(pady=20)

jendela.mainloop()

conn.close()
