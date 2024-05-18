
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

        intensywnosc_ratioed = calculateIntesityToTimeRatio(intensywnosc)
        avg_time = calculateAverageTime(czas)

        result = calculateAvgIntensityAllTimeFrames(avg_time, intensywnosc_ratioed)

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


def calculateAvgIntensityOneTimeFrame(average_time: float, intensity:float) -> float:
    if average_time == 0 or intensity == 0:
        return 0
    else:
        return average_time * intensity

def calculateAverageTime(service_time: list) -> float:
    if len(service_time) == 0:
        return 0
    else:
        return sum(service_time) / len(service_time)

def calculateAvgIntensityAllTimeFrames(average_time: float, intensities: dict) -> dict:
    avg_intensities = {}
    for key in intensities.keys():
        avg_intensities[key] = calculateAvgIntensityOneTimeFrame(average_time, intensities[key])
    return avg_intensities

def calculateIntesityToTimeRatio(intensities: dict) -> dict:
    sum_intensities = sum(intensities.values())
    ratios = {}
    for key in intensities.keys():
        ratios[key] = intensities[key] / sum_intensities
    return ratios