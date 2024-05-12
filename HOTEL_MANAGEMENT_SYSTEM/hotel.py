from tkinter import *
from PIL import Image, ImageTk
from customer import CustomerWindow
from room_details import roomWindow
from details import detailsWindow
from report import reportWindow
from logOut import logOutWindow


class HotelManagmentSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1300x700+0+0")

        # ============= First Image ===============
        # 1st
        image1 = Image.open(
            r"D:\ALL PROGRAMMING\PYTHON_ALL_PROJECTS\HOTEL_MANAGEMENT_SYSTEM\allImages\hotel1.png")
        image1 = image1.resize((500, 140))
        self.photoimg1 = ImageTk.PhotoImage(image1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=550, height=140)

        # 2nd
        img2 = Image.open(
            r"D:\ALL PROGRAMMING\PYTHON_ALL_PROJECTS\HOTEL_MANAGEMENT_SYSTEM\allImages\hotel2.png")
        img2 = img2.resize((500, 140))
        self.photoimage2 = ImageTk.PhotoImage(img2)

        lblimg1 = Label(self.root, image=self.photoimage2, bd=4, relief=RIDGE)
        lblimg1.place(x=500, y=0, width=550, height=140)

        # 3rd
        img3 = Image.open(
            r"D:\ALL PROGRAMMING\PYTHON_ALL_PROJECTS\HOTEL_MANAGEMENT_SYSTEM\allImages\tajpalacehotel.jpg")
        img3 = img3.resize((500, 140))
        self.photoimage3 = ImageTk.PhotoImage(img3)

        lblim2 = Label(self.root, image=self.photoimage3, bd=4, relief=RIDGE)
        lblim2.place(x=1050, y=0, width=220, height=140)

        # =================== Logo ====================

        image2 = Image.open(
            r"D:\ALL PROGRAMMING\PYTHON_ALL_PROJECTS\HOTEL_MANAGEMENT_SYSTEM\allImages\logohotel.png")
        image2 = image2.resize((230, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(image2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        # ====================== TITLE ====================
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=(
            "times new roman", 30, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1300, height=45)

        # ======================== MAIN FRAME ====================

        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=185, width=1300, height=620)

        # ======================= Menu =======================

        lbl_menu = Label(main_frame, text="Menu", font=(
            "times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ======================== BUTTON FRAME ====================

        button_frame = Frame(main_frame, bd=4, relief=RIDGE)
        button_frame.place(x=0, y=34, width=230, height=170)

        # customer
        cust_btn = Button(button_frame, text="CUSTOMER", width=24, font=(
            "times new roman", 12, "bold"), command=self.cust_details, bg="gold", fg="black", bd=1, cursor="hand2")
        cust_btn.grid(row=0, column=0, pady=1)

        # room
        room_btn = Button(button_frame, text="ROOM", width=24, font=(
            "times new roman", 12, "bold"), command=self.room_details, bg="gold", fg="black", bd=1, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        # deatils
        details_btn = Button(button_frame, text="DETAILS", width=24, font=(
            "times new roman", 12, "bold"), command=self.det_details, bg="gold", fg="black", bd=1, cursor="hand2")
        details_btn.grid(row=2, column=0, pady=1)

        # report
        report_btn = Button(button_frame, text="REPORT", width=24, font=(
            "times new roman", 12, "bold"),command=self.rep_details,bg="gold", fg="black", bd=1, cursor="hand2")
        report_btn.grid(row=3, column=0, pady=1)

        # Logout
        logout_btn = Button(button_frame, text="LOGOUT", width=24, font=(
            "times new roman", 12, "bold"),command=self.logOut_details,bg="white", fg="red", bd=1, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)

        # ============================ RIGHT SIDE IMAGE ================================

        image3 = Image.open(
            r"D:\ALL PROGRAMMING\PYTHON_ALL_PROJECTS\HOTEL_MANAGEMENT_SYSTEM\allImages\slide3.jpg")
        image3 = image3.resize((1040, 500), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(image3)

        lblimg = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=225, y=0, width=1040, height=500)

        # ============================== DOWN IMAGE ===================================
        # first
        image4 = Image.open(
            r"D:\ALL PROGRAMMING\PYTHON_ALL_PROJECTS\HOTEL_MANAGEMENT_SYSTEM\allImages\myh.jpg")
        image4 = image4.resize((230, 210), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(image4)

        lblimg = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=205, width=225, height=158)

        # second
        image5 = Image.open(
            r"D:\ALL PROGRAMMING\PYTHON_ALL_PROJECTS\HOTEL_MANAGEMENT_SYSTEM\allImages\khana.jpg")
        image5 = image5.resize((225, 190), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(image5)

        lblimg = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=360, width=225, height=140)
    # customer window

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.detail = CustomerWindow(self.new_window)

    # room window
    def room_details(self):
        self.new_window = Toplevel(self.root)
        self.detail = roomWindow(self.new_window)

    # details window
    def det_details(self):
        self.new_window = Toplevel(self.root)
        self.detail = detailsWindow(self.new_window)
        
    # report window
    def rep_details(self):
        self.new_window = Toplevel(self.root)
        self.detail = reportWindow(self.new_window)
        
    # Logout window
    def logOut_details(self):
        self.new_window = Toplevel(self.root)
        self.detail = logOutWindow(self.new_window)


# =========== Main ===========
if __name__ == "__main__":
    root = Tk()
    obj = HotelManagmentSystem(root)
    root.mainloop()
