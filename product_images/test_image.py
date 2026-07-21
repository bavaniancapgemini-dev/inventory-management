from tkinter import Tk

from image_manager import upload_image

root = Tk()

root.withdraw()

path = upload_image()

print(path)