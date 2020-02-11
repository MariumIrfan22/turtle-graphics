#!/usr/bin/env python
# coding: utf-8

# # Turtle Graphics

# In[1]:


#smileyface
import turtle
s=turtle.Screen()
t=turtle.Turtle()
t.pensize(3)
x=-100
y=100
t.goto(x, y)
t.undo()
t.penup()
t.goto(x, y)
t.pendown()
t.circle(100)
t.penup()
t.goto(x-35, y+120)
t.pendown()
t.dot(25)
t.penup()
t.goto(x+35, y+120)
t.pendown()
t.dot(25)
t.penup()
t.goto(x-60.62, y+65)
t.pendown()
t.setheading(-60)
t.circle(70, 120)


# In[1]:


#seasideside turtle
import turtle
s=turtle.Screen()
t=turtle.Turtle(shape='turtle')
t.penup()
t.goto(-300,0)
t.pendown()
t.setheading(-45)
t.circle(50, 90)
t.setheading(-45)
t.circle(50, 90)
t.setheading(-45)
t.circle(50, 90)
t.setheading(-45)
t.circle(50, 90)
t.setheading(-45)
t.circle(50, 90)
t.setheading(-45)
t.circle(50, 90)
t.setheading(-45)
t.circle(50, 90)
t.penup()
t.goto(-100, 200)
t.pendown()
t.circle(50)
t.penup()
t.goto(0, -50)


# In[1]:


#CS.2#square
import turtle
s=turtle.Screen()
t=turtle.Turtle()
t.pensize(5)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)


# In[3]:


#CS.3#diagonal
import turtle
s=turtle.Screen()
t=turtle.Turtle()
t.pensize(5)
t.pencolor('red')
s.bgcolor("black")
t.left(45)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)



# In[1]:


#cs.4#pentagon
import turtle
s=turtle.Screen()
t=turtle.Turtle()
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)


# In[1]:


#cs.4 #hexagon
import turtle
s=turtle.Screen()
t=turtle.Turtle()
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)


# In[1]:


#hectagon
import turtle
s=turtle.Screen()
t=turtle.Turtle()
t.forward(100)
t.left(51.43)
t.forward(100)
t.left(51.43)
t.forward(100)
t.left(51.43)
t.forward(100)
t.left(51.43)
t.forward(100)
t.left(51.43)
t.forward(100)
t.left(51.43)
t.forward(100)
t.left(51.43)
s.bye()


# In[1]:


#octagon
import turtle
s=turtle.Screen()
t=turtle.Turtle()
t.forward(100)
t.left(45)
t.forward(100)
t.left(45)
t.forward(100)
t.left(45)
t.forward(100)
t.left(45)
t.forward(100)
t.left(45)
t.forward(100)
t.left(45)
t.forward(100)
t.left(45)
t.forward(100)
t.left(45)
s.bye()


# In[4]:


#cs.5
import turtle
s=turtle.Screen()
t=turtle.Turtle()
t.penup()
t.goto(0,100)
t.pendown()
t.circle(100)
t.penup()
t.goto(-100,0)
t.pendown()
t.circle(100)
t.penup()
t.goto(100,0)
t.pendown()
t.circle(100)
s.bye()


# In[2]:


#cs.6
import turtle
s=turtle.Screen()
t=turtle.Turtle()
def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
t.circle(25)
jump(t,0,-25)
t.circle(50)
jump(t,0,-50)
t.circle(75)
jump(t,0,-75)
t.circle(100)


# In[3]:


#cs.7
import turtle
s=turtle.Screen()
t=turtle.Turtle(shape="turtle")
a=turtle.Turtle(shape="turtle")
b=turtle.Turtle(shape="turtle")
t.penup()
t.goto(-300,0)
t.pendown()
t.setheading(-45)
t.circle(50,90)
t.setheading(-45)
t.circle(50,90)
t.setheading(-45)
t.circle(50,90)
t.setheading(-45)
t.circle(50,90)
t.setheading(-45)
t.circle(50,90)
t.setheading(-45)
t.circle(50,90)
t.penup()
t.goto(-100,200)
t.pendown()
t.circle(50)
t.penup()
t.goto(0,-50)
t.pendown()
a.penup()
a.goto(-150,-50)
a.pendown()
b.penup()
b.goto(+50,-70)
b.pendown()


# In[2]:


#cs.8
import turtle
s=turtle.Screen()
a=turtle.Turtle()
b=turtle.Turtle()
s.bgcolor("blue")
a.pensize(3)
b.pensize(5)
a.pencolor("green")
b.pencolor("yellow")
a.penup()
a.goto(-300,0)
a.pendown()
a.circle(1)
a.penup()
b.penup()
b.goto(100,0)
b.pendown()
b.circle(109)
b.penup()


# In[3]:


help(turtle)


# In[1]:


#cs.9
import turtle
s=turtle.Screen()
t=turtle.Turtle()
def star():
    for i in range(5):
        t.forward(100)
        t.right(144)

star()


# In[1]:


#cs.10
import turtle
s=turtle.Screen()
t=turtle.Turtle()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)


# In[6]:


#cs.11
import turtle
s=turtle.Screen()
t=turtle.Turtle()
t.pensize(3)
t.penup()
t.goto(0,0)
t.pendown()
t.dot(25)
t.penup()
t.goto(0,-50)
t.pendown()
t.circle(50)
t.goto(0,160)
t.goto(0,-160)
t.goto(300,-160)
t.goto(300,160)
t.goto(-300,160)
t.goto(-300,-160)
t.goto(0,-160)
t.penup()
t.goto(-300,-120)
t.pendown()
t.circle(120,180)
t.penup()
t.goto(300,120)
t.pendown()
t.circle(120,180)
t.penup()
t.goto(-300,40)
t.pendown()
t.forward(80)
t.right(90)
t.forward(80)
t.right(90)
t.forward(80)
t.penup()
t.goto(-220,30)
t.pendown()
t.circle(30,-180)
t.penup()
t.goto(300,40)
t.pendown()
t.left(180)
t.forward(80)
t.left(90)
t.forward(80)
t.left(90)
t.forward(80)
t.left(90)
t.forward(80)
t.penup()
t.goto(220,30)
t.pendown()
t.left(90)
t.circle(30,180)
t.penup()
t.goto(280,0)
t.pendown()
t.setheading(90)
t.goto(280,20)
t.goto(280,-20)
t.goto(280,0)
t.circle(10)
t.penup()
t.goto(-280,0)
t.pendown()
t.goto(-280,20)
t.goto(-280,-20)
t.goto(-280,0)
t.setheading(270)
t.circle(10)


# In[1]:


#CS.12
import turtle
def jump(n,x,y):
    n.penup()
    n.goto(x,y)
    n.pendown()
s=turtle.Screen()
s.bgcolor('black')
t=turtle.Turtle()                 #for text
t.color('deep pink')
style=('courier',16,'bold')
jump(t,-460,360)
t.write('Waxing cresent',font=style, align='left')
t.hideturtle()
g=turtle.Turtle()                 #for each background colour
g.pencolor('grey')
g.fillcolor('grey')
g.begin_fill()
jump(g,-460,250)
for i in range(4):
    g.forward(110)
    g.left(90)
g.end_fill()
a=turtle.Turtle()                 #wasing cresent
a.pencolor('white')
a.fillcolor('white')
a.begin_fill()
jump(a,-400,260)
a.circle(40)
a.end_fill()
g.fillcolor('grey')
g.begin_fill()
jump(g,-420,260)
g.circle(40)
g.end_fill()

jump(t,-200,360)                # first quater
t.write('First Quater',font=style, align='left')
jump(g,-200,250)
g.fillcolor('grey')
g.begin_fill()
for i in range(4):
    g.forward(110)
    g.left(90)
g.end_fill()
jump(a,-140,260)
a.begin_fill()
a.circle(40,180)
a.end_fill()

jump(t,10,360)                # waxing gibbous 
t.write('waxing gibbous',font=style,align='left')
jump(g,10,250)
g.begin_fill()
for i in range(4):
    g.forward(110)
    g.left(90)
g.end_fill()
jump(a,60,260)
a.circle(40)





jump(t,220,360)              # full moon
t.write('full moon',font=style,align='left')
jump(g,220,250)
g.begin_fill()
for i in range(4):
    g.forward(110)
    g.left(90)
g.end_fill()
jump(a,270,260)
a.begin_fill()
a.circle(40)
a.end_fill()
g.hideturtle()
a.hideturtle()





# In[1]:


import turtle
def jump(n,x,y):
    n.penup()
    n.goto(x,y)
    n.pendown()
s=turtle.Screen()
s.bgcolor('red')
t=turtle.Turtle()
a=turtle.Turtle()
b=turtle.Turtle()
a.pencolor('red')
b.pencolor('blue')
t.pencolor('green')
b.circle(100)
t.right(180)
t.circle(0)


# In[ ]:




