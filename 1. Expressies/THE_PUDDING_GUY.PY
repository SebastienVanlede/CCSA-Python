# https://dodona.ugent.be/nl/courses/399/series/3960/activities/761303597
gekochteStuks = int(input())
kostprijsPerStuk = float(input())
aantalBarcodes = int(input())
aantalMijlen = int(input())

totaleKostprijs = gekochteStuks * kostprijsPerStuk
frequentMijlen = int((gekochteStuks / aantalBarcodes)) * aantalMijlen

print("Phillips spendeerde ${:.2f}".format(totaleKostprijs), "voor", frequentMijlen, "frequent flyer mijlen.")
