import tkinter as tk
from tkinter import PhotoImage
import math
import os


nameOfThisSoftware = 'ORIZIN　AIアシスタント Python式計算機'
thisDir = os.path.abspath(os.path.dirname(__file__))


def shutdown(event):
    quit()


def worker():
    resultBox.delete('1.0', 'end')
    resultBox.insert('end', eval(requestBox.get()))


def worker_from_shortcut(event):
    worker()


root = tk.Tk()
root.title(nameOfThisSoftware)
root.geometry("800x450")
icon = [PhotoImage(file=thisDir + '/ORIZIN_Agent_Oのみ_透明.png')]
root.wm_iconphoto(True, *icon)

root.bind('<Control-q>', shutdown)
root.bind('<Return>', worker_from_shortcut)

mainFrame = tk.Frame(root, height=300)
mainFrame.pack(anchor=tk.NW, expand=1, fill=tk.BOTH)

controllerFrame = tk.Frame(mainFrame, height=100)
controllerFrame.pack(anchor=tk.NW, pady=5, expand=1, fill=tk.X)

requestBox = tk.Entry(controllerFrame)
requestBox.pack(anchor=tk.NW, side=tk.LEFT, expand=1, fill=tk.BOTH)

startButton = tk.Button(controllerFrame, text='実行', command=worker)
startButton.pack(side=tk.LEFT, anchor=tk.NW)

resultFrame = tk.Frame(mainFrame)
resultFrame.pack(anchor=tk.NW, expand=1, fill=tk.BOTH)

resultBox = tk.Text(resultFrame)
resultBox.pack(side=tk.LEFT, anchor=tk.NW, expand=1, fill=tk.BOTH)

resultBox.insert('end', open(thisDir + '/ORIZIN_Agent_AA.txt', encoding='utf-8_sig').read())


root.mainloop()
