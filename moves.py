import main as r
import start as s


def ruch(pol1, pol2):
  color = r.board[pol1][1]
  if r.board[pol1][0]=="S":
    ruchS(pol1,pol2,color)
  elif r.board[pol1][0]=="P":
    if color=="b":
      ruchPb(pol1,pol2)
    elif color=="c":
      ruchPc(pol1,pol2)
  elif r.board[pol1][0]=="W":
    ruchW(pol1,pol2)
  else:
    print("Nie można wykonać ruchu")
    
def ruchW(pol1, pol2):
  if pol2 == pol1:
    print("Nie możesz wykonać tego ruchu.")
  elif r.board[pol2]!="⬜︎":
    print("Bicie.",pol1,r.board[pol2])
  elif True:
    for i in range(8):
      print(i)
      if r.board[pol2+8*i] == "Wb":
        print("Ruch możliwy")
        r.board[pol1],r.board[pol2] = r.board[pol2],r.board[pol1]
        s.wypisz()
        break
      else:
        print(r.board[pol2+8*i])
        
def ruchS(pol1, pol2, color):
  pass

def ruchPc(pol1,pol2):
  if pol2 == pol1:
    print("Nie możesz wykonać tego ruchu.")
  elif r.board[pol2]!="⬜︎":
    print("Bicie.",pol1,r.board[pol2])
  elif pol2 - 8 == pol1:
    r.board[pol1],r.board[pol2] = r.board[pol2],r.board[pol1]
    s.wypisz()
  else:
    print("Nie możesz wykonać tego ruchu.")

def ruchPb(pol1,pol2):  
  if pol2 == pol1:
    print("Nie możesz wykonać tego ruchu.")
  elif r.board[pol2]!="⬜︎":
    if pol2 +8 == pol1: 
      print("Bicie.",pol1,r.board[pol2])
    else:
      print("Nie możesz wykonać tego ruchu")
  elif pol2 + 8 == pol1:
    r.board[pol1],r.board[pol2] = r.board[pol2],r.board[pol1]
    s.wypisz()
  else:
    print("Nie możesz wykonać tego ruchu.")