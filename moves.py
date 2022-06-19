import main as r
import start as s

def ruch(pol1, pol2):
  color = r.board[pol1][1]
  if pol2 == pol1:
    print("Nie możesz wykonać tego ruchu. Error 0032")
  elif r.board[pol1][0]=="P":
    if color=="b":
      ruchPb(pol1,pol2)
    elif color=="c":
      ruchPc(pol1,pol2)
  elif r.board[pol1][0]=="W":
    ruchW(pol1,pol2)
  else:
    print("Nie można wykonać ruchu Error 0031")

   
def ruchW(pol1, pol2):         #bicie trzeba zrobic 
  if r.board[pol2]!="⬜︎": 
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
  if pol2 - 8 == pol1:
    if r.board[pol2]!="⬜︎":    
      print("Nie możesz wykonać tego ruchu. Pole zajęte. (+1)",pol1,r.board[pol2])
    else:
      r.board[pol1],r.board[pol2] = r.board[pol2],r.board[pol1]
      if pol2 >=56 and pol2 <=63:
        promo(pol2,'c')

  elif r.board[pol2]!="⬜︎":                   #jeśli coś zbija
    
    if r.board[pol2][1] == "b" and r.board[pol1][1] == "c":
      
      if pol2 - 9 == pol1:
        PnoLeft = [63,55,47,39,31,23,15]
        if pol1 in PnoLeft:
          print("Nie możesz wykonać tego ruchu Error 0012")
        else:
          r.board[pol2] = r.board[pol1]
          r.board[pol1] = "⬜︎"
          print("Zbite.")
          if pol2 >=56 and pol2 <=63:
            promo(pol2,'c')

      elif pol2 - 7 == pol1:
        PnoRight = [0,8,16,24,32,40,48,56]
        if pol1 in PnoRight:
          print("Nie możesz wykonać tego ruchu Error 001")
        else:
          r.board[pol2] = r.board[pol1]
          r.board[pol1] = "⬜︎"
          print("Zbite.")
          if pol2 >=56 and pol2 <=63:
            promo(pol2,'c')
  if pol2 - 16 == pol1:
    polW = pol2 - 8
    if r.board[polW] == "⬜︎":
      print("Pol1 =",pol1)
      if pol1 >= 8 and pol1 <= 15:
        if r.board[pol2]!="⬜︎":    
          print("Nie możesz wykonać tego ruchu. Pole zajęte. (+2)",pol1,r.board[pol2])
        else:
          r.board[pol1],r.board[pol2] = r.board[pol2],r.board[pol1]
      else:
        print("Nie możesz wykonać tego ruchu Error021")
    else:
      print("Nie możesz wykonać tego ruchu Error02")

def ruchPb(pol1,pol2):  
  if pol2 + 8 == pol1:
    if r.board[pol2]!="⬜︎":    
      print("Nie możesz wykonać tego ruchu. Pole zajęte. (+1)",pol1,r.board[pol2])
    else:

      r.board[pol1],r.board[pol2] = r.board[pol2],r.board[pol1]
      if pol2 >=0 and pol2 <=7:
        promo(pol2,'b')                      #Promocja, przekazanie danych odnośnie promocji

  elif pol2 + 16 == pol1:
    polW = pol2 + 8
    if r.board[polW] == "⬜︎":
      if pol1 >= 48 and pol1 <= 55:
        if r.board[pol2]!="⬜︎":    
          print("Nie możesz wykonać tego ruchu. Pole zajęte. (+2)",pol1,r.board[pol2])
        else:
          r.board[pol1],r.board[pol2] = r.board[pol2],r.board[pol1]
      else:
        print("Nie możesz wykonać tego ruchu")
    else:
      print("Nie możesz wykonać tego ruchu")
  
  elif r.board[pol2]!="⬜︎":                   #czy coś zbija
    if r.board[pol2][1] == "c" and r.board[pol1][1] == "b":
    
      if pol2 + 9 == pol1:
        PnoLeft = [0,8,16,24,32,40,48,56]

        if pol1 in PnoLeft:
          print("Nie możesz wykonać tego ruchu")
          
        else:
          r.board[pol2] = r.board[pol1]
          r.board[pol1] = "⬜︎"
          print("Zbite.")
          if pol2 >=0 and pol2 <=7:
            promo(pol2, 'b')

      elif pol2 + 7 == pol1:
        PnoRight = [63,55,47,39,31,23,15]
        if pol1 in PnoRight:
          print("Nie możesz wykonać tego ruchu")
        else:
          r.board[pol2] = r.board[pol1]
          r.board[pol1] = "⬜︎"
          print("Zbite.")
          if pol2 >=0 and pol2 <=7:
            promo(pol2, "b")
  elif pol2 + 16 == pol1:
    polW = pol2 + 8
    if r.board[polW] == "⬜︎":
      if pol1 >= 48 and pol1 <= 55:
        if r.board[pol2]!="⬜︎":    
          print("Nie możesz wykonać tego ruchu. Pole zajęte. (+2)",pol1,r.board[pol2])
        else:
          r.board[pol1],r.board[pol2] = r.board[pol2],r.board[pol1]
      else:
        print("Nie możesz wykonać tego ruchu")
    else:
      print("Nie możesz wykonać tego ruchu")
  else:
    print("Nie możesz wykonać tego ruchu")  

def promo(pol2, side):
  print("")
  if r.board[pol2][0] == "P":
    print("---------------")
    print("Promocja. W co chcesz się zamienić?")
    print("[1]S [2]W [3]G [4]D")
    print("")
    try:
      Wybór = int(input())
      if Wybór == 1:
        r.board[pol2] = "S" + side
        r.clear()
      elif Wybór == 2:
        r.board[pol2] = "W" + side
        r.clear()
      elif Wybór == 3:
        r.board[pol2] = "G" + side
        r.clear()
      elif Wybór == 4:
        r.board[pol2] = "D" + side
        r.clear()
      else:
        print("Nie możesz dokonać tej zmiany. Error Z001")
      print("")
    except:
      pass
