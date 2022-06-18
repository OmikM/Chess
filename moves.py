import main as r
import start as s
def ruch(pol1, pol2):
  color = r.board[pol1][1]
  if pol2 == pol1:
    print("Nie możesz wykonać tego ruchu.")
  elif pol2>63:
    return "nie"
  elif r.board[pol1][0]=="S":
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
  if r.board[pol2]!="⬜︎": #czy buicie
    print("Bicie.",pol1,r.board[pol2])
  i= 0
  while pol2+8*i>=0 and pol2+8*i<=63:
    if r.board[pol2+8*i] == "Wb":
      r.board[pol1],r.board[pol2] = r.board[pol2],r.board[pol1]
      return None
    if pol2<pol1:
      i+=1
    else:
      i-=1
  i = 0
  while (pol2+1*i)%8!=0:
    if r.board[pol2+1*i] == "Wb":    
      r.board[pol1],r.board[pol2]=r.board[pol2],r.board[pol1]
      break
    if pol2<pol1:
      i+=1
    else:
      i-=1

def ruchPc(pol1,pol2):
  if r.board[pol2]!="⬜︎":
    print("Bicie.",pol1,r.board[pol2])
  elif pol2 - 8 == pol1:
    r.board[pol1],r.board[pol2] = r.board[pol2],r.board[pol1]
  else:
    print("Nie możesz wykonać tego ruchu.")

def ruchPb(pol1,pol2):  
  if r.board[pol2]!="⬜︎":
    if pol2 +8 == pol1: 
      print("Bicie.",pol1,r.board[pol2])
    else:
      print("Nie możesz wykonać tego ruchu")
  elif pol2 + 8 == pol1:
    r.board[pol1],r.board[pol2] = r.board[pol2],r.board[pol1]
    
  else:
    print("Nie możesz wykonać tego ruchu.")