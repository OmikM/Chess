wnica = ["⬜︎"]*64 #pusta szachownica
def wypisz(): #ładne wypisywanie
  for i in range(8):
   i =i*8
   print(wnica[0+i],wnica[1+i],wnica[2+i],wnica[3+i],wnica[4+i],wnica[5+i],wnica[6+i],wnica[7+i])
    
def start():
  for i in range(8): #stawianie pionków czarnych
    wnica[8+i] = "Pc"
  for i in range(8): #stawianie pionków białe
    wnica[48+i] = "Pb"
  InneFig = ["W","S","G","K","D","G","S","W"]#Figury inne niż pionki w kolejności ustawienia
  for i in range(64):                      
    if i<8:
      wnica[i] = InneFig[i]+"c" #Rozkładanie figur w odpowiedniej kolejności na planszy (białe)
    if i>=56:
      wnica[i] = InneFig[i%8]+"b" #Czarne
  wypisz()
    
def ruch(pol1, pol2):
  color = wnica[pol1][1]
  if wnica[pol1][0]=="S":
    ruchS(pol1,pol2,color)
  if wnica[pol1][0]=="P":
    if color=="b":
      ruchPb(pol1,pol2)
    elif color=="c":
      ruchPc(pol1,pol2)
  if wnica[pol1][0]=="W":
    ruchW(pol1,pol2)
    


def ruchW(pol1, pol2):
  if pol2 == pol1:
    print("Nie możesz wykonać tego ruchu.")
  elif wnica[pol2]!="⬜︎":
    print("Bicie.",pol1,wnica[pol2])

  elif True:
    for i in range(8):
      if wnica[pol2+8*i] == "Wb":
        print("Ruch możliwy")
        wnica[pol1],wnica[pol2] = wnica[pol2],wnica[pol1]
        
      else:
        print(wnica[pol2+8*i])
        break

  

def ruchS(pol1, pol2, color):
  pass
def ruchPb(pol1,pol2):
  
  if pol2 == pol1:
    print("Nie możesz wykonać tego ruchu.")
  elif wnica[pol2]!="⬜︎":
    print("Bicie.",pol1,wnica[pol2])
  elif pol2 + 8 == pol1:
    wnica[pol1],wnica[pol2] = wnica[pol2],wnica[pol1]
    wypisz()
  else:
    print("Nie możesz wykonać tego ruchu.")
  
  
start()
while True:
  ruch(int(input("skąd: ")),int(input("do kąd: ")))
  wypisz()