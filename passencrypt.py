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

inverted_codemap = {}
for key, val in codemap.items():
    inverted_codemap[val] = key

def encrypt(before):
    passw = ''
    for i in range(len(before)):
        if before[i] == 'a':
            passw += '21'
        elif before[i] == 'b':
            passw += '22'
        elif before[i] == 'c':
            passw += '23'
        elif before[i] == 'd':
            passw += '31'
        elif before[i] == 'e':
            passw += '32'
        elif before[i] == 'f':
            passw += '33'
        elif before[i] == 'g':
            passw += '41'
        elif before[i] == 'h':
            passw += '42'
        elif before[i] == 'i':
            passw += '43'
        elif before[i] == 'j':
            passw += '51'
        elif before[i] == 'k':
            passw += '52'
        elif before[i] == 'l':
            passw += '53'
        elif before[i] == 'm':
            passw += '61'
        elif before[i] == 'n':
            passw += '62'
        elif before[i] == 'o':
            passw += '63'
        elif before[i] == 'p':
            passw += '71'
        elif before[i] == 'q':
            passw += '72'
        elif before[i] == 'r':
            passw += '73'
        elif before[i] == 's':
            passw += '74'
        elif before[i] == 't':
            passw += '81'
        elif before[i] == 'u':
            passw += '82'
        elif before[i] == 'v':
            passw += '83'
        elif before[i] == 'w':
            passw += '91'
        elif before[i] == 'x':
            passw += '92'
        elif before[i] == 'y':
            passw += '93'
        elif before[i] == 'z':
            passw += '94'
        elif before[i] == ' ':
            passw += '95'
    if len(before) < 20:
        while len(passw) < 40:
            passw += 'H'
            while len(passw) < 40:
                passw += random.choice(['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '[', ']', ';', "'", ',', '.', '/', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '|', ':', '"', '<', '>', '?', '`', '~'])
    afterE.delete(0, tk.END)
    afterE.insert(0, passw)

def decrypt(before):
    passw = ''
    i = 0
    while i < len(before):
        if 'H' in before[i:i+2]:  # Stops processing at the 'H' character
            break
        pair = before[i:i+2]  # Take two characters at a time
        if pair in inverted_codemap:
            passw += inverted_codemap[pair]  # Add the corresponding character
        else:
            passw += ''  # Handle cases where the pair is not found
        i += 2
               
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