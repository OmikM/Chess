import start as s
import moves as m
import os

board = s.wnica

def run():
  global ruchCB # Białe czy czarne True to czarne False to białe
  ruchCB = False
  s.start()
  while True:
    boardstary = board[:] #kopiowanie by móc porównać
    print("player move",["b","c"][int(ruchCB)])
    pol1 = s.naLiczbe(input("skąd: "))
    pol2 = s.naLiczbe(input("do kąd: "))
    m.ruch(pol1, pol2, ruchCB)
    os.system('cls')
    if boardstary == board: #Czy zaszła zmiana
      print("ruch niemożliwy")
    else:
      ruchCB = not ruchCB
    s.wypisz()
if __name__=='__main__':
  print(s.naZnaki(63))
  run()