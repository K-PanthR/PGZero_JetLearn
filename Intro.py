import pgzrun

WIDTH=500
HEIGHT=500
def draw():
  screen.clear()
  screen.fill("white")
  screen.draw.line((20,20),(206,206),"black")
  screen.draw.circle((250,250),80,"black")
  screen.draw.filled_circle((250,250),80,"black")

pgzrun.go()