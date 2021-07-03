import pytesseract as tess
import PIL
from PIL import Image
import os
import tkinter.filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
tess.pytesseract.tesseract_cmd = ("C:\\Program Files\\Tesseract-OCR\\tesseract.exe")
def imgtotxt():
    image_file=askopenfilename(filetypes=[("Image Files","*.png;*.jpg;*.jpeg")])
    img= Image.open(image_file)
    if img.format != "PNG":
        img=img.convert("RGB")
        img.save("test.png","png")
        img=Image.open("test.png")
    cwd=os.path.dirname(image_file)
    #print(cwd)
    text=tess.image_to_string(img)
    #old_name=os.path.basename(image_file)
    new_name=cwd+"/"+ os.path.splitext(os.path.basename(image_file))[0] + ".txt"
    #print(new_name)
    file=open(new_name,"w")
    file.write(text)
    file.close()
    #print("done")
#imgtotxt()