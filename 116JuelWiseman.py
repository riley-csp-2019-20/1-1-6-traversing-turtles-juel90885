#   a116_traversing_turtles.py


import turtle as trtl


# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    #get colors for from color list
    new_color = turtle_colors.pop()
    #set the turtles color
    t.color(new_color) 
    my_turtles.append(t)

#  
startx = 0
starty = 0

#
count = 1
for t in my_turtles:
    t.up()
    t.goto(startx, starty)
    t.down()
    t.right(45*count)     
    t.forward(50)

    #	
    startx = t.xcor()
    starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()