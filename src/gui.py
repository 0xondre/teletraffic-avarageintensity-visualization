import tkinter as tk
import matplotlib.backends.backend_tkagg as tkagg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import numpy as np
import matplotlib.figure as figure
import gateway

# TODO: zmiana okresu na koncu pokazac czy moze byc w ten sposob, dopisanie teorii,  wprowadzanie manualne

# define windows and frames
window = tk.Tk()
window.title("Teoria ruchu")
window.geometry("1000x400")
window.resizable(False, False)

fig = figure.Figure(figsize=(7.3, 2.5))
fig.subplots_adjust(bottom=0.2)
ax = fig.add_subplot()

fig2 = figure.Figure(figsize=(7.3, 2.5))
fig2.subplots_adjust(bottom=0.2)
ax2 = fig2.add_subplot()


homepage = tk.Frame(window)
homepage.grid(row=0, column=0, sticky="nsew")
pageHelp = tk.Frame(window)
pageHelp.grid(row=0, column=0, sticky="nsew")
pageGenerate = tk.Frame(window)
pageGenerate.grid(row=0, column=0, sticky="nsew")
pageResults = tk.Frame(window)
pageResults.grid(row=0, column=0, sticky="nsew")

canvas = tkagg.FigureCanvasTkAgg(fig, master=pageGenerate)
canvas2 = tkagg.FigureCanvasTkAgg(fig2, master=pageResults)

data = [1] * 1440
time = [30]
result = {}
size = 1440

# functions to page generate

def generate_poisson():
  ax.clear()
  poisson_data = np.random.poisson(lam=0.7, size=size)
  uniform_data = np.random.uniform(low=0.01, high=0.99, size=size)
  global data
  data = poisson_data + uniform_data
  ax.hist(data, bins=30)
  ax.set_title("Wygenerowane dane poissonowskie")
  ax.set_xlabel("Wartości intensywności")
  ax.set_ylabel("Ilość wystąpień")
  canvas.draw()

def generate_gauss():
  ax.clear()
  global data
  data = np.random.normal(loc=0.7, scale=0.3, size=size)
  for i in range(size):
    if data[i] < 0:
      data[i] = 0.0
  ax.hist(data, bins=30)
  ax.set_title("Wygenerowane dane gaussowskie")
  ax.set_xlabel("Wartości intensywności")
  ax.set_ylabel("Ilość wystąpień")

  canvas.draw()

def dalej_pageGenerate():
  ax.clear()
  
  gateway1 = gateway.Gateway()
  gateway1.saveDataToFile(intensities=data, time=time)
  global result
  result = gateway1.get_result()
  pageResults.tkraise()
  x_ticks = list(result.keys())[::60]
  x_ticks.append('1440')
  x_labels = range(0, 25)
  

  ax2.bar(result.keys(), result.values())
  ax2.set_xticks(x_ticks)
  ax2.set_xticklabels(x_labels)
  ax2.set_title("Wartość średniego nateżenia ruchu w zależności od czasu")
  ax2.set_xlabel("Czas [h]")
  ax2.set_ylabel("Średnie nateżenie ruchu [Erlang]")
  canvas2.draw()


def wygeneruj_z_pliku():
  ax.clear()
  gateway1 = gateway.Gateway()

  global result
  result = gateway1.get_result()
  pageResults.tkraise()


  x_ticks = list(result.keys())[::60]
  x_ticks.append('1440')
  x_labels = range(0, 25)
  
  ax2.bar(result.keys(),result.values())
  ax2.set_xticks(x_ticks)
  ax2.set_xticklabels(x_labels)

  ax2.set_title("Wartość średniego nateżenia ruchu w zależności od czasu")
  ax2.set_xlabel("Czas [h]")
  ax2.set_ylabel("Średnie nateżenie ruchu [Erlang]")
  
  canvas2.draw()


# Home page layout
button_1_homepage = tk.Button(homepage, text="Wygeneruj wykres używając danych z plików", command=wygeneruj_z_pliku, width=20, height=3, font=('Calibri', 14), wraplength=200)
button_2_homepage = tk.Button(homepage, text="Wprowadź nowe dane", command=lambda: pageGenerate.tkraise(), width=20, height=3, font=('Calibri', 14))
button_3_homepage = tk.Button(homepage, text="Pomoc", command=lambda: pageHelp.tkraise(), width=20, height=3, font=('Calibri', 14))
label_homepage = tk.Label(
  homepage,
  text= "Witaj w aplikacji do wizualizowania średniego nateżenia ruchu telekomunikacyjnego. Dostarcza ona wizualizacji, które pomogą Ci zrozumieć, jak działa obliczanie średniego natężenia ruchu telekomunikacyjnego oraz jak wykorzystywana jest sieć w różnych porach dnia (jesli użyjesz rzeczywistych danych). Aby dowiedzieć się więcej naciśnij przycisk Pomoc.",
  wraplength=700,
  font=('Calibri', 14))

button_1_homepage.grid(row=0, column=0, padx=10, pady=14, sticky="ns")
button_2_homepage.grid(row=1, column=0, padx=10, pady=14, sticky="ns")
button_3_homepage.grid(row=2, column=0, padx=10, pady=14, sticky="ns")
label_homepage.grid(row=0,rowspan=5, column=1, padx=10, pady=10, sticky="nsew")

# page help layout
label_pageHelp = tk.Label(
  pageHelp,
  text="been the industry' of type g, remain has been ith the release of Letrasng versions of Lorem IpLremy' of type g, remainoing essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem IpLrem Ipsum has been the industry' of type g, remainoing essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem IpLrem Ipsum has been the industry' of type g, remainoing essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem IpLrem Ipsum has been the industry' of type g, remainoing essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ip",
  font=('Calibri', 14),
  wraplength=900
  )
button_pageHelp = tk.Button(pageHelp, text="Back", command=lambda: homepage.tkraise(), width=20, height=3, font=('Calibri', 14))

label_pageHelp.grid(row=0, rowspan=3, column=0, columnspan=3, padx=10, pady=10, sticky="ns")
button_pageHelp.grid(row=3, column=2, padx=10, pady=10)

# page generate layout 
canvas_widget = canvas.get_tk_widget().grid(row=0, column=1,rowspan=2, columnspan=2,  sticky="nsew", padx=10, pady=10)
toolbar = NavigationToolbar2Tk(canvas, pageGenerate, pack_toolbar=False)
toolbar.update()
toolbar.grid(row=2, column=1,columnspan=2, sticky="nsew", padx=10, pady=10)

button_1_pageGenerate = tk.Button(pageGenerate, text="Rozkład Poissona", command=generate_poisson, width=20, height=3, font=('Calibri', 14))
button_2_pageGenerate = tk.Button(pageGenerate, text="Rozkład Gaussa", command=generate_gauss, width=20, height=3, font=('Calibri', 14))
button_3_pageGenerate = tk.Button(pageGenerate, text="Dalej", command=dalej_pageGenerate, width=20, height=3, font=('Calibri', 14))

button_1_pageGenerate.grid(row=0, column=0, padx=10, pady=14)
button_2_pageGenerate.grid(row=1, column=0, padx=10, pady=14)
button_3_pageGenerate.grid(row=2, column=0, padx=10, pady=14)

# functions to page result
def change_time():
  pass
def saveResults():
  f = open("results.txt", "w")
  for key in result.keys():
    f.write(str(key) + " " + str(result[key]) + "\n")
  f.close()

# page results layout
def return_to_homepage():
  homepage.tkraise()
  ax2.clear()


canvas2_widget = canvas2.get_tk_widget().grid(row=0, column=1,rowspan=2,columnspan=2, sticky="nsew", padx=10, pady=10)
toolbar2 = NavigationToolbar2Tk(canvas2, pageResults, pack_toolbar=False)
toolbar2.update()
toolbar2.grid(row=2, column=1,columnspan=2, sticky="nsew", padx=10, pady=10)

button_1_pageResults = tk.Button(pageResults, text="Zmień okres", command=lambda: change_time, width=21, height=3, font=('Calibri', 14))
button_2_pageResults = tk.Button(pageResults, text="Zapisz resultaty jako txt", command=saveResults, width=21, height=3, font=('Calibri', 14))
button_3_pageResults = tk.Button(pageResults, text="Powrót do pierwszej strony", command=return_to_homepage, width=21, height=3, font=('Calibri', 14))

button_1_pageResults.grid(row=0, column=0, padx=10, pady=14)
button_2_pageResults.grid(row=1, column=0, padx=10, pady=14)
button_3_pageResults.grid(row=2, column=0, padx=10, pady=14)

homepage.tkraise()
window.mainloop()