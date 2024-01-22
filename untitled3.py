from tkinter import*
import random
root=Tk()
root.geometry("800x500")
root.title("Random Background Colour")

colorArray=["red","black","blue","green","orange","white","aqua","cyan","purple","yellow",]
colorDictionary={'color':colorArray}

def bg():
    randomNo=random.randint(0,9)
    randomColor= colorDictionary['color'][randomNo]
    root.configure(background=randomColor)

button=Button(root,text="Random Background",command=bg)
button.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()