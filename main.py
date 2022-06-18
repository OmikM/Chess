import start as s
import moves
    
board = s.wnica
def run():
  print("I work")
  s.start()
  while True:
    moves.ruch(int(input("skąd: ")),int(input("dokąd: ")))
  s.wypisz()
if __name__ == "__main__":
    run()
