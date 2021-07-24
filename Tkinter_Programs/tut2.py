from tkinter import * 
import tkinter as tk
from PIL import ImageTk, Image

root = Tk()
root.geometry("1920x1080")
root.title("Map-Lib Game")


def printInput():
    inp1 = inputtext.get(1.0, "end-1c")
    inp2 = inputtext1.get(1.0, "end-1c")
    lbl.config(text="Roses are Red\nViolets are Blue\nI proposed " + inp1 + "\nBut she said " + inp2 + " loves you", font=("comicsansms", 16), fg="red")

    
welc = Label(text="WELCOME!!", font=("comicsansms", 40, "bold"))
welc.pack()

img1_p = ImageTk.PhotoImage(Image.open("D:/Python/Tkinter_Programs/tenor.gif"))
img1 = Label(image=img1_p)
img1.pack() 

statem = Label(text="\nThis is a Mad-Lib Game.\nIn order to get the best result, please answer honestly else it ain't gonna be that fun.", font=("comicsansms", 18))
statem.pack()

ques1 = Label(root, text="\nEnter the character you like the most: ", font=(14))
ques1.pack()

inputtext = tk.Text(root, height = 2, width = 20)
inputtext.pack()


ques2 = Label(root, text = "\nEnter the person you love the most: ", font=(14))
ques2.pack()

inputtext1 = tk.Text(root, height = 2, width = 20)
inputtext1.pack()

printButton = Button(root, text="Print", command = printInput)
printButton.pack()

lbl = tk.Label(root, text="")
lbl.pack()

exit_button = Button(root, text="Exit Program", command=root.quit)
exit_button.pack()

root.mainloop()