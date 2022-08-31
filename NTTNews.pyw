from os import system, remove
from os.path import isfile
from time import sleep
from datetime import datetime
from json import load
from sys import exit
from urllib.request import urlretrieve
import PySimpleGUI as sg

# ----------< JSON LOADER >----------

datet = datetime.today().strftime("%d.%m.%Y") + '.json'

urlretrieve('https://raw.githubusercontent.com/xemulat/NTTNews/main/news/' + datet, datet)
sleep(0.5)
with open(datet) as f:
    d = load(f)
    datez = str(d["NewsDate"])
    line1 = str(d["l1"])
    line2 = str(d["l2"])
    line3 = str(d["l3"])
    line4 = str(d["l4"])
    line5 = str(d["l5"])
    line6 = str(d["l6"])
    line7 = str(d["l7"])
    line8 = str(d["l8"])
    line9 = str(d["l9"])
    line10 = str(d["l10"])
    writtenby = str(d["WrittenBy"])
sleep(1.5)

# ----------< MAIN FUNCTIONS >----------

system('cls')
sg.theme("DarkGray15")
sg.set_options(font=("Consolas", 9), text_color='#FFFFFF')

# ----------< NEWS GUI >----------

def news():
    news = [[sg.Text("Date: " + datez)],
            [sg.Text("")],
            [sg.Text(line1)],
            [sg.Text(line2)],
            [sg.Text(line3)],
            [sg.Text(line4)],
            [sg.Text("")],
            [sg.Text(line5)],
            [sg.Text(line6)],
            [sg.Text(line7)],
            [sg.Text("")],
            [sg.Text(line8)],
            [sg.Text(line9)],
            [sg.Text(line10)],
            [sg.Text("")],
            [sg.Text("Story Written By: " + writtenby)],
            [sg.Button("Back"), sg.Button("Exit")],
            [sg.Text("")],
            [sg.Text("NTTNews v1.0")],
            [sg.Text("CopyLeft Xemulated 2022")]]

    layoutz = [[sg.Column(news)]]

    window = sg.Window("NTTNews", layoutz)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            remove(datet)
            exit()
        elif event == "Back":
            window.close()

news()
