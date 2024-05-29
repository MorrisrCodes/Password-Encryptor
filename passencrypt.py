import tkinter as tk

def enctrypt(before):
    passw = ''
    if len(before) < 10:
        passw + ('z')
    elif len(before) >= 10:
        passw + ('Z')
    return passw

root = tk.Tk()

root.title("Password Encryptor")

beforeL = tk.Label(root, text="Before")
beforeL.grid(row=0, column=0)
afterL = tk.Label(root, text="Encrypted")
afterL.grid(row=0, column=1)

beforeE = tk.Entry(root, width=50)
beforeE.grid(row=1, column=0)
beforeE.insert(0, "Enter password here")
afterE = tk.Entry(root, width=50)
afterE.grid(row=1, column=1)

rule = tk.Label(root, text="Password must be at least 10 characters long, include 1 number, 1 uppercase letter, and 1 special character")  
rule.grid(row=2, column=0, columnspan=4)

sub = tk.Button(root, text="Encrypt", command=lambda: encrypt(beforeE.get()))
sub.grid(row=3, column=0, columnspan=2)

root.mainloop()