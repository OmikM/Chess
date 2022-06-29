import start as s
import moves as m
import os
import szachy as sz
# TODO funkcja czy ruch możliwy
board = s.wnica

def run():
  s.start()
  ruchCB = False # Białe czy czarne True to czarne False to
  while True:
    boardstary = board[:] #kopiowanie by móc porównać
    print("player move",["b","c"][int(ruchCB)])
    pol1 = s.naLiczbe(input("skąd: "))
    pol2 = s.naLiczbe(input("do kąd: "))
    m.ruch(pol1, pol2, ruchCB)
    os.system('cls')
    print(sz.IsSzach(ruchCB))
    #sz.IsMat(ruchCB)
    if boardstary == board: #Czy zaszła zmiana
      print("ruch niemożliwy")
    else:
      ruchCB = not ruchCB
    s.wypisz()
if __name__=='__main__':
  print(s.naZnaki(63))
  run()