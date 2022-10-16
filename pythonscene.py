import turtle




turtle.pensize(8) # pen size for turtle

turtle.speed(0) #max speed


turtle.shape('turtle') 



turtle.pu() #pen up

screen = turtle.getscreen() #creates screen

def ground(x , y): #ground function
    turtle.color('green')
    turtle.fillcolor('green')
    turtle.begin_fill()
    turtle.goto(x , y - 300)
    turtle.pd()
    
    turtle.forward(2000)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(2000)
    turtle.right(90)
    turtle.forward(500)
    turtle.end_fill()
    turtle.pu()

    turtle.right(90)
def switzerland(x, y): #switzerland flag
    
    
    turtle.color('red', 'yellow')
    turtle.fillcolor('red')
    turtle.goto(x ,y)
    turtle.pd()

    turtle.begin_fill()
    
    for i in range(2):
        turtle.forward(500)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)

    turtle.end_fill()

    turtle.goto(x + 215, y - 260)
    turtle.color('white')
    distance = 75

    turtle.fillcolor('white')
    turtle.begin_fill()
    #makes white cross
    turtle.forward(distance)
    turtle.left(90)
    turtle.forward(distance)
    turtle.right(90)
    turtle.forward(distance)
    turtle.left(90)
    turtle.forward(distance)
    turtle.left(90)
    turtle.forward(distance)
    turtle.right(90)
    turtle.forward(distance)
    turtle.left(90)
    turtle.forward(distance)
    turtle.left(90)
    turtle.forward(distance)
    turtle.right(90)
    turtle.forward(distance)
    turtle.left(90)
    turtle.forward(distance)
    turtle.left(90)
    turtle.forward(distance)
    turtle.right(90)
    turtle.forward(distance)

    turtle.end_fill()
    turtle.pu()

    turtle.color('grey')
    turtle.fillcolor('grey')
    turtle.pensize(20)

    turtle.goto(x + 5 ,y -5)
    turtle.pd()
    turtle.forward(690)
    turtle.color('grey') #makes pole

    turtle.fillcolor('grey')

    
    

def sweden(x ,y): #sweden flag
    turtle.pu()
    
    turtle.right(270)
    turtle.colormode(255)
    turtle.color(0,106, 167)
    turtle.fillcolor(0,106, 167)
    turtle.goto(x,y)
    turtle.pd()
    


    turtle.begin_fill() #fills flag
    
    for i in range(2):
        turtle.forward(500)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)

    turtle.end_fill()
    
    
    turtle.pu()
    turtle.goto(x ,y - 125)
    turtle.color(254, 204, 2)
    turtle.fillcolor(254, 204, 2)
    
    turtle.pd()
    turtle.begin_fill()
    
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(50)
    

    turtle.end_fill()

    turtle.pu()
    turtle.goto(x + 150 ,y)
    turtle.right(180)


    turtle.pd()
    turtle.begin_fill()
    
    
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(50)
    turtle.end_fill()
    turtle.pu()

    turtle.color('grey')
    turtle.fillcolor('grey')
    turtle.pensize(20)

    turtle.goto(x ,y)
    turtle.pd()
    turtle.left(90)
    turtle.forward(690)
    turtle.color('grey') #makes pole

    turtle.fillcolor('grey')

    turtle.hideturtle()

    
ground(-1000, 0)        
switzerland(100, 400)
sweden(-500, 400)
