import tkinter as tk
import random

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
        else:
            passw += before[i]
    if len(before) < 20:
        while len(passw) < 40:
            passw += 'H'
            while len(passw) < 40:
                passw += random.choice(['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '[', ']', ';', "'", ',', '.', '/', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '|', ':', '"', '<', '>', '?', '`', '~'])
    afterE.delete(0, tk.END)
    afterE.insert(0, passw)

def decrypt(before, after):
    passw = ''
    if before == 'Enter password here' or before == '':
        i = 0
        while i < (len(after)):
            pair = after[i:i+2]
            if pair == '21':
                passw += 'a'
            elif pair == '22':
                passw += 'b'
            elif pair == '23':
                passw += 'c'
            elif pair == '31':
                passw += 'd'
            elif pair == '32':
                passw += 'e'
            elif pair == '33':
                passw += 'f'
            elif pair == '41':
                passw += 'g'
            elif pair == '42':
                passw += 'h'
            elif pair == '43':
                passw += 'i'
            elif pair == '51':
                passw += 'j'
            elif pair == '52':
                passw += 'k'
            elif pair == '53':
                passw += 'l'
            elif pair == '61':
                passw += 'm'
            elif pair == '62':
                passw += 'n'
            elif pair == '63':
                passw += 'o'
            elif pair == '71':
                passw += 'p'
            elif pair == '72':
                passw += 'q'
            elif pair == '73':
                passw += 'r'
            elif pair == '74':
                passw += 's'
            elif pair == '81':
                passw += 't'
            elif pair == '82':
                passw += 'u'
            elif pair == '83':
                passw += 'v'
            elif pair == '91':
                passw += 'w'
            elif pair == '92':
                passw += 'x'
            elif pair == '93':
                passw += 'y'
            elif pair == '94':
                passw += 'z'
            else:
                passw += pair
            i += 2
    else:
        i = 0
        while i < (len(before)):
            pair = before[i:i+2]
            if pair == '21':
                passw += 'a'
            elif pair == '22':
                passw += 'b'
            elif pair == '23':
                passw += 'c'
            elif pair == '31':
                passw += 'd'
            elif pair == '32':
                passw += 'e'
            elif pair == '33':
                passw += 'f'
            elif pair == '41':
                passw += 'g'
            elif pair == '42':
                passw += 'h'
            elif pair == '43':
                passw += 'i'
            elif pair == '51':
                passw += 'j'
            elif pair == '52':
                passw += 'k'
            elif pair == '53':
                passw += 'l'
            elif pair == '61':
                passw += 'm'
            elif pair == '62':
                passw += 'n'
            elif pair == '63':
                passw += 'o'
            elif pair == '71':
                passw += 'p'
            elif pair == '72':
                passw += 'q'
            elif pair == '73':
                passw += 'r'
            elif pair == '74':
                passw += 's'
            elif pair == '81':
                passw += 't'
            elif pair == '82':
                passw += 'u'
            elif pair == '83':
                passw += 'v'
            elif pair == '91':
                passw += 'w'
            elif pair == '92':
                passw += 'x'
            elif pair == '93':
                passw += 'y'
            elif pair == '94':
                passw += 'z'
            else:
                passw += pair
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
dec = tk.Button(root, text="Decrypt", command=lambda: decrypt(beforeE.get(), afterE.get()))
dec.grid(row=3, column=1)

root.mainloop()