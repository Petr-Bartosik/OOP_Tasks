class Mesto:
    def __init__(self, nazev_mesta, nazev_regionu, nazev_zeme, pocet_obcanu, psc, predcisli):
        self._nazev_mesta = nazev_mesta
        self._nazev_regionu = nazev_regionu
        self._nazev_zeme = nazev_zeme
        self._pocet_obcanu = pocet_obcanu
        self._psc = psc
        self._predcisli = predcisli

    # Getters
    def get_nazev_mesta(self):
        return self._nazev_mesta

    def get_nazev_regionu(self):
        return self._nazev_regionu

    def get_nazev_zeme(self):
        return self._nazev_zeme

    def get_pocet_obcanu(self):
        return self._pocet_obcanu

    def get_psc(self):
        return self._psc

    def get_predcisli(self):
        return self._predcisli

    # Setters
    def set_nazev_mesta(self, nazev_mesta):
        self._nazev_mesta = nazev_mesta

    def set_nazev_regionu(self, nazev_regionu):
        self._nazev_regionu = nazev_regionu

    def set_nazev_zeme(self, nazev_zeme):
        self._nazev_zeme = nazev_zeme

    def set_pocet_obcanu(self, pocet_obcanu):
        self._pocet_obcanu = pocet_obcanu

    def set_psc(self, psc):
        self._psc = psc

    def set_predcisli(self, predcisli):
        self._predcisli = predcisli

    # Method to input data
    def input_data(self):
        self._nazev_mesta = input("Zadejte název města: ")
        self._nazev_regionu = input("Zadejte název regionu: ")
        self._nazev_zeme = input("Zadejte název země: ")
        self._pocet_obcanu = int(input("Zadejte počet občanů: "))
        self._psc = input("Zadejte PSČ: ")
        self._predcisli = input("Zadejte předčíslí: ")

    # Method to output data
    def output_data(self):
        print(f"Název města: {self._nazev_mesta}")
        print(f"Název regionu: {self._nazev_regionu}")
        print(f"Název země: {self._nazev_zeme}")
        print(f"Počet občanů: {self._pocet_obcanu}")
        print(f"PSČ: {self._psc}")
        print(f"Předčíslí: {self._predcisli}")

# Příklad použití třídy
mesto = Mesto("Praha", "Hlavní město Praha", "Česká republika", 1300000, "11000", "+420")
mesto.output_data()

# Vstup nových dat
mesto.input_data()
mesto.output_data()
