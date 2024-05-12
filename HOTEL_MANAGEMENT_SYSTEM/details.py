from tkinter import *
from PIL import Image, ImageTk


class detailsWindow():
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1040x462+230+222")

        # title
        lbl_title = Label(self.root, text="DETAILS", font=(
            "times new roman", 22, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1040, height=50)

        # logo
        image2 = Image.open(
            r"D:\ALL PROGRAMMING\PYTHON_ALL_PROJECTS\HOTEL_MANAGEMENT_SYSTEM\allImages\logohotel.png")
        image2 = image2.resize((120, 45), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(image2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=120, height=45)


if __name__ == "__main__":
    root = Tk()
    obj = detailsWindow(root)
    root.mainloop()
