import turtle



def square(x, y):

    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    for i in range(4):
        turtle.forward(75)
        turtle.right(90)

def star(x, y):
     
    turtle.goto(x,y)
    

    turtle.pd()
    
    for i in range(5):
    
        turtle.forward(200)
        turtle.left(216)

    
def pentagon(x, y):

     
    turtle.goto(x,y - 125)
    

    turtle.pd()
    
    for i in range(5):
    
        turtle.forward(200)
        turtle.left(72)



