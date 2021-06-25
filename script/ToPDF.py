"""
ToPDF.py , 25/06/2021
author: LucasVBR
"""
from os import path

import tkinter
from tkinter.filedialog import askopenfilenames

from PIL import Image

"""
Program that convert Images into PDF
The order of Images is by name in alphanumerical
The name of the PDF is the same than the first file selected

If there is 0 files selected, the program stop
"""

root = tkinter.Tk()
root.withdraw()

while True:
    # Select files
    files = askopenfilenames(title='Images a convertir en PDF',
                             filetypes=[("Images", "*.jpg *.jpeg *.png"),
                                        ("All", "*.*")])

    if len(files) > 0: # There is files : Convert them

        imageList = []
        for image in files:
            temp = Image.open(rf"{image}")
            imageList.append(temp.convert('RGB'))


        pdf_file = f"out/{path.splitext(path.basename(files[0]))[0]}.pdf"

        imageList[0].save(rf"{pdf_file}",
                          save_all=True,
                          append_images=imageList[1:])
    else: # Stop
        break
