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
            line_stripped = line.strip()
            self.czas.append(int(line_stripped))
        fCzas.close()
        

        for i in range(1,1441):
            if str(i) not in self.intensywnosc.keys():
                self.intensywnosc[str(i)] = 0
        
        sorted_keys = sorted(self.intensywnosc.keys(), key=lambda x: int(x))
        self.intensywnosc = {key: self.intensywnosc[key] for key in sorted_keys}


    
    
