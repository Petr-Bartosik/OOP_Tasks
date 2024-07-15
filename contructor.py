class Mesto:
    def __init__(self, nazev_mesta=None, nazev_regionu=None, nazev_zeme=None, pocet_obcanu=None, psc=None, predcisli=None):
        self._nazev_mesta = nazev_mesta if nazev_mesta else ""
        self._nazev_regionu = nazev_regionu if nazev_regionu else ""
        self._nazev_zeme = nazev_zeme if nazev_zeme else ""
        self._pocet_obcanu = pocet_obcanu if pocet_obcanu else 0
        self._psc = psc if psc else ""
        self._predcisli = predcisli if predcisli else ""

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

    # Overloaded string method
    def __str__(self):
        return (f"Město: {self._nazev_mesta}, Region: {self._nazev_regionu}, Země: {self._nazev_zeme}, "
                f"Počet občanů: {self._pocet_obcanu}, PSČ: {self._psc}, Předčíslí: {self._predcisli}")

    # Overloaded equality method
    def __eq__(self, other):
        if isinstance(other, Mesto):
            return (self._nazev_mesta == other._nazev_mesta and
                    self._nazev_regionu == other._nazev_regionu and
                    self._nazev_zeme == other._nazev_zeme and
                    self._pocet_obcanu == other._pocet_obcanu and
                    self._psc == other._psc and
                    self._predcisli == other._predcisli)
        return False

# Příklad použití třídy
mesto1 = Mesto("Praha", "Hlavní město Praha", "Česká republika", 1300000, "11000", "+420")
mesto2 = Mesto("Brno", "Jihomoravský kraj", "Česká republika", 380000, "60200", "+420")

# Výstup dat
mesto1.output_data()
print(str(mesto1))

# Vstup nových dat
mesto1.input_data()
mesto1.output_data()

# Porovnání měst
print(mesto1 == mesto2)
