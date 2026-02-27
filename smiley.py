import pgzrun
WIDTH=500
HEIGHT=700
def draw():
    screen.clear()
    screen.fill((0,0,210))
    screen.draw.filled_circle((250,350),(200),(255,255,0))
    screen.draw.filled_circle((150,250),(30),(0,0,0))
    screen.draw.filled_circle((350,250),(30),(0,0,0))
    screen.draw.filled_circle((250,400),(100),(0,0,0))
    screen.draw.filled_rect(Rect((150,300),(250,100)),(255,255,0))
pgzrun.go()
