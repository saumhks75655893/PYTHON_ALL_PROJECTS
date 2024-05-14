from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


class CustomerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1040x462+230+222")

        # ====================== TITLE ====================
        lbl_title = Label(self.root, text="CUSTOMERS DETAILS", font=(
            "times new roman", 22, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1040, height=50)

        # =================== Logo ====================

        image2 = Image.open(
            r"D:\ALL PROGRAMMING\PYTHON_ALL_PROJECTS\HOTEL_MANAGEMENT_SYSTEM\allImages\logohotel.png")
        image2 = image2.resize((120, 45), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(image2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=120, height=45)

        # ===================== LABEL FRAME ==================

        labelframeLeft = LabelFrame(self.root, bd=2, text="Customer Details", font=(
            "Times New Roman", 12, "bold"), relief=RIDGE, padx=2)
        labelframeLeft.place(x=5, y=50, width=360, heigh=410)

        # ======================= labels and entries ===================

        # customer reference
        lbl_cust_ref = Label(labelframeLeft, text="Customer ref : ", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeLeft, font=(
            "arial", 11, "bold"), width=26)
        entry_ref.grid(row=0, column=1)

        # customer name
        lbl_cust_name = Label(labelframeLeft, text="Customer name : ", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_cust_name.grid(row=1, column=0, sticky=W)

        txt_cname = ttk.Entry(labelframeLeft, font=(
            "arial", 11, "bold"), width=26)
        txt_cname.grid(row=1, column=1)

        # Customer mother name

        lbl_cust_m_name = Label(labelframeLeft, text="Mother name : ", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_cust_m_name.grid(row=2, column=0, sticky=W)

        entry_m_name = ttk.Entry(labelframeLeft, font=(
            "arial", 11, "bold"), width=26)
        entry_m_name.grid(row=2, column=1)

        # Customer gender combobox

        lbl_cust_gender = Label(labelframeLeft, text="Gender : ", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_cust_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(
            labelframeLeft, font=("arial", 10, "bold"), width=27, state="readonly")
        combo_gender["values"] = ("Male", "Female", "Others")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # post code
        lbl_cust_post = Label(labelframeLeft, text="PostCode : ", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_cust_post.grid(row=4, column=0, sticky=W)

        entry_post = ttk.Entry(labelframeLeft, font=(
            "arial", 11, "bold"), width=26)
        entry_post.grid(row=4, column=1)

        # mobile number
        lbl_cust_mob = Label(labelframeLeft, text="Mobile No. : ", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_cust_mob.grid(row=5, column=0, sticky=W)

        entry_mob = ttk.Entry(labelframeLeft, font=(
            "arial", 11, "bold"), width=26)
        entry_mob.grid(row=5, column=1)

        # email id
        lbl_cust_email = Label(labelframeLeft, text="Email id : ", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_cust_email.grid(row=6, column=0, sticky=W)

        entry_email = ttk.Entry(labelframeLeft, font=(
            "arial", 11, "bold"), width=26)
        entry_email.grid(row=6, column=1)

        # nationality
        lbl_cust_nationality = Label(labelframeLeft, text="Nationality : ", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_cust_nationality.grid(row=7, column=0, sticky=W)

        combo_nationality = ttk.Combobox(
            labelframeLeft, font=("arial", 10, "bold"), width=27, state="readyonly")
        combo_nationality["values"] = ("Indian", "African", "American", "Britist", "Chinese", "Korean", "Japanese", "Combodian",
                                       "Russian", "Pakistani", "Afaganistani", "Nepali", "ShriLankan", "Bhutani", "Thailandian", "Purtagali")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        # Id proof type (combobox)
        lbl_cust_idProof = Label(labelframeLeft, text="Id Proof : ", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_cust_idProof.grid(row=8, column=0, sticky=W)

        combo_Id = ttk.Combobox(
            labelframeLeft, font=("arial", 10, "bold"), width=27, state="readyonly")
        combo_Id["values"] = (
            "Adhar card", "Driving licence", "Passport", "VoterId card")
        combo_Id.current(0)
        combo_Id.grid(row=8, column=1)

        # Id number
        lbl_cust_IdNumber = Label(labelframeLeft, text="ID Number : ", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_cust_IdNumber.grid(row=9, column=0, sticky=W)

        entry_IdNumber = ttk.Entry(labelframeLeft, font=(
            "arial", 11, "bold"), width=26)
        entry_IdNumber.grid(row=9, column=1)

        # address
        lbl_cust_address = Label(labelframeLeft, text="Address : ", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_cust_address.grid(row=10, column=0, sticky=W)

        entry_address = ttk.Entry(labelframeLeft, font=(
            "arial", 11, "bold"), width=26)
        entry_address.grid(row=10, column=1)

        # ====================== BUTTONS =========================
        btn_frame = Frame(labelframeLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=350, width=350, height=40)

        # add button
        btn_add = Button(btn_frame, text="Add", font=(
            "arial", 10, "bold"), bg="black", fg="gold", width=10)
        btn_add.grid(row=0, column=0, padx=2)

        # update button
        btn_update = Button(btn_frame, text="Update", font=(
            "arial", 10, "bold"), bg="black", fg="gold", width=9)
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete", font=(
            "arial", 10, "bold"), bg="black", fg="gold", width=9)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset", font=(
            "arial", 10, "bold"), bg="black", fg="gold", width=10)
        btn_reset.grid(row=0, column=3, padx=2)

        # =============================== Table Frame =================================

        Table_frame = LabelFrame(self.root, bd=2, text="View Details And Search System", font=(
            "Times New Roman", 12, "bold"), relief=RIDGE, padx=2)
        Table_frame.place(x=366, y=50, width=670, heigh=408)

        # search by
        lblSearchBy = Label(Table_frame, text="Search by : ", font=(
            "arial", 10, "bold"), bg="red", fg="gold", padx=2)
        lblSearchBy.grid(row=0, column=0, sticky=W)

        # combo box to search
        combo_Id = ttk.Combobox(
            Table_frame, font=("arial", 10, "bold"), width=24, state="readyonly")
        combo_Id["values"] = (
            "Mobile NO.", "Reference NO.")
        combo_Id.current(0)
        combo_Id.grid(row=0, column=1, padx=3)

        # Search value
        txtSearch = ttk.Entry(Table_frame, font=(
            "arial", 11, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=3)

        btnSearch = Button(Table_frame, text="Search", font=(
            "arial", 10, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(Table_frame, text="Show All", font=(
            "arial", 10, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=2)

        # ============================ show data tabes ===========================

        details_table = Frame(Table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=665, height=300)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Customer_details_table = ttk.Treeview(details_table, columns=("ref", "name", "mother", "gender", "post", "mobile",
                                                   "email", "nationality", "IdProof", "IdNumber", "Address"), xscrollcommand=scroll_x, yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Customer_details_table.xview)
        scroll_y.config(command=self.Customer_details_table.yview)

        self.Customer_details_table.heading("ref", text="Refer No", width=100)
        self.Customer_details_table.heading("name", text="Name")
        self.Customer_details_table.heading("mother", text="Mother Name")
        self.Customer_details_table.heading("gender", text="Gender")
        self.Customer_details_table.heading("post", text="PostId")
        self.Customer_details_table.heading("mobile", text="Mobile No")
        self.Customer_details_table.heading("email", text="Email ID")
        self.Customer_details_table.heading("nationality", text="Nationality")
        self.Customer_details_table.heading("IdProof", text="ID Proof")
        self.Customer_details_table.heading("IdNumber", text="ID Number")
        self.Customer_details_table.heading("Address", text="Address")

        self.Customer_details_table["show"] = "headings"

        self.Customer_details_table.column("ref",width=100)
        self.Customer_details_table.column("name",widht=100)
        self.Customer_details_table.column("mother",widht=100)
        self.Customer_details_table.column("gender",widht=100)
        self.Customer_details_table.column("post",widht=100 )
        self.Customer_details_table.column("mobile",widht=100)
        self.Customer_details_table.column("email",widht=100)
        self.Customer_details_table.column("nationality",widht=100)
        self.Customer_details_table.column("IdProof",widht=100)
        self.Customer_details_table.column("IdNumber",widht=100)
        self.Customer_details_table.column("Address",widht=100 )
        
        
        self.Customer_details_table.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = Tk()
    obj = CustomerWindow(root)
    root.mainloop()
