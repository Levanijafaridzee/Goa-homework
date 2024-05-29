from turtle import *
speed(0)
#we want to paint a house


#step 1: draw a square
width(7)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

#door

left(90)
forward(70) 
begin_fill()
color("pink")
left(90)
forward(100)
right(90)
forward(60)
left(270)
forward(100) 
end_fill


#roof\

penup()
goto(200,200)
pendown()
begin_fill()
color("blue")
right(145)
forward(170)
left(109)
forward(167)
end_fill()
right(54)
#window
penup()

goto(170,170)
pendown()
color("yellow")
begin_fill()
forward(40)
left(90)
forward(35)
left(90)
forward(40)
left(90)
forward(35)
end_fill()
#window end

penup()
goto(30,170)
pendown()
begin_fill()
right(90)
forward(40)
right(90)
forward(35)
right(90)
forward(40)
right(90)
forward(35)
end_fill()


penup()
goto(200,100)
forward(100) 
pendown()
color("black")
right(90)
forward(150)
right(90)
forward(200)
right(90)
forward(150) 
right(90)
forward(200)
left(35)
forward(170)
left(107)
forward(170)
left(180)
forward(170)
right(50)
forward(243) 
right(90)
forward(150)
end_fill()

penup()
goto(0,0)
right(91)
pendown()
forward(390)




exitonclick()