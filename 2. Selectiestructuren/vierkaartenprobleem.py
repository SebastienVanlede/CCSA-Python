# https://dodona.ugent.be/nl/courses/399/series/3961/activities/1345385696
kaartZijde = str(input())
if kaartZijde == "waarde": 
  kaartWaarde = int(input())
else: 
  kaartWaarde = str(input())

draai = str(input())
controle = True

if kaartZijde == 'waarde' and kaartWaarde%2 != 0 and draai == 'ja':
  controle = False
if kaartZijde == 'waarde' and kaartWaarde%2 == 0 and draai == 'nee':
  controle = False
if kaartZijde == 'kleur' and kaartWaarde == 'rood' and draai == 'ja':
  controle = False
if kaartZijde == 'kleur' and kaartWaarde != 'rood' and draai == 'nee':
  controle = False

if draai == 'nee':
  if controle: 
    print(f'Juist: kaarten met {kaartZijde} {kaartWaarde} moeten niet gedraaid worden.')
  else: 
    print(f'Fout: kaarten met {kaartZijde} {kaartWaarde} moeten gedraaid worden.')
else:
  if controle: 
    print(f'Juist: kaarten met {kaartZijde} {kaartWaarde} moeten gedraaid worden.')
  else: 
    print(f'Fout: kaarten met {kaartZijde} {kaartWaarde} moeten niet gedraaid worden.')
