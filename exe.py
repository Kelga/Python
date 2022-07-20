from tkinter import *
from tkinter.ttk import Checkbutton
from os import system
import sys
window = Tk()
window.title("ExePackager")
window.geometry('320x240')

var = IntVar()
varWC = IntVar()
result = "pyinstaller --onedir --console  """
cw = None
fd = None
n = None
system(r'pip install pyinstaller')

def convertation():
    if var.get() == 0:
        fd = "--onedir"
    else:
        fd = "-F"
    if varWC.get() == 0:
        cw = "--noconsole"
    else:
        cw = "--windowed"
    if progname != None:
        n = progname.get()
    else:
        n = ''
    result = f'pyinstaller -n {n} {fd} {cw} {pathStr.get()}'
    system(result)
    return
    
pathLabel = Label(window, text="Путь к файлу.")
pathLabel.grid(column=0, row=0)
pathStr = Entry(window)
pathStr.grid(column=1, row=0)
prognamel = Label(window, text="Имя программы.")
prognamel.grid(column=0, row=1)
progname = Entry(window)
progname.grid(column=1, row=1)

onedir = Radiobutton(window, text="Папка с файлами", variable=var, value=0)
onedir.grid(column=0, row=2)
onefile = Radiobutton(window, text="Один файл", variable=var, value=1)
onefile.grid(column=1, row=2)

console = Radiobutton(window, text="Консольная программа", variable=varWC, value=0)
console.grid(column=0, row=3)
windowed = Radiobutton(window, text="Программа с GUI", variable=varWC, value=1)
windowed.grid(column=1, row=3)

confirm = Button(window, text="Конвертировать", command=convertation)
confirm.grid(column=1, row=4)

window.mainloop()