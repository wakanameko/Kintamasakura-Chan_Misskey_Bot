#coding utf-8
########################################
# きんたまさくらちゃんノートBot 　         #
# 開発：@wakanameko2                　　#
# 元ネタ：@kintamasakura              　#
########################################
import os
import platform
import tkinter as tk
import PIL
import webbrowser
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from misskey import Misskey

AppName = 'きんたまさくらちゃんノートBot'
Version = '1.0'
Develop = '@wakanameko2'
Original = 'たまさくらちゃんの金玉 きんたまさくらちゃん(@kintamasakura)'

ur = platform.uname()
print(ur.system)
print(ur.release)
print(ur.version)
print(ur.processor)
print(AppName)
print(Develop)
print(Original)

#MainWindow
MainWindow = tk.Tk()
MainWindow.geometry('300x450')
MainWindow.resizable(width = False, height = False)
MainWindow.title(f"{AppName} | {Version}")
Menubaa = tk.Menu(MainWindow) 
MainWindow.config(menu=Menubaa)
MainWindow.iconphoto(False, tk.PhotoImage(file="きんたまさくらちゃん.png"))

class Application(tk.Frame):
    def drawLabelPngImg(self):
        global pngImg
        pngImg = tk.PhotoImage(file="きんたまさくらちゃん.png")
        label = tk.Label(dlg_modeless, width=100,height=100,image=pngImg)
        label.pack()

img = ImageTk.PhotoImage(Image.open("きんたまさくらちゃんsmall.png"))
