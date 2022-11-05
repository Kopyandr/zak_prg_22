
import turtle 

# HRQCÍ POLE ? 
turtle.speed(10)
print("Hra piškvorky: velikost pole je 50 jednotek. Stejně jako papírkové piškvorky hra neoznamuje vítěze")
for u in range (3):
    for i in range (3):
        for j in range (4):
            turtle.forward(50)
            turtle.left(90)
        turtle.forward(50)
    turtle.left(180)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
turtle.left(45)
for i in range (9): #Hráč 1 udává svuj tah 
        print("Hráč 1")
        x=int(input("souradnice x: "))
        y=int(input("souradnice y: "))  
        while ((x>0 and x<50)or(x>50 and x<100)or(x>100)) or ((y>0 and y<50)or(y>50 and y<100)or(y>100)): #při použití (!=) nejde vložid více argumentů
            if ((x>0 and x<50)or(x>50 and x<100)or(x>100)):
                x=int(input("zadej x znovu dobre pls: "))
            if ((y>0 and y<50)or(y>50 and y<100)or(y>100)):
                y=int(input("zadej y dobre ale: "))
        else:
            yy=(y+50)
            turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
            turtle.forward(75)
            turtle.penup()
            turtle.goto(x,yy) 
            turtle.pendown()
            turtle.right(90)
            turtle.forward(75)
            turtle.left(90)
        for p in range(1): # hrač 2 udává svuj tah 
            print("Hráč 2")
            a=int(input("zadej souradnicu x: "))
            b=int(input("zadej souřadnicu y: "))
            while ((a>0 and a<50)or(a>50 and a<100)or(a>100)) or ((b>0 and b<50)or(b>50 and b<100)or(b>100)):  
                if ((a>0 and a<50)or(a>50 and a<100)or(a>100)):
                    a=int(input("zadej x znovu ale dobre brooo cmon: "))
                if ((b>0 and b<50)or(b>50 and b<100)or(b>100)):
                    b=int(input("notak, pravidla už znáš ;): "))
            else: 
                vstupx=a+42 # posunutí kruhu tak aby byl v hracím poly 
                vstupy=b+6
                turtle.penup()
                turtle.goto(vstupx,vstupy)
                turtle.pendown()
                turtle.circle(25)
        
turtle.exitonclick()