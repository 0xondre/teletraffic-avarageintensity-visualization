import calculations as calc
import input 

input1 = input.Input()
input1.fromFile()
average_time = calc.calculateAverageTime(input1.czas)
print("sredni czas:",average_time)
for key in input1.intensywnosc.keys():
    intensity = calc.calculateAvgIntensityOneTimeFrame(average_time, input1.intensywnosc[key])
    print(key,intensity)
