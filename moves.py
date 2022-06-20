import main as r
import start as s
import pawnMove as pm

def ruch(pol1, pol2):
  color = r.board[pol1][1]
  if pol2 == pol1:
    print("Nie możesz wykonać tego ruchu. Error 0032")
  elif pol2>63:
    return "nie"
  elif r.board[pol1][0]=="S":
    ruchS(pol1,pol2)
  elif r.board[pol1][0]=="P":
    if color=="b":
      pm.ruchPb(pol1,pol2)
    elif color=="c":
      pm.ruchPc(pol1,pol2)
  elif r.board[pol1][0]=="W":
    ruchW(pol1,pol2)
  elif r.board[pol1][0]=="K":
    ruchK(pol1,pol2)
  else:
    print("Nie można wykonać ruchu Error 0031")

def jakDaleko(pol1,pol2):
  if type(pol1)==int:
    pol1 = s.naZnaki(pol1)
    pol2 = s.naZnaki(pol2)
  x = s.litery.index(pol1[0])-s.litery.index(pol2[0])
  if x<0:
    x = x*-1
  y = int(pol1[1])-int(pol2[1])
  if y<0:
    y = x*-1
  return y+x


def ruchS(pol1,pol2):
  SMoves = [-17,-10,-15,-6,17,10,15,6]
  for x in SMoves:
    if pol1+x==pol2 and jakDaleko(pol1,pol2)==3:
      r.board[pol1],r.board[pol2]=r.board[pol2],r.board[pol1]
def ruchK(pol1,pol2):
  KMoves = [-9,-8,-7,-1,1,7,8,9]
  for x in KMoves:
    if pol1+x==pol2 and jakDaleko(pol1,pol2)<3:
      print(pol1+x,pol2)
      r.board[pol1],r.board[pol2]=r.board[pol2],r.board[pol1]


def ruchW(pol1, pol2):
  if r.board[pol2]!="⬜︎": #czy bicie
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

