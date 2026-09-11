from tkinter import *

def submit():
    name = n.get()
    phone = p.get()
    age = int(a.get())

    if age >= 18:
        result.config(text="Eligible we will contact u soon")
    else:
        result.config(text="Not Eligible")

root = Tk()
root.title("Enquiry Form")

Label(root, text="Candidate Name").pack()
n = Entry(root)
n.pack()

Label(root, text="Phone Number").pack()
p = Entry(root)
p.pack()

Label(root, text="Age").pack()
a = Entry(root)
a.pack()

Label(root, text="Designation").pack()
d = Entry(root)
d.pack()

Button(root, text="Submit", command=submit).pack()

result = Label(root, text="")
result.pack()

root.mainloop()