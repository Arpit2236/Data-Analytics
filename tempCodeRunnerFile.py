r('black')
pencolor('white')
side = 6
colors =['red', 'yellow', 'blue', 'green', 'orange', 'purple']
for i in range(side):
    fd(200)
    for i in range(side):
        fd(100)
        lt(360/side)
        begin_fill()
        fillcolor(colors[i%6])
        for i in range(side)