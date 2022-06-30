import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("palegreen")

t.speed(0)
t.shape("turtle")
t.color("blue")
t.stamp()
t.ht()
t.left(90)
len1 = 100
len2 = 10
len3 = 20
len123 = len1 + len2 + len3

for i in range(12):
  t.penup()
  t.fd(len1)
  t.pendown()
  t.fd(len2)
  t.penup()
  t.fd(len3)
  t.pendown()
  t.stamp()
  t.penup()
  t.bk(len123)
  t.rt(30)