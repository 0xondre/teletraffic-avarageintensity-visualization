import calculations as calc
import input

class Gateway:
    

    def __init__(self, intensity_name="int.txt", time_name="czas.txt") -> None:
        self.intensity_name = intensity_name
        self.time_name = time_name

    def get_result(self):
        input1 = input.Input(self.intensity_name, self.time_name)

        input1.fromFile()
        intensywnosc = input1.intensywnosc
        czas = input1.czas

        intensywnosc_ratioed = calc.calculateIntesityToTimeRatio(intensywnosc)
        avg_time = calc.calculateAverageTime(czas)

        result = calc.calculateAvgIntensityAllTimeFrames(avg_time, intensywnosc_ratioed)

        return result
    def saveDataToFile(self, intensities=[1,1,1,1,1,1,1,1,1], time=[1]) -> None:
        f = open(self.intensity_name, "w")
        for i in range(len(intensities)):
            f.write(str(i+1) + " " + str(intensities[i]) + "\n")
        f.close()

        f = open(self.time_name, "w")
        for i in range(len(time)):
            f.write(str(time[i-1]) + "\n")
        f.close()