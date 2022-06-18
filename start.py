wnica = ["⬜︎"]*64 #pusta szachownica
import os


def wypisz(): #ładne wypisywanie
  for i in range(8):
   i =i*8
   print(wnica[0+i],wnica[1+i],wnica[2+i],wnica[3+i],wnica[4+i],wnica[5+i],wnica[6+i],wnica[7+i])

def clear():
  os.system('clear')
    
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
