import turtle
import math

def circle(t, x, y, radius):
   dist = 2.0*math.pi*radius /120.0
   t.penup()
   t.hideturtle()
   t.setposition(x, y)
   t.pendown() 
   for n in range(0, 150):
       t.fd(dist)
       t.right(3)

def main():
   x = 0
   y = 0
   radius = 100
   t = turtle.Turtle()
   circle(t, x, y, radius)


if __name__ == '__main__':
   main()
   turtle.mainloop()
