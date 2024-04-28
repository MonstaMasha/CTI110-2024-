Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> wn = turtle.Screen()
>>> wn.bgcolor("aliceblue")
>>> 
>>> bonnie = turtle.Turtle()
>>> bonnie.color("lime")
>>> bonnie.pensize(5)
>>> 
>>> chica = turtle.Turtle()
>>> chica.color("teal")
>>> chica.pensize(5)
>>> 
>>> bonnie.forward(90)
>>> bonnie.left(135)
>>> bonnie.forward(90)
>>> bonnie.left(110)
>>> bonnie.forward(70)
>>> bonnie.left(135)

>>> chica.left(270)
>>> chica.forward(100)
>>> chica.left(90)
>>> chica.forward(100)
>>> chica.left(90)
>>> chica.forward(100)
>>> chica.left(90)
>>> chica.forward(100)
>>> chica.left(90)
>>> 
>>> wn.mainloop()
