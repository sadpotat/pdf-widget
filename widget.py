from tkinter import *
from tkinter import ttk
from math import ceil
from PIL import ImageTk, Image
from pdf2image import convert_from_path

# geometry dimensions
x, y = [450, 750]
root = Tk()     # creates root object
# the numbers +1050+10 are for positioning the window
root.geometry(f"{x}x{y}+1050+10")
root.resizable(False, False)
# root.overrideredirect(1)

# creating a canvas widget
canvas = Canvas(root, width=x-20)

# another frame in the canvas
frame = Frame(canvas)
frame.grid(row=0, column=0)

# quit button to save my RAM
ttk.Button(root, text="Quit", command=root.destroy).pack(side=BOTTOM, fill=X)

# convert stored pdf to image
# images is a list where every element is a PIL image object of a page in the pdf
images = convert_from_path('test_multiple_page.pdf', fmt="jpeg",
                           poppler_path=r"put path to poppler-(version)\Library\bin here")

# resize image to fit root
width, height = images[0].size
w, h = x, ceil(height*x/width)

i = 0
for image in images:
    images[i] = image.resize((w, h), Image.LANCZOS)
    i += 1

# re-initializing root geometry to fit image for single page pdfs
if len(images) == 1:
    root.geometry(f"{w}x{h}")

# display image as a Label widget
for i in range(len(images)):
    images[i] = ImageTk.PhotoImage(images[i])
    ttk.Label(frame, image=images[i], width=w).grid(column=0, row=i)

# placing canvas
canvas.pack(side=LEFT, fill=Y, expand=True)

# adding a scrollbar for multiple pages
if len(images) != 1:
    canvas.create_window(0, 0, anchor='nw', window=frame)
    # make sure everything is displayed before configuring the scrollregion
    canvas.update_idletasks()

    # creating a vertical scrollbar
    vbar = Scrollbar(root, orient="vertical", command=canvas.yview)

    # setting scrollregion
    canvas.configure(scrollregion=canvas.bbox("all"), yscrollcommand=vbar.set)

    # placing scrollbar
    vbar.pack(side=LEFT, fill=Y, expand=True)

root.mainloop()
