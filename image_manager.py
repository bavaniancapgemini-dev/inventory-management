import os
import shutil

from tkinter import filedialog

def upload_image():

    file = filedialog.askopenfilename(

        title="Choose Product Image",

        filetypes=[

            ("Images","*.png *.jpg *.jpeg")

        ]

    )

    if not file:

        return ""

    folder = "product_images"

    os.makedirs(

        folder,

        exist_ok=True

    )

    filename = os.path.basename(file)

    destination = os.path.join(

        folder,

        filename

    )

    shutil.copy(

        file,

        destination

    )

    return destination