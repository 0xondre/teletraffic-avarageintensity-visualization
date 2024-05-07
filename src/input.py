class Input:
    intensywnosc = {}
    czas = []

    def __init__(self, int_name="int.txt", time_name="czas.txt") -> None:
        self.int_name = int_name
        self.time_name = time_name

    def fromFile(self) -> None:
        fInt = open(self.int_name, "r")
        lines = fInt.readlines()
        for line in lines:
            line_splitted = line.split()
            self.intensywnosc[line_splitted[0]] = float(line_splitted[1])
        fInt.close()

        fCzas = open(self.time_name, "r")
        lines = fCzas.readlines()
        for line in lines:
            line.split()
            self.czas.append(float(line[0]))
        fCzas.close()

    
    
