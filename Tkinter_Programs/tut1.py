from tkinter import *
from PIL import Image, ImageTk

lisa_root = Tk() #make a basic GUI

#Width x Height
lisa_root.geometry("644x484")

#Width, Height
lisa_root.minsize(400, 200)

#Width, Height
lisa_root.maxsize(1920,1080)


# photo = PhotoImage(file="name.png") 

#For Png and GIF format images
my_img = ImageTk.PhotoImage(Image.open("D:/Python/Tkinter_Programs/tenor.gif"))
my_label = Label(image=my_img)
my_label.pack()


#For JPG Images
img1 = Image.open("D:/Python/Tkinter_Programs/Hey.jpg")
img1 = img1.resize((450, 350), Image.ANTIALIAS)
ph = ImageTk.PhotoImage(img1)
img = Label(image=ph)
img.image = ph
img.place(x=0, y=0)


#Label
stat = Label(text="This is a Mad_Lib Game. \nIt's better you Read the question properly and answer honestly to get the most satisfying answer.\n\n")
stat.pack()
ques1 = Label(text = "Enter a name of a character: ")
ques1.pack()

quit_Button = Button(lisa_root, text="Exit", command=lisa_root.quit)
quit_Button.pack()

#GUI logic above here
lisa_root.mainloop()


#text-adds the text
#bd-background
#fg-foreground
#font-sets the font
    #1.font=("comicsansms", 40, "bold")
    #2.font="comicsansms 40 bold"
#padx-x padding
#pady-y padding
#relief-border styling - SUNKEN, RAISED, GROOVE, RIDGE

