import tkinter as tk
# Definiowanie stron i okien
window = tk.Tk()
window.title("Teoria ruchu")
window.geometry("650x400")
window.resizable(False, False)

homepage = tk.Frame(window)
homepage.grid(row=0, column=0, sticky="nsew")
pageHelp = tk.Frame(window)
pageHelp.grid(row=0, column=0, sticky="nsew")
pageGenerate = tk.Frame(window)
pageGenerate.grid(row=0, column=0, sticky="nsew")
pageResults = tk.Frame(window)
pageResults.grid(row=0, column=0, sticky="nsew")

# Home page layout
button_1_homepage = tk.Button(homepage, text="Wygeneruj dane", command=lambda: pageGenerate.tkraise(), width=20, height=3, font=('Calibri', 14))
button_2_homepage = tk.Button(homepage, text="Wprowadz dane z pliku", command=lambda: pageResults.tkraise(), width=20, height=3, font=('Calibri', 14))
button_3_homepage = tk.Button(homepage, text="Pomoc", command=lambda: pageHelp.tkraise(), width=20, height=3, font=('Calibri', 14))
label_homepage = tk.Label(
  homepage,
  text= "Witaj w  industry. Lorem Ipsum has been the industry' of type g, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. ",
  wraplength=400,
  font=('Calibri', 14))

button_1_homepage.grid(row=0, column=0, padx=10, pady=10)
button_2_homepage.grid(row=1, column=0, padx=10, pady=10)
button_3_homepage.grid(row=2, column=0, padx=10, pady=10)
label_homepage.grid(row=0,rowspan=3, column=1, padx=10, pady=10, sticky="ns")

# page help layout
label_pageHelp = tk.Label(
  pageHelp,
  text="been the industry' of type g, remaining essentially unchanged. It was popularised been the industry' of type g, remaining essentially unchanged. Ibeen the industry' of type g, remaining essentially unchanged. I,  g, remaining essentially unchanged.  g, remaining essentially unchanged.  g, remaining essentially unchanged.  g, remaining essentially unchanged.  g, remaining essentially unchanged.  g, remaining essentially unchanged.  g, remaining essentially unchanged.  g, remaining essentially unchanged.  g, remaining essentially unchanged.  g, remaining essentially unchanged. ",
  font=('Calibri', 14),
  wraplength=400)
button_pageHelp = tk.Button(pageHelp, text="Back", command=lambda: homepage.tkraise(), width=20, height=3, font=('Calibri', 14))

label_pageHelp.grid(row=0, rowspan=3, column=1, padx=10, pady=10, sticky="ns")
button_pageHelp.grid(row=1, column=0, padx=10, pady=10)

# page generate layout zmien komendy w buttonach 
button_1_pageGenerate = tk.Button(pageGenerate, text="Rozkład Poissona", command=lambda: pageGenerate.tkraise(), width=20, height=3, font=('Calibri', 14))
button_2_pageGenerate = tk.Button(pageGenerate, text="Rozkład Gaussa", command=lambda: pageResults.tkraise(), width=20, height=3, font=('Calibri', 14))
button_3_pageGenerate = tk.Button(pageGenerate, text="Losowo", command=lambda: pageHelp.tkraise(), width=20, height=3, font=('Calibri', 14))

button_1_pageGenerate.grid(row=0, column=0, padx=10, pady=10)
button_2_pageGenerate.grid(row=1, column=0, padx=10, pady=10)
button_3_pageGenerate.grid(row=2, column=0, padx=10, pady=10)

homepage.tkraise()
window.mainloop()