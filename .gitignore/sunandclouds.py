x = 320
height = 480
def setup():
    size (640, 480)
def draw():    
    global x
    global height
    global length
    
    if height <= -480:
        height = 480
    height -= 1
    
    background(0,0,255)
    
    noStroke()
    fill(255, 255, 0)
    ellipse(x, height, 70, 70)
    fill(255, 255, 255)
    ellipse(60, 80, 60, 60)
    ellipse(80, 100, 60, 60)
    ellipse(50, 100, 60, 60)
    ellipse(510, 80, 60, 60)
    ellipse(530, 100, 60, 60)
    ellipse(500, 100, 60, 60)
    fill(69,139,0)
    rect(1, 350, 640, 180)
