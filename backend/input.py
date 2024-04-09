class Input:
    intensywnosc = {}
    czas = []
    def __init__(self):
        pass
    def fromFile(self) -> None:
        fInt = open("int.txt", "r")
        lines = fInt.readlines()
        for line in lines:
            line_splitted = line.split()
            self.intensywnosc[line_splitted[0]] = float(line_splitted[1])
        fInt.close()

        fCzas = open("czas.txt", "r")
        lines = fCzas.readlines()
        for line in lines:
            line.split()
            self.czas.append(float(line[0]))
        fCzas.close()

    def generate(self) -> None:
        pass

    def manual(self) -> None:
        pass
    
    
