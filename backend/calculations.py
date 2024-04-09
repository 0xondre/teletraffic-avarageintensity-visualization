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