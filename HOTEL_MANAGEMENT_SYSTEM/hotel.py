from tkinter import *
from PIL import Image, ImageTk


class HotelManagmentSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1540x800+0+0")

        # ============= First Image ===============
        image1 = Image.open(
            r"D:\ALL PROGRAMMING\PYTHON_ALL_PROJECTS\HOTEL_MANAGEMENT_SYSTEM\allImages\hotel1.png")
        image1 = image1.resize((1540, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(image1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1540, height=150)

        # =================== Logo ====================

        image2 = Image.open(
            r"D:\ALL PROGRAMMING\PYTHON_ALL_PROJECTS\HOTEL_MANAGEMENT_SYSTEM\allImages\logohotel.png")
        image2 = image2.resize((230, 150), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(image2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=150)

        # ====================== TITLE ====================
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        
        lbl_title.place(x=0,y=140,width=1540,height=50)

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagmentSystem(root)
    root.mainloop()
