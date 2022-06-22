import moves as m
import pawnMove as pm
import main as r

poleBK = 60 
poleCK = 4

def IsSzach(color):
    i = 0
    print("I am here")
    print(i)
    for pole in r.board:
        if pole[1]==color:
            boardstary = r.board[:]
            m.ruch(i,poleCK,0)
            if boardstary!=r.board:
                r.board = boardstary[:]
                print("Szach debilu")
                break
        i+=1
    