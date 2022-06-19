wnica = ["⬜︎"]*64 #pusta szachownica
litery = ["a","b","c","d","e","f","g","h"]
import os

def wypisz(): #ładne wypisywanie
  for i in range(8):
   i =i*8
   print(int(i/8)+1,wnica[0+i],wnica[1+i],wnica[2+i],wnica[3+i],wnica[4+i],wnica[5+i],wnica[6+i],wnica[7+i])
  for item in litery:
    print(" ",item, end="")
  print(" ")
    
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

def naLiczbe(tekst):
  a = 8*(int(tekst[1])-1)
  a += litery.index(tekst[0])
  return a
def naZnaki(liczba):
  a = litery[liczba%8]+str(liczba//8+1)
  return a
