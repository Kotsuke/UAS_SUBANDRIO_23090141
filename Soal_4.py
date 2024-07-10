class Buah:
    def __init__(Self, Nama, Warna, Rasa):
        Self.Nama = Nama
        Self.Warna = Warna
        Self.Rasa = Rasa
    def get_Nama(Self):
        return Self.Nama
    def get_Warna(Self):
        return Self.Warna
    def get_Rasa(Self):
        return Self.Rasa
    def info(self):
        return f'Nama : {self.Nama}, Warna : {self.Warna}, Rasa : {self.Rasa}'
class Mangga(Buah):
    def __init__(Self, Nama, Warna, Rasa, Vitamin):
        super().__init__(Nama, Warna, Rasa)
        Self.Vitamin = Vitamin
    def info_buah(self):
        return f'{super().info()}, Vitamin : {self.Vitamin}' 
object = Mangga('Mangga','Kuning', 'Manis', 'V')
print(object.info_buah())