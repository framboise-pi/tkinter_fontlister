#!/usr/bin/env python3
######################
#
#  ▄▄·       ·▄▄▄▄  ▄▄▄ .▄▄▌  ▪  ▄▄▄▄· ▄▄▄  ▄▄▄ .   ·▄▄▄▄▄▄  
# ▐█ ▌▪▪     ██▪ ██ ▀▄.▀·██•  ██ ▐█ ▀█▪▀▄ █·▀▄.▀·   ▐▄▄·▀▄ █·
# ██ ▄▄ ▄█▀▄ ▐█· ▐█▌▐▀▀▪▄██▪  ▐█·▐█▀▀█▄▐▀▀▄ ▐▀▀▪▄   ██▪ ▐▀▀▄ 
# ▐███▌▐█▌.▐▌██. ██ ▐█▄▄▌▐█▌▐▌▐█▌██▄▪▐█▐█•█▌▐█▄▄▌   ██▌.▐█•█▌
# ·▀▀▀  ▀█▄▀▪▀▀▀▀▀•  ▀▀▀ .▀▀▀ ▀▀▀·▀▀▀▀ .▀  ▀ ▀▀▀  ▀ ▀▀▀ .▀  ▀
#
# ASCII art generator: http://patorjk.com/software/taag/
#
#fork from
#https://www.tutorialspoint.com/how-to-list-available-font-families-in-tkinter

from tkinter import *
from tkinter import font

root = Tk()
root.geometry("680x480")
root.title('Tkinter availables Fonts List')

fonts=list(font.families())
fonts.sort()

def Content(frame):
   font_count = 0
   font_previous = ""
   for f in fonts:
      if (str(f) != str(font_previous)):
         font_count = font_count + 1
         phrase="...[FONT-N°" + str(font_count) +"] adding new font to list"
         print(phrase)
         font_previous = str(f)
         label = Label(frame,text=f,font=(f, 14)).pack()
      else:
         print("--- [REMOVED] duplicata")
      
def Update(canvas):
   canvas.configure(scrollregion=canvas.bbox("all"))
   
canvas = Canvas(root,bd=1, background="white")
frame = Frame(canvas, background="white")

scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scroll_y.set)
scroll_y.pack(side="right", fill="y")
canvas.pack(side="left", expand=1, fill="both")
canvas.create_window((5,4), window=frame, anchor="n")
frame.bind("<Configure>", lambda e, canvas=canvas: Update(canvas))
Content(frame)
root.mainloop()
