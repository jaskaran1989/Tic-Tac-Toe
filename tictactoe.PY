
a=[[1,2,3],[4,5,6],[7,8,9]]       ## fixed list of 3 dimension grid named=a
gwin=False    ## boolean value

player1="x" ## assigning player
size=9      ##variable of loop
r=0         ##row variable which is assign to that position which we get after clculation for  assiging x or o player
c=0         ## column variable which is assign to that position which we get after clculation for  assiging x or o player
b=0



print("*"*40)
print("-"*40)                                 ##  welcoming players   
print(" "*10+"WELCOME TO TIC-TAC-TOE"+" "*10) ##    to really entertaning
print("-"*40)                                 ##    game 
print("*"*40)                                

                
def wincheck(): 
        """
        this function checks the winner
        of the game
        """
        xwin=False
        owin=False
        win=False
        for i in range (3) :
                
                if (a[i][0]=="x" and a[i][1]== "x" and a[i][2]== "x" ):
                        xwin=True
                        win=True
                elif (a[i][0]=="o" and a[i][1]== "o" and a[i][2]== "o"):
                        owin=True
                        win=True
                elif (a[0][i]=="x" and a[1][i]== "x" and a[2][i]== "x" ):
                        xwin=True
                        win=True
                elif (a[0][i]=="o" and a[1][i]== "o" and a[2][i]== "o"):
                        owin=True
                        win=True
                elif (a[i][0]=="x" and a[1][1]=="x" and a[2][2]=="x"):
                        xwin=True
                        win=True
                elif (a[0][2]=="o" and a[1][1]=="o" and a[2][0]=="o"):
                        owin=True
                        win=True
        if ((a[0][0]=="x" and a[1][1]=="x" and a[2][2]=="x") or (a[0][2]=="x" and a[1][1]=="x" and a[2][0]=="x")):
                xwin=True
                win=True
               ## print("x is winner")
                        
                                
        elif ((a[0][0]=="o" and a[1][1]=="o" and a[2][2]=="o") or( a[0][2]=="o" and a[1][1]=="o" and a[2][0]=="o")):
                owin=True
                win=True
               ## print("o is winner")
                

        if (xwin==True and owin==True):
                print("boring draw!!!")
                
        elif(xwin==True and owin==False):
                print("X wins")
        elif(xwin==False and owin==True):
                print("o wins")
        elif (size==0 and (xwin==False and owin==False)):
                print("boring draw!!!")
        
        
        return win


def Printboard():    
        """
        this Printboard function help in
        printing my tic tac toe board
        """
        if (size>=0 or gwin==False):
                print("Tic tac toe board")
        else:
                print("Final tic tac toe board")
       ## print("print board call gwin "+str(gwin))

        
        print("|"+"---|"*3)
        for rows in range(len(a)):
                for columns in range(len(a[rows])):
                        if columns==0:
                                print("|",end=" ")
                        print(str(a[rows][columns])+" |",end=" ")
                print()
                print("|"+"---|"*3)
                 


Printboard()                                      ##calling function


b=input("player x its your turn choose your position")
while (len(b)!=1) or not(b>="1" and b<="9"):                    ## error checking part
        print(b,end=" "+"is ")                                ##which ensures that user
        print("invalid input please enter from 1 to 9")          ## didnot enter anyother thing 
        b=input("choose  one of positions")                    ## except numbers 1 to 9   

b=int(b)



c=(b-1)%3   ## calculation of colums position
r=(b-1)//3  ## calculation for row position


while((gwin==False) and (size>0) ):
        c=(b-1)%3   ## calculation of colums position
       
        r=(b-1)//3  ## calculation for row position
       
        ##if statement mentioned under is doing work for overlapping 
        if (a[r][c]==1 or a[r][c]== 2 or a[r][c]==3 or a[r][c]==4 or a[r][c]==5 or a[r][c]==6 or a[r][c]==7 or a[r][c]==8 or a[r][c]==9 ):
                print()                                                                                                                    
                a[r][c]=player1
                size=size-1
                        
                
                Printboard()   ##calling function Printboard
                gwin=wincheck() ##Calling function wincheck
        

                if (size>0 and gwin==False):
                                        
                        if player1 == "x":      ## player1=x flips 
                                player1 = "o"   ## to player1=o
                        else:
                                player1 = "x"

                        print("player " + player1+" it is your turn") 
                        b=input("choose your position")


                                
                        while (len(b)!=1) or not(b>="1" and b<="9"):
                                print(b,end=" "+"is ")
                                print("invalid input please enter from 1 to 9")
                                b=input("choose your position")

                        b=int(b)      
                       
        else:
                print("Sorry this place is already filled")
                b=input("choose your position")
                b=int(b)
        


