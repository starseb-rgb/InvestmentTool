from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Add Image')
root.iconbitmap('C:\Image Python')
my_img = ImageTk.PhotoImage(Image.open(data.jpg))
my_label = Label(image=,my_img)
my_label.pack()



window= Tk()
window.title('Add Image')
window= Canvas(window, width=450, height=450)
window.pack()
image= PhotoImage(file = 'C:\Image Python\data.jpg')
window.create_image(0,0,anchor = NW, image = image)
window.mainloop()
