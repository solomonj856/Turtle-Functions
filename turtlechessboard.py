import turtle
import turtleshapes

turtle.color('black', 'red')

turtle.pensize(8)

turtle.speed(0)



#x and y coordinate of turtle
x = -300
y = 300


white = 'white'
black = 'black'
row = 0

for i in range(64):

    if i % 2 == 0:
        turtle.fillcolor(white) #if even number, fill white
    
    elif i % 2 == 1:
        turtle.fillcolor(black) # if odd number, fill black
        
            
    turtle.begin_fill() #fills shape
    turtleshapes.square(x, y) #draws square function
    turtle.end_fill()
    
    x += 75
    
    if x == 300 and row % 2 == 0: #changes the colors for each row
        row += 1
        white = 'black'
        black = 'white'
        x = -300
        y -= 75
    elif x == 300 and row % 2 == 1:
        row += 1
        white = 'white'
        black = 'black'
        x = -300
        y -= 75
        
        
