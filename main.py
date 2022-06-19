import start as s
import moves as m
import os

board = s.wnica

def run():
  s.start()
  while True:
    boardstary = board[:] #kopiowanie by móc porównać
    pol1 = s.naLiczbe(input("skąd: "))
    pol2 = s.naLiczbe(input("do kąd: "))
    m.ruch(pol1, pol2)
    os.system('clear')
    if boardstary == board: #Czy zaszła zmiana
      print("ruch niemożliwy")
    s.wypisz()
if __name__=='__main__':
  print(s.naZnaki(63))
  run()