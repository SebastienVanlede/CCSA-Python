# https://dodona.ugent.be/nl/courses/399/series/8106/activities/2096226599/
class BankRekening:
    def __init__(self, rekening_houder, rekening_nummer, bedrag=0):
        self.rekening_houder = rekening_houder
        self.rekening_nummer = rekening_nummer
        self.bedrag = bedrag

    def __str__(self):
        rekening_nummer = self.rekening_nummer
        rekening_houder = self.rekening_houder
        bedrag = self.bedrag
        return str(f'{rekening_houder}, {rekening_nummer}, bedrag: {bedrag}')

    def __repr__(self):
        return str(
            f"BankRekening('{self.rekening_houder}', '{self.rekening_nummer}', {self.bedrag})")

    def afhalen(self, n):
        self.bedrag -= n

    def storten(self, n):
        self.bedrag += n
