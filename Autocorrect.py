import textblob
from textblob import TextBlob
import tkinter.filedialog
from tkinter.filedialog import askopenfilename
import docx
from docx import Document
from docx.shared import Inches
import os

def autocorrect_text():
    file=askopenfilename(filetypes=[("Text files",".txt")])
    #cwd=os.path.dirname(file)
    
    file1=open(file,"r")
    a=file1.read()
    file1.close()
    b=TextBlob(a)
    b=b.correct()
    #new_name=cwd+"/"+ os.path.splitext(os.path.basename(file))[0] + ".txt"
    
    file2=open(file,"w")
    file2.write(str(b))
    file2.close()
#autocorrect_text()