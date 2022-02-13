"""
tic tac toe

Description:
"""
print("Welcome to tic tac toe")
mode=input("what mode do you want to play; (e)easy,(p)possible,(i)impossible: ")
modnum=1

import pygame
import random

pygame.init()
w=pygame.display.set_mode([600,600])
pygame.draw.line(w,(255,255,255),(200,0),(200,600))
pygame.draw.line(w,(255,255,255),(400,0),(400,600))
pygame.draw.line(w,(255,255,255),(0,200),(600,200))
pygame.draw.line(w,(255,255,255),(0,400),(600,400))

pygame.display.flip()

#setup
s1=" "
s2=" "
s3=" "
s4=" "
s5=" "
s6=" "
s7=" "
s8=" "
s9=" "
cord=""
omove=0
mewin=False
owin=False
tiewin=False

move=0
tie=s1!=" " and s2!=" " and s3!=" " and s4!=" " and s5!=" " and s6!=" " and s7!=" " and s8!=" " and s9!=" "  
#game
while True: 
    if mode=="p":
      modenum=random.randint(1,2)
    if mode=="i":
      modenum=2
    
    
    cord=input("Enter the cords in a x,y for where you want to place your mark. ex. 1,3 : ")
    if cord=="1,1":
        if s7==" ":
            s7="X"
            pygame.draw.line(w,(255,255,255),(0,400),(200,600))
            pygame.draw.line(w,(255,255,255),(0,600),(200,400))
    if cord=="2,1":
        if s8==" ":
            s8="X"
            pygame.draw.line(w,(255,255,255),(200,400),(400,600))
            pygame.draw.line(w,(255,255,255),(200,600),(400,400))
    if cord=="3,1":
        if s9==" ":
            s9="X"
            pygame.draw.line(w,(255,255,255),(400,400),(600,600))
            pygame.draw.line(w,(255,255,255),(400,600),(600,400))
    if cord=="1,2":    
        if s4==" ":
            s4="X"
            pygame.draw.line(w,(255,255,255),(0,200),(200,400))
            pygame.draw.line(w,(255,255,255),(0,400),(200,200))
    if cord=="2,2":
        if s5==" ":
            s5="X"
            pygame.draw.line(w,(255,255,255),(200,200),(400,400))
            pygame.draw.line(w,(255,255,255),(200,400),(400,200))
    if cord=="3,2":
        if s6==" ":
            s6="X"
            pygame.draw.line(w,(255,255,255),(400,200),(600,400))
            pygame.draw.line(w,(255,255,255),(400,400),(600,200))
    if cord=="1,3":
        if s1==" ":
            s1="X"
            pygame.draw.line(w,(255,255,255),(0,0),(200,200))
            pygame.draw.line(w,(255,255,255),(0,200),(200,0))
    if cord=="2,3":
        if s2==" ":
            s2="X"
            pygame.draw.line(w,(255,255,255),(200,200),(400,0))
            pygame.draw.line(w,(255,255,255),(200,0),(400,200))
    if cord=="3,3":
        if s3==" ":
            s3="X"
            pygame.draw.line(w,(255,255,255),(400,0),(600,200)) #finish opponent graphics
            pygame.draw.line(w,(255,255,255),(400,200),(600,0))
    if cord=="done":
        break

    pygame.display.flip()
    
    #winning
    #rows
    if s1=="X" and s2=="X" and s3=="X":
        mewin=True
        break
        
    if s4=="X" and s5=="X" and s6=="X":
        mewin=True
        break
        
    if s7=="X" and s8=="X" and s9=="X":
        mewin=True
        break
        
    #collums
    if s1=="X" and s4=="X" and s7=="X":
        mewin=True
        break
        
    if s2=="X" and s5=="X" and s8=="X":
        mewin=True
        break
        
    if s3=="X" and s6=="X" and s9=="X":
        mewin=True
        break
        
    #diagnals
    if s1=="X" and s5=="X" and s9=="X":
        mewin=True
        break
        
    if s3=="X" and s5=="X" and s7=="X":
        mewin=True
        break
    if tie:
        tiewin=True
        break
    move=0
    #create master mode functions
    if modenum==2:
    #    offense
        #  collums
        #   collum1 

        if move==0:
            if s1=="O" and s4=="O":
                if s7==" ":
                    s7="O"
                    move=1
        if move==0:
            if s7=="O" and s4=="O":
                if s1==" ":
                    s1="O"
                    move=1
        if move==0:
            if s1=="O" and s7=="O":
                if s4==" ":
                    s4="O"
                    move=1
        #collum 2
        if move==0:
            if s2=="O" and s5=="O":
                if s8==" ":
                    s8="O"
                    move=1
        if move==0:
            if s2=="O" and s8=="O":
                if s5==" ":
                    s5="O"
                    move=1
        if move==0:
            if s8=="O" and s5=="O":
                if s2==" ":
                    s2="O"
                    move=1
        #collum 3
        if move==0:
            if s3=="O" and s6=="O":
                if s9==" ":
                    s9="O"
                    move=1
        if move==0:
            if s9=="O" and s3=="O":
                if s6==" ":
                    s6="O"
                    move=1
        if move==0:
            if s9=="O" and s6=="O":
                if s3==" ":
                    s3="O"
                    move=1
        #rows
        #row 1
        if move==0:
            if s1=="O" and s2=="O":
                if s3==" ":
                    s3="O"
                    move=1
        if move==0:
            if s1=="O" and s3=="O":
                if s2==" ":
                    s2="O"
                    move=1
        if move==0:
            if s3=="O" and s2=="O":
                if s1==" ":
                    s1="O"
                    move=1
        #row 2
        if move==0:
            if s6=="O" and s5=="O":
                if s4==" ":
                    s4="O"
                    move=1
        if move==0:
            if s4=="O" and s5=="O":
                if s6==" ":
                    s6="O"
                    move=1
        if move==0:
            if s4=="O" and s6=="O":
                if s5==" ":
                    s5="O"
                    move=1
        #row 3
        if move==0:
            if s9=="O" and s8=="O":
                if s7==" ":
                    s7="O"
                    move=1
        if move==0:
            if s7=="O" and s8=="O":
                if s9==" ":
                    s9="O"
                    move=1
        if move==0:
            if s7=="O" and s9=="O":
                if s8==" ":
                    s8="O"
                    move=1
        #diagnals
        #dia1
        if move==0:
            if s1=="O" and s9=="O":
                if s5==" ":
                    s5="O"
                    move=1
        if move==0:
            if s1=="O" and s5=="O":
                if s9==" ":
                    s9="O"
                    move=1
        if move==0:
            if s5=="O" and s9=="O":
                if s1==" ":
                    s1="O"
                    move=1
        #dia2
        if move==0:
            if s3=="O" and s7=="O":
                if s5==" ":
                    s5="O"
                    move=1
        if move==0:
            if s7=="O" and s5=="O":
                if s3==" ":
                    s3="O"
                    move=1
        if move==0:
            if s3=="O" and s5=="O":
                if s7==" ":
                    s7="O"
                    move=1
        # deffense
        #  collums
        #   collum1 

        if move==0:
            if s1=="X" and s4=="X":
                if s7==" ":
                    s7="O"
                    move=1
        if move==0:
            if s7=="X" and s4=="X":
                if s1==" ":
                    s1="O"
                    move=1
        if move==0:
            if s1=="X" and s7=="X":
                if s4==" ":
                    s4="O"
                    move=1
        #collum 2
        if move==0:
            if s2=="X" and s5=="X":
                if s8==" ":
                    s8="O"
                    move=1
        if move==0:
            if s2=="X" and s8=="X":
                if s5==" ":
                    s5="O"
                    move=1
        if move==0:
            if s8=="X" and s5=="X":
                if s2==" ":
                    s2="O"
                    move=1
        #collum 3
        if move==0:
            if s3=="X" and s6=="X":
                if s9==" ":
                    s9="O"
                    move=1
        if move==0:
            if s9=="X" and s3=="X":
                if s6==" ":
                    s6="O"
                    move=1
        if move==0:
            if s9=="X" and s6=="X":
                if s3==" ":
                    s3="O"
                    move=1
        #rows
        #row 1
        if move==0:
            if s1=="X" and s2=="X":
                if s3==" ":
                    s3="O"
                    move=1
        if move==0:
            if s1=="X" and s3=="X":
                if s2==" ":
                    s2="O"
                    move=1
        if move==0:
            if s3=="X" and s2=="X":
                if s1==" ":
                    s1="O"
                    move=1
        #row 2
        if move==0:
            if s6=="X" and s5=="X":
                if s4==" ":
                    s4="O"
                    move=1
        if move==0:
            if s4=="X" and s5=="X":
                if s6==" ":
                    s6="O"
                    move=1
        if move==0:
            if s4=="X" and s6=="X":
                if s5==" ":
                    s5="O"
                    move=1
        #row 3
        if move==0:
            if s9=="X" and s8=="X":
                if s7==" ":
                    s7="O"
                    move=1
        if move==0:
            if s7=="X" and s8=="X":
                if s9==" ":
                    s9="O"
                    move=1
        if move==0:
            if s7=="X" and s9=="X":
                if s8==" ":
                    s8="O"
                    move=1
        #diagnals
        #dia1
        if move==0:
            if s1=="X" and s9=="X":
                if s5==" ":
                    s5="O"
                    move=1
        if move==0:
            if s1=="X" and s5=="X":
                if s9==" ":
                    s9="O"
                    move=1
        if move==0:
            if s5=="X" and s9=="X":
                if s1==" ":
                    s1="O"
                    move=1
        #dia2
        if move==0:
            if s3=="X" and s7=="X":
                if s5==" ":
                    s5="O"
                    move=1
        if move==0:
            if s7=="X" and s5=="X":
                if s3==" ":
                    s3="O"
                    move=1
        if move==0:
            if s3=="X" and s5=="X":
                if s7==" ":
                    s7="O"
                    move=1
    
    while move==0:
        omove=random.randint(1,9)
        if omove==1:
            if s1==" ":
                s1="O"
                move=1
        if omove==2:
            if s2==" ":
                s2="O"
                move=1
        if omove==3:
            if s3==" ":
                s3="O"
                move=1
        if omove==4:
            if s4==" ":
                s4="O"
                move=1
        if omove==5:
            if s5==" ":
                s5="O"
                move=1
        if omove==6:
            if s6==" ":
                s6="O"
                move=1
        if omove==7:
            if s7==" ":
                s7="O"
                move=1
        if omove==8:
            if s8==" ":
                s8="O"
                move=1
        if omove==9:
            if s9==" ":
                s9="O"
                move=1
    #oppo graphic
    if s1=="O":
      pygame.draw.circle(w,(255,255,255),(100,100),98,1)
    if s2=="O":
      pygame.draw.circle(w,(255,255,255),(300,100),98,1)
    if s3=="O":
      pygame.draw.circle(w,(255,255,255),(500,100),98,1)
    if s4=="O":
      pygame.draw.circle(w,(255,255,255),(100,300),98,1)
    if s5=="O":
      pygame.draw.circle(w,(255,255,255),(300,300),98,1)
    if s6=="O":
      pygame.draw.circle(w,(255,255,255),(500,300),98,1)
    if s7=="O":
      pygame.draw.circle(w,(255,255,255),(100,500),98,1)
    if s8=="O":
      pygame.draw.circle(w,(255,255,255),(300,500),98,1)
    if s9=="O":
      pygame.draw.circle(w,(255,255,255),(500,500),98,1)
    pygame.display.flip()
    #owin
    #rows
    if s1=="O" and s2=="O" and s3=="O":
        owin=True
        break
        
    if s4=="O" and s5=="O" and s6=="O":
        owin=True
        break
        
    if s7=="O" and s8=="O" and s9=="O":
        owin=True
        break
        
    #collums
    if s1=="O" and s4=="O" and s7=="O":
        owin=True
        break
        
    if s2=="O" and s5=="O" and s8=="O":
        owin=True
        break
        
    if s3=="O" and s6=="O" and s9=="O":
        owin=True
        break
        
    #diagnals
    if s1=="O" and s5=="O" and s9=="O":
        owin=True
        break
        
    if s3=="O" and s5=="O" and s7=="O":
        owin=True
        break
    if tie:
        tiewin=True
        break
    print("\n"*100)

#end

if mewin:
    print("You won =)")
if owin:
    print("The opponent won=(")
if tiewin:
    print("It is a tie, nobody wins")


        
        
        
    
    

