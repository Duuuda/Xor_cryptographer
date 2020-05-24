# Encryption v3.1.5.9

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

# Encryption/Decryption


def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    del num, from_base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def Encrypt(into):
    keys = [randint(ord(into[0]), 2147483647) for i in range(len(into) - 1)]
    cip = [ord(into[i]) ^ keys[i] for i in range(len(into) - 1)]
    out = {convert_base(keys[i], to_base=36): convert_base(cip[i], to_base=36) for i in range(len(into) - 1)}
    del keys, cip
    return out


def Decrypt(into):
    return ''.join([chr(int(convert_base(list(into.keys())[i], from_base=36)) ^ int(convert_base(list(into.values())[i], from_base=36))) for i in range(len(into))])


# Interface


def Cs(a):
    s = a.geometry()
    s = s.split('+')
    s = s[0].split('x')
    s[0] = str(int((a.winfo_screenwidth() - int(s[0]))/2))
    s[1] = str(int((a.winfo_screenheight() - int(s[0]))/2))
    a.geometry('+{0}+{1}'.format(s[0], s[1]))
    del s, a


def write(self, text):
    self.configure(state=NORMAL)
    self.delete(1.0, END)
    self.insert(1.0, text)
    self.configure(state=DISABLED)
    del text, self


def ClEnk():
    cell = Encrypt(txt11.get(1.0, END))
    write(txt12, '.'.join(list(cell.values())))
    write(txt13, ':'.join(list(cell.keys())))
    del cell


def ClDec():
    try:
        nu1 = txt22.get(1.0, END)[0:len(txt22.get(1.0, END)) - 1]
        nu2 = txt21.get(1.0, END)[0:len(txt21.get(1.0, END)) - 1]
        cell = Decrypt(dict(zip(nu1.split(':'), nu2.split('.'))))
        del nu1, nu2
        write(txt23, cell)
        del cell
    except:
        messagebox.showerror(title='ERROR_511', message='Keys/Ciphertext entered incorrectly!!!')


def ToD():
    txt21.delete(1.0, END)
    txt21.insert(1.0, txt12.get(1.0, END)[0:len(txt12.get(1.0, END))-1])
    txt22.delete(1.0, END)
    txt22.insert(1.0, txt13.get(1.0, END)[0:len(txt13.get(1.0, END))-1])
    write(txt23, '')
    tabs.select(t2)

def ToE():
    txt11.delete(1.0, END)
    txt11.insert(1.0, txt23.get(1.0, END)[0:len(txt23.get(1.0, END))-1])
    write(txt12, '')
    write(txt13, '')
    tabs.select(t1)

def ClAll1():
    txt11.delete(1.0, END)
    write(txt12, '')
    write(txt13, '')

def ClAll2():
    txt21.delete(1.0, END)
    txt22.delete(1.0, END)
    write(txt23, '')

window = Tk()
window.geometry('1001x498')
window.update_idletasks()
Cs(window)
window.iconbitmap('assets/lock.ico')
window.title("Duda's Encryption v3.1.5.9")
window['bg'] = "gray17"
window.resizable(width=FALSE, height=FALSE)

tabs = ttk.Notebook(window)
tabs.pack(fill='both', expand='yes')

t1 = Frame(window, bg='grey17')
tabs.add(t1, text='Encrypt')
t2 = Frame(window, bg='grey17')
tabs.add(t2, text='Decrypt')

f_11 = LabelFrame(t1, text="Text")
f_11['bg'] = "gray17"
f_11['fg'] = "white"
f_11.grid(row=0, column=0, columnspan=6, rowspan=7)
txt11 = Text(f_11, bg='grey25', fg='white', width=58, height=28)
txt11.pack(expand=1, fill=BOTH)

f_12 = LabelFrame(t1, text="Encrypted Text")
f_12['bg'] = "gray17"
f_12['fg'] = "white"
f_12.grid(row=0, column=9, columnspan=6, rowspan=3)
txt12 = Text(f_12, bg='grey25', fg='white', width=58, height=12)
txt12.configure(state=DISABLED)
txt12.pack(expand=1, fill=BOTH)

f_13 = LabelFrame(t1, text="Keys")
f_13['bg'] = "gray17"
f_13['fg'] = "white"
f_13.grid(row=4, column=9, columnspan=6, rowspan=3)
txt13 = Text(f_13, bg='grey25', fg='white', width=58, height=12)
txt13.configure(state=DISABLED)
txt13.pack(expand=1, fill=BOTH)

label11 = Label(t1, text="→", bg='grey17', fg='white')
label11.config(font=("Calibri", 30))
label11.grid(row=1, column=7, padx=5)

label12 = Label(t1, text="→", bg='grey17', fg='white')
label12.config(font=("Calibri", 30))
label12.grid(row=5, column=7, padx=5)

btnEn = Button(t1, text="Encode",  width=5, height=1, bg='grey15', fg='white', command=ClEnk)
btnEn.grid(row=3, column=7)

btnToD = Button(t1, text="→",  width=2, height=1, bg='grey15', fg='white', command=ToD)
btnToD.grid(row=0, column=7)

btnCl1 = Button(t1, text="Cl All",  width=4, height=1, bg='grey15', fg='white', command=ClAll1)
btnCl1.grid(row=6, column=7)

f_21 = LabelFrame(t2, text="Encrypted Text")
f_21['bg'] = "gray17"
f_21['fg'] = "white"
f_21.grid(row=0, column=0, columnspan=6, rowspan=3)
txt21 = Text(f_21, bg='grey25', fg='white', width=58, height=12)
txt21.pack(expand=1, fill=BOTH)

f_22 = LabelFrame(t2, text="Keys")
f_22['bg'] = "gray17"
f_22['fg'] = "white"
f_22.grid(row=4, column=0, columnspan=6, rowspan=3)
txt22 = Text(f_22, bg='grey25', fg='white', width=58, height=12)
txt22.pack(expand=1, fill=BOTH)

f_23 = LabelFrame(t2, text="Text")
f_23['bg'] = "gray17"
f_23['fg'] = "white"
f_23.grid(row=0, column=9, columnspan=6, rowspan=7)
txt23 = Text(f_23, bg='grey25', fg='white', width=58, height=28)
txt23.configure(state=DISABLED)
txt23.pack(expand=1, fill=BOTH)

label21 = Label(t2, text="→", bg='grey17', fg='white')
label21.config(font=("Calibri", 30))
label21.grid(row=1, column=7, padx=5)

label22 = Label(t2, text="→", bg='grey17', fg='white')
label22.config(font=("Calibri", 30))
label22.grid(row=5, column=7, padx=5)

btnDe = Button(t2, text="Decode",  width=5, height=1, bg='grey15', fg='white', command=ClDec)
btnDe.grid(row=3, column=7)

btnToE = Button(t2, text="←",  width=2, height=1, bg='grey15', fg='white', command=ToE)
btnToE.grid(row=0, column=7)

btnCl2 = Button(t2, text="Cl All",  width=4, height=1, bg='grey15', fg='white', command=ClAll2)
btnCl2.grid(row=6, column=7)

window.mainloop()
