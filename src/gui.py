import tkinter as tk
import matplotlib.backends.backend_tkagg as tkagg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import numpy as np
import matplotlib.figure as figure
import gateway

# male t na male h, teoriaruchu/ na folder w ktorym znajduje sie program


# define windows and frames
window = tk.Tk()
window.title("Teoria ruchu")
window.geometry("1000x400")
window.resizable(False, False)

fig = figure.Figure(figsize=(7.2, 2.5))
fig.subplots_adjust(bottom=0.2, right=0.95)
ax = fig.add_subplot()

fig2 = figure.Figure(figsize=(7.2, 2.5))
fig2.subplots_adjust(bottom=0.2, right=0.95)
ax2 = fig2.add_subplot()


homepage = tk.Frame(window)
homepage.grid(row=0, column=0, sticky="nsew")
pageHelp = tk.Frame(window)
pageHelp.grid(row=0, column=0, sticky="nsew")
pageNewData = tk.Frame(window)
pageNewData.grid(row=0, column=0, sticky="nsew")
pageGenerate = tk.Frame(window)
pageGenerate.grid(row=0, column=0, sticky="nsew")
pageManualEntry = tk.Frame(window)
pageManualEntry.grid(row=0, column=0, sticky="nsew")
pageResults = tk.Frame(window)
pageResults.grid(row=0, column=0, sticky="nsew")

canvas = tkagg.FigureCanvasTkAgg(fig, master=pageGenerate)
canvas2 = tkagg.FigureCanvasTkAgg(fig2, master=pageResults)

data = [1] * 1440
time = [120]
result = {}
size = 1440
avg_value = 0

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
  
  avg_value = sum(result.values())/len(result.values())
  formatted_number = "{:.4f}".format(avg_value)
  label_avgValue.config(text=("Średnia wartość natężenia podczas całej doby wynosi " + formatted_number +" Erlang. Na wykresie wartość jest oznaczona czerwoną linią."))

  ax2.bar(result.keys(), result.values())
  ax2.axhline(y=avg_value, color='red', linewidth=0.5)

  ax2.set_xticks(x_ticks)
  ax2.set_xticklabels(x_labels)
  ax2.set_title("Wartość średniego nateżenia ruchu w zależności od minuty doby")
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

  avg_value = sum(result.values())/len(result.values())
  formatted_number = "{:.4f}".format(avg_value)
  label_avgValue.config(text=("Średnia wartość natężenia podczas całej doby wynosi " + formatted_number +" Erlang. Na wykresie wartość jest oznaczona czerwoną linią."))

  ax2.bar(result.keys(),result.values())
  ax2.set_xticks(x_ticks)
  ax2.set_xticklabels(x_labels)
  
  ax2.axhline(y=avg_value, color='red', linewidth=0.5)


  ax2.set_title("Wartość średniego nateżenia ruchu w zależności od minuty doby")
  ax2.set_xlabel("Czas [h]")
  ax2.set_ylabel("Średnie nateżenie ruchu [Erlang]")
  
  canvas2.draw()


# Home page layout
button_1_homepage = tk.Button(homepage, text="Wygeneruj wykres używając danych z plików", command=wygeneruj_z_pliku, width=20, height=3, font=('Calibri', 14), wraplength=200)
button_2_homepage = tk.Button(homepage, text="Wprowadź nowe dane", command=lambda: pageNewData.tkraise(), width=20, height=3, font=('Calibri', 14))
button_3_homepage = tk.Button(homepage, text="Pomoc", command=lambda: pageHelp.tkraise(), width=20, height=3, font=('Calibri', 14))
label_homepage = tk.Label(
  homepage,
  text= "Witaj w aplikacji do wizualizowania średniego nateżenia ruchu telekomunikacyjnego. Dostarcza ona wizualizacji, które pomogą Ci zrozumieć, jak wykorzystywana jest sieć w różnych porach dnia (jesli użyjesz rzeczywistych danych) oraz jak działa obliczanie średniego natężenia ruchu telekomunikacyjnego. Aby dowiedzieć się więcej naciśnij przycisk \"Pomoc\". Program autorstwa Jędrzeja Ciechanowskiego 273146.",
  wraplength=700,
  font=('Calibri', 14))

button_1_homepage.grid(row=0, column=0, padx=10, pady=14, sticky="ns")
button_2_homepage.grid(row=1, column=0, padx=10, pady=14, sticky="ns")
button_3_homepage.grid(row=2, column=0, padx=10, pady=14, sticky="ns")
label_homepage.grid(row=0,rowspan=5, column=1, padx=10, pady=10, sticky="nsew")

# page help layout
label_pageHelp = tk.Label(
  pageHelp,
  text="Aplikacja do wizualizacji i obliczania średnich wartości natężenia w ruchu telekomunikacyjnym umożliwia wprowadzenie danych używając plików int.txt oraz czas.txt. Oba pliki muszą znajdować się w folderze w którym znajduję się projekt. Czasy rozmów znajdują się w pliku czas.txt, każda linia zawiera liczbę w formie floata (część ułamkową od całkowitej dzieli kropka). Intesywnosc w każdej minucie znajduje się w pliku int.txt, każda linia składa się z dwóch liczb pierwsza to minuta doby w formie inta, a druga to intensywność w formie floata (część ułamkową od całkowitej dzieli kropka), tym co dzieli obie liczby jest dowolna liczba spacji. Innym sposobem wprowadzenia danych jest wygenerowanie ich losowo, wewnątrz programu, za pomocą rozkładu Poissona lub Gaussa. Możesz również wprowadzić dane ręcznie. Obliczanie danych odbywa się za pomocą wzoru A = λ * h, gdzie A to średnia wartość natężenia, λ to średnia ilość połączeń, a h to średni czas użycia. Przy wprowadzaniu manualnym użyty wzór to A = n / T * h, gdzie to n to ilość rozmów w badanym czasie T o średniej długości h minut. Jak można zauważyć jest to rozwinięcie poprzedniego wzoru a średnia ilość połączeń λ = n / T. Innym wzorem nie użytym w programie jest A = λ / μ, gdzie μ to intensywność zakończenia obsługi pojedynczego zgłoszenia. Aby wrócić do poprzedniej strony naciśnij przycisk \"Powrót\".",
  font=('Calibri', 14),
  wraplength=960
  )
button_pageHelp = tk.Button(pageHelp, text="Powrót", command=lambda: homepage.tkraise(), width=20, height=3, font=('Calibri', 14))

label_pageHelp.grid(row=0, rowspan=3, column=0, columnspan=3, padx=10, pady=10, sticky="ns")
button_pageHelp.grid(row=3, column=2, padx=10, pady=10)

# page new data layout

button_1_newData = tk.Button(pageNewData, text="Wygeneruj dane losowe", command=lambda: pageGenerate.tkraise(), width=21, height=3, font=('Calibri', 14))
button_2_newData = tk.Button(pageNewData, text="Manualnie wprowadź dane", command=lambda: pageManualEntry.tkraise(), width=21, height=3, font=('Calibri', 14))
button_3_newData = tk.Button(pageNewData, text="Powrót", command=lambda: homepage.tkraise(), width=21, height=3, font=('Calibri', 14))

label_newData = tk.Label(
  pageNewData,
  text= "Aby wygenerować dane losowe za pomocą rozkładu poissona lub gaussa naciśnij przycisk \"Wygeneruj dane losowe\". Jeśli chcesz wprowadzić dane ręcznie naciśnij przycisk \"Manualnie wprowadź dane\". Aby wrócić do poprzedniej strony naciśnij przycisk \"Powrót\".",
  wraplength=700,
  font=('Calibri', 14))

button_1_newData.grid(row=0, column=0, padx=10, pady=14, sticky="ns")
button_2_newData.grid(row=1, column=0, padx=10, pady=14, sticky="ns")
button_3_newData.grid(row=2, column=0, padx=10, pady=14, sticky="ns")
label_newData.grid(row=0,rowspan=3, column=1, padx=10, pady=10, sticky="nsew")

# page manual entry layout
def calculate_intensity():
  avgTime = spinbox_avgTime.get()
  amtOfCalls = spinbox_amtOfCalls.get()
  timespan = spinbox_timespan.get()

  if avgTime.isdigit() and amtOfCalls.isdigit() and timespan.isdigit() and int(timespan) != 0:
    avgTime_num = int(avgTime)
    amtOfCalls_num = int(amtOfCalls)
    timespan_num = int(timespan)
    text = "Średnia wartość natężenia wynosi: " + str(avgTime_num * amtOfCalls_num/timespan_num) + " Erlang"
    label_odpowiedz.config(text=text, wraplength=400)
  elif int(timespan) == 0:
    label_odpowiedz.config(text=("Okres czasu nie może wynosić 0"))
  else:
    label_odpowiedz.config(text=("Wprowadzone dane nie są liczbami"))


spinbox_avgTime = tk.Spinbox(pageManualEntry, from_=0, to=10000, width=10)
spinbox_timespan = tk.Spinbox(pageManualEntry, from_=0, to=10000, width=10)
spinbox_amtOfCalls = tk.Spinbox(pageManualEntry, from_=0, to=10000, width=10)

button_1_manualEntry = tk.Button(pageManualEntry, text="Oblicz", command=calculate_intensity, width=21, height=3, font=('Calibri', 14))
button_2_manualEntry = tk.Button(pageManualEntry, text="Powrót", command=lambda: pageNewData.tkraise(), width=21, height=3, font=('Calibri', 14))

label_odpowiedz = tk.Label(pageManualEntry, text="", font=('Calibri', 14))
label_amtOfCalls = tk.Label(pageManualEntry, text="Liczba połączeń", font=('Calibri', 14))
label_timespan = tk.Label(pageManualEntry, text="Badany okres czasu w minutach", font=('Calibri', 14))
label_avgTime = tk.Label(pageManualEntry, text="Średni czas użycia w minutach", font=('Calibri', 14))
label_opis = tk.Label(pageManualEntry, text="Wprowadź dane w formie liczb calkowitych, aby obliczyć średnią wartość natężenia ruchu. Używany wzór to średnia wartość natężenia = liczba połączeń / okres czasu * średni czas użycia (A = n / T * h).", font=('Calibri', 14), wraplength=600)

button_1_manualEntry.grid(row=2, column=0, padx=10, pady=14, sticky="ns")
button_2_manualEntry.grid(row=3, column=0, padx=10, pady=14, sticky="ns")

spinbox_avgTime.grid(row=0, column=0, padx=5, pady=14, sticky="ns")
spinbox_amtOfCalls.grid(row=0, column=1, padx=5, pady=14, sticky="ns")
spinbox_timespan.grid(row=0, column=2, padx=5, pady=14, sticky="ns")

label_odpowiedz.grid(row=0, column=3, padx=5, pady=14, sticky="ns")
label_avgTime.grid(row=1, column=0, padx=5, pady=14, sticky="ns")
label_amtOfCalls.grid(row=1, column=1, padx=5, pady=14, sticky="ns")
label_timespan.grid(row=1, column=2, padx=5, pady=14, sticky="ns")
label_opis.grid(row=2, column=1,rowspan=2,columnspan=3, padx=10, pady=14, sticky="ns")

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
def saveResults():
  f = open("results.txt", "w")
  for key in result.keys():
    f.write(str(key) + " " + str(result[key]) + "\n")
  f.close()

def return_to_homepage():
  homepage.tkraise()
  ax2.clear()

# page results layout

canvas2_widget = canvas2.get_tk_widget().grid(row=0, column=1,rowspan=2,columnspan=2, sticky="nsew", padx=10, pady=10)
toolbar2 = NavigationToolbar2Tk(canvas2, pageResults, pack_toolbar=False)
toolbar2.update()
toolbar2.grid(row=2, column=1, padx=10, pady=10)

#button_1_pageResults = tk.Button(pageResults, text="Zmień okres", command=lambda: change_time, width=23, height=3, font=('Calibri', 14))
button_2_pageResults = tk.Button(pageResults, text="Zapisz wynik jako result.txt", command=saveResults, width=23, height=3, font=('Calibri', 14))
button_3_pageResults = tk.Button(pageResults, text="Powrót do pierwszej strony", command=return_to_homepage, width=23, height=3, font=('Calibri', 14))
label_avgValue = tk.Label(pageResults, text=("Średnia wartość natężenia z użytych danych wynosi " + str(avg_value) +" Erlang. Na wykresie wartość jest oznaczona czerwoną linią."), font=('Calibri', 14),wraplength=400)

#button_1_pageResults.grid(row=0, column=0, padx=10, pady=14)
button_2_pageResults.grid(row=0, column=0, padx=10, pady=14)
button_3_pageResults.grid(row=2, column=0, padx=10, pady=14)

label_avgValue.grid(row=2, column=2,columnspan=2, padx=10, pady=14)

homepage.tkraise()
window.mainloop()