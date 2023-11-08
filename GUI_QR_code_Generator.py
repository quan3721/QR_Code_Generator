# -- Create AN APPLICATION TO GENERATE INTO QR CODE -- #

# -- Import Libraries -- #
from tkinter import *
import pyqrcode
from PIL import ImageTk, Image


# -- Create a function to generate -- #
def generate():
    link_name = name_entry.get() # -- get the name of file
    link = link_entry.get() # -- get the url value
    file_name = link_name + ".png" # -- create a name of file image
    url = pyqrcode.create(link) # -- generate link into qr code
    url.png(file_name, scale=8) # -- convert qr code to file png
    image = ImageTk.PhotoImage(Image.open(file_name)) # Image.open(file_name) : to open image from name file; and ImageTk.PhotoImage() : to open on window based on Tkinter Library
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200, 450, window=image_label)


# -- Create a new window based on tkinter library -- #
root = Tk()

# -- Create a canvas -- #
canvas = Canvas(root, width=400, height=700)
canvas.pack()

# -- Create a label for application -- #
app_label = Label(root, text="QR Code Generator", fg='blue', font=("Arial", 25))
canvas.create_window(200, 50, window=app_label) # -- the position of label on canvas

# -- Create another labels for data input -- #
name_label = Label(root, text="Link name")
link_label = Label(root, text="Link")
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

# -- Create entry for entering input -- #
name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200, 120, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

# -- Create button to generate QR code -- #
button = Button(text="Generate QR code", command=generate)
canvas.create_window(200, 230, window=button)

# -- Create a loop to show the window -- #
root.mainloop()