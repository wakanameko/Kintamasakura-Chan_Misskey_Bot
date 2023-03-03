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

### Load UserData.txt ###
if(os.path.isfile('UserData.txt')):
    UserInfo = open("UserData.txt", "r")
    UserData = UserInfo.read()
    print(UserData)
    #Get Instance
    startI = 'Instance:'
    endI = '\nToken:'
    sI = str(UserData)
    InsData = sI[sI.find(startI)+len(startI):sI.rfind(endI)]
    print(InsData)
    #Get Token
    startT = 'Token:'
    endT = '\n'
    sT = str(UserData)
    TokenData = sT[sT.find(startT)+len(startT):sT.rfind(endT)]
    print(TokenData)
else:
    print('ログイン情報が保存されていません!')
    res = messagebox.showinfo("注意", "ログイン情報が保存されていません!")
### Load UserData.txt ###

# events
def exitTAMA():
    exit()

def DelInfo():
    if(os.path.isfile('UserData.txt')):
        os.remove('UserData.txt')

def DelAPIKey():
    if(os.path.isfile('API_Keyんたまさくらちゃん.txt')):
        os.remove('API_Keyんたまさくらちゃん.txt')

def SaveInfo():
    txt_ins_get = (txt_ins.get())
    txt_Token_get = (txt_Token.get())
    SIF = open('UserData.txt', 'w', encoding='UTF-8')
    SIF.write(f"Instance:{txt_ins_get}\nToken:{txt_Token_get}\n")
    SIF.close()

def NNow():
    txt_ins_get = (txt_ins.get())
    txt_Token_get = (txt_Token.get())
    api = Misskey(txt_ins_get)
    api.token = txt_Token_get
    if verK == True:
        api.notes_create(text="たまさくらちゃんの金玉、きんたまさくらちゃん")
    else:
        api.notes_create(text="たまさくらちゃんの金玉　きんたまさくらちゃん")


#Widgeds
Label_wlcm = tk.Label(MainWindow, text = f"{AppName}", font = ("normal", 18, "bold"))
Label_icon = tk.Label(MainWindow, image = img)
Label_Login = tk.Label(MainWindow, text = "ログイン:", font = ("normal", 14, "bold"))
Label_ins = tk.Label(MainWindow, text = "インスタンス(Misskey.io等)")
Label_token = tk.Label(MainWindow, text = "アクセストークン")
#Label_emp = tk.Label(MainWindow, text = " ")
txt_ins = tk.Entry(width=20)
if(os.path.isfile('UserData.txt')):
    txt_ins.insert(tk.END, InsData)
txt_Token = tk.Entry(width=20)
if(os.path.isfile('UserData.txt')):
    txt_Token.insert(tk.END, TokenData)
button_SaveInfo = tk.Button(MainWindow, text = "情報を保存", command = SaveInfo, width = 9)
Label_Note = tk.Label(MainWindow, text = "ノート:", font = ("normal", 14, "bold"))
varK = tk.BooleanVar()
chk_K = tkinter.Checkbutton(text='句読点を付ける', variable = varK)
button_NNow = tk.Button(MainWindow, text = "ノート", command = NNow, width = 9)

#MenuBar
menu_file = tk.Menu(MainWindow)
Menubaa.add_cascade(label = f"{AppName}{Version}", menu = menu_file)
menu_file.add_command(label = 'ログイン情報を保存', command = SaveInfo)
menu_file.add_command(label = 'ログイン情報を削除', command = DelInfo)
menu_file.add_separator()
menu_file.add_command(label = 'アクセストークンを削除', command = DelAPIKey)
menu_file.add_separator()
menu_file.add_command(label = '閉じる', command = exitTAMA)

menu_Note = tk.Menu(MainWindow)
Menubaa.add_cascade(label = "ノート", menu = menu_Note)
menu_Note.add_command(label = 'ノート', command = NNow)

#Layouts
Label_wlcm.pack()
Label_icon.pack(anchor = tk.W, padx = 15)
Label_Login.pack(anchor = tk.W, padx = 15, pady = 0)
Label_ins.pack(anchor = tk.W, padx = 15, pady = 0)
txt_ins.pack(anchor = tk.E, padx = 15, pady = 0)
Label_token.pack(anchor = tk.W, padx = 15, pady = 0)
txt_Token.pack(anchor = tk.E, padx = 15, pady = 0)
button_SaveInfo.pack(anchor = tk.W, padx = 15, pady = 0)
#Label_emp.pack(anchor = tk.W, padx = 15, pady = 0)
Label_Note.pack(anchor = tk.W, padx = 15, pady = 0)
chk_K.pack(anchor = tk.W, padx = 15, pady = 0)
button_NNow.pack(anchor = tk.W, padx = 15, pady = 0)

MainWindow.mainloop()