import moves as m
import pawnMove as pm
import main as r

poleBK = 60 
poleCK = 4

def IsSzach(ruchCB):
    i = 0
    x = ["b", "c"]
    for i in x:
        for pole in r.board:
            if pole[1]==ruchCB:
             boardstary = r.board[:]
             m.ruch(i,4,not ruchCB)
             if boardstary!=r.board:
                r.board = boardstary[:]
                print("Szach")
                return True
            i = 0
        i+=1


def IsMat(ruchCB):
    KMoves = [-9,-8,-7,-1,1,7,8,9]
    for move in KMoves:
        boardstary = r.board[:]
        m.ruchK(poleCK,poleCK+move)
        if IsSzach(ruchCB) == True:
            print("mat")
            return False
        r.board = boardstary[:]