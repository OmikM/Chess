import start as s
import moves as m
import os

board = s.wnica

def run():
  s.start()
  while True:
    boardstary = board[:] #kopiowanie by móc porównać 
    m.ruch(int(input("skąd: ")),int(input("dokąd: ")))
    s.clear()
    if boardstary == board: #Czy zaszła zmiana
      print("ruch niemożliwy")
    s.wypisz()
if __name__=='__main__':
  run()
