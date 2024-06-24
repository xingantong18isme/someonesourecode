import tkinter as tk
form tkinter import messagebox
w=tk.Tk()
w.title("encrypt")
w.geometry("300x300")
def encrypt():
  y=e1.get()
  m=""
  for x in y:
    m+=chr(ord(x)^31)
  messagebox.showinfo("encrypt",f"Encrypted text is '{m}'.")
e1=tk.Text(w,height=4)
e1.pack()
b1=tk.Button(w,text="Encrypt Now")
b1.pack()
w.mainloop()
