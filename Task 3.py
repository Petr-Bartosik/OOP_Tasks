class Zeme:
    def __init__(self, nazev_zeme, kontinent, populace, volaci_kod, hlavni_mesto, nazvy_mest):
        self._nazev_zeme = nazev_zeme
        self._kontinent = kontinent
        self._populace = populace
        self._volaci_kod = volaci_kod
        self._hlavni_mesto = hlavni_mesto
        self._nazvy_mest = nazvy_mest

    # Getters
    def get_nazev_zeme(self):
        return self._nazev_zeme

    def get_kontinent(self):
        return self._kontinent

    def get_populace(self):
        return self._populace

    def get_volaci_kod(self):
        return self._volaci_kod

    def get_hlavni_mesto(self):
        return self._hlavni_mesto

    def get_nazvy_mest(self):
        return self._nazvy_mest

    # Setters
    def set_nazev_zeme(self, nazev_zeme):
        self._nazev_zeme = nazev_zeme

    def set_kontinent(self, kontinent):
        self._kontinent = kontinent

    def set_populace(self, populace):
        self._populace = populace

    def set_volaci_kod(self, volaci_kod):
        self._volaci_kod = volaci_kod

    def set_hlavni_mesto(self, hlavni_mesto):
        self._hlavni_mesto = hlavni_mesto

    def set_nazvy_mest(self, nazvy_mest):
        self._nazvy_mest = nazvy_mest

    # Method to input data
    def input_data(self):
        self._nazev_zeme = input("Zadejte název země: ")
        self._kontinent = input("Zadejte kontinent: ")
        self._populace = int(input("Zadejte populaci: "))
        self._volaci_kod = input("Zadejte volací kód: ")
        self._hlavni_mesto = input("Zadejte hlavní město: ")
        self._nazvy_mest = input("Zadejte názvy měst (oddělené čárkou): ").split(", ")

    # Method to output data
    def output_data(self):
        print(f"Název země: {self._nazev_zeme}")
        print(f"Kontinent: {self._kontinent}")
        print(f"Populace: {self._populace}")
        print(f"Volací kód: {self._volaci_kod}")
        print(f"Hlavní město: {self._hlavni_mesto}")
        print(f"Názvy měst: {', '.join(self._nazvy_mest)}")

# Příklad použití třídy
zeme = Zeme("Česká republika", "Evropa", 10700000, "+420", "Praha", ["Brno", "Ostrava", "Plzeň"])
zeme.output_data()

# Vstup nových dat
zeme.input_data()
zeme.output_data()
