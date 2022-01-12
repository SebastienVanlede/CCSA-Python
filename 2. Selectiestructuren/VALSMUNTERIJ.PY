# https://dodona.ugent.be/nl/courses/399/series/3961/activities/408865752
stand1 = str(input())
stand2 = str(input())
posMunt = 0

if stand1 == "rechts":
  if stand2 == "rechts": 
    posMunt = 1
  elif stand2 == "links": 
    posMunt = 2
  else: 
    posMunt = 3
if stand1 == "links":
  if stand2 == "rechts": 
    posMunt = 4
  elif stand2 == "links": 
    posMunt = 5
  else: 
    posMunt = 6
if stand1 == "evenwicht":
  if stand2 == "rechts": 
    posMunt = 7
  elif stand2 == "links": 
    posMunt = 8
  else: 
    posMunt = 9
print("muntstuk #" + str(posMunt) + " is vervalst")
