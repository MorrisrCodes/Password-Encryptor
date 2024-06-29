from tkinter.messagebox import showinfo
import tkinter as tk
import random

codemap = {
    'a': '45', 'b': '91', 'c': '31', 'd': '06', 'e': '83', 'f': '27', 'g': '64', 
    'h': '59', 'i': '29', 'j': '77', 'k': '49', 'l': '13', 'm': '90', 'n': '42', 
    'o': '56', 'p': '02', 'q': '66', 'r': '01', 's': '72', 't': '24', 'u': '44', 
    'v': '15', 'w': '08', 'x': '73', 'y': '38', 'z': '20', 'A': '37', 'B': '78', 
    'C': '81', 'D': '18', 'E': '57', 'F': '11', 'G': '87', 'H': '55', 'I': '14', 
    'J': '03', 'K': '75', 'L': '10', 'M': '89', 'N': '85', 'O': '50', 'P': '46', 
    'Q': '74', 'R': '62', 'S': '63', 'T': '79', 'U': '25', 'V': '36', 'W': '04', 
    'X': '93', 'Y': '84', 'Z': '16', '0': '41', '1': '94', '2': '22', '3': '12', 
    '4': '17', '5': '52', '6': '67', '7': '92', '8': '60', '9': '43', '!': '53', 
    '@': '26', '#': '07', '$': '61', '%': '34', '^': '76', '&': '88', '*': '21', 
    '(': '48', ')': '58', '-': '30', '_': '32', '=': '05', '+': '65', '[': '70', 
    ']': '82', ';': '80', "'": '35', ',': '28', '.': '47', '/': '19', '{': '69', 
    '}': '33', '|': '09', ':': '40', '"': '86', '<': '23', '>': '68', '?': '71', 
    '`': '39', '~': '54', ' ': '51'
}

#reversing the keys and values in the codemap dictionary
inverted_codemap = {}
for key, val in codemap.items():
    inverted_codemap[val] = key

def encrypt(before):
    #adding exception handling
    try:
        passw = ''
        #exception handling for invalid characters
        for i in before:
            if i not in codemap:
                showinfo("Error", "Password must contain only letters, numbers, and special characters")
                return
            passw += codemap[i] #adding each digit to the password
        #exception handling for password length
        if not 8 <= len(before) <= 20:
            showinfo("Error", "Password must be between 8 and 20 characters long")
            return
        #exception handling for password having an uppercase letter, number, and special character
        if not any(char.isupper() for char in before):
            showinfo("Error", "Password must contain at least one uppercase letter")
            return
        if not any(char.isdigit() for char in before):
            showinfo("Error", "Password must contain at least one number")
            return
        if not any(char in '!@#$%^&*(),.?":{}|<>' for char in before):
            showinfo("Error", "Password must contain at least one special character")
            return
    except KeyError:
        pass
    if len(before) < 20: #if it is equal to 20, then the password is already 40 characters long
        while len(passw) < 40:
            passw += 'H' #adds H to the end of the password that's been altered
            while len(passw) < 40: #adding random characters to the password
                passw += random.choice(['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '[', ']', ';', "'", ',', '.', '/', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '|', ':', '"', '<', '>', '?', '`', '~'])
    afterE.delete(0, tk.END)
    afterE.insert(0, passw)

def decrypt(before):
    passw = ''
    i = 0
    while i < len(before):
        if 'H' in before[i:i+2]: #if H is in the password it means you have reached the end of the altered password and you can disregard the rest of the code
            break
        pair = before[i:i+2] #each password character is a double digit number so need to check each pair
        passw += inverted_codemap[pair]
        i += 2
    afterE.delete(0, tk.END)
    afterE.insert(0, passw)
               
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

rule = tk.Label(root, text="Password must be between 8 and 20 characters long, include 1 number, 1 uppercase letter, and 1 special character")  
rule.grid(row=2, column=0, columnspan=4)

sub = tk.Button(root, text="Encrypt", command=lambda: encrypt(beforeE.get()))
sub.grid(row=3, column=0)
dec = tk.Button(root, text="Decrypt", command=lambda: decrypt(beforeE.get()))
dec.grid(row=3, column=1)

root.mainloop()
#check on documentation