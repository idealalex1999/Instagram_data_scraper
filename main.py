import tkinter as tk
from tkinter import ttk
from tkinter import LEFT, RIGHT, TOP, BOTTOM

from Tracer_Frame import *

if __name__ == '__main__':
    path_icon = os.path.join('C:\\', 'Users', 'nerva', 'PycharmProjects', 'IG_Competitors_Tracer', 'prototipo_modified.ico')
    root = tk.Tk()
    root.title('IG Competitors Tracer')
    root.iconbitmap(path_icon)
    root.resizable(False, False)
    TracerFrame(root).pack(side='top', fill='both', expand=True)
    root.mainloop()
