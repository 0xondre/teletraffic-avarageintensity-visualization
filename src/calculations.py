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
