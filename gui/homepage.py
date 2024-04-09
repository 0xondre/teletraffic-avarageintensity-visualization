import tkinter as tk

def button_1_clicked():
  print("button 1")

def button_2_clicked():
  print("button 2")

def button_3_clicked():
  print("button 3")

window = tk.Tk()
window.title("Teoria Ruchu - Zmienic nazwe")
window.geometry("600x400") 

button_1 = tk.Button(window, text="Button 1", command=button_1_clicked, width=20, height=3, font=('Calibri', 14))
button_2 = tk.Button(window, text="Button 2", command=button_2_clicked, width=20, height=3, font=('Calibri', 14))
button_3 = tk.Button(window, text="Button 3", command=button_3_clicked, width=20, height=3, font=('Calibri', 14))

button_1.grid(row=0, column=0, padx=10, pady=10)
button_2.grid(row=1, column=0, padx=10, pady=10)
button_3.grid(row=2, column=0, padx=10, pady=10)

window.mainloop()