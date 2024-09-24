from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')
def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.01)
    
def run_top():
    print('TOP')
    for x in range(0,800,10):
        draw_boy(x,550)
def run_right():
    print('RIGHT')
    for y in range(600,0,-10):
        draw_boy(800,y)
def run_bottom():
    print('BOTTOM')
    for x in range(800,0,-10):
        draw_boy(x,0)
def run_left():
    print('LEFT')
    for y in range(0,600,10):
        draw_boy(0,y)
def run_t_top():
    print('tTOP')
    for x in range(0,600,10):
        draw_boy(x,600)
def run_t_right():
    print('tRIGHT')
    for y in range(600,0,-10):
        draw_boy(600,y)
def run_t_bottom():
    print('tBOTTOM')
    for x in range(600,0,-10):
        draw_boy(x,0)
def run_t_diagonal():
    print('DIAGONAL')
    y=0
    for x in range(600,0,-10):
        y=y+10
        draw_boy(x,y)
    
    
def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_right()
    run_bottom()
    run_left()
    
def run_triangle():
    print('TRIANGLE')
    run_t_top()
    run_t_right()
    run_t_diagonal()
    

def run_circle():
    print('CIRCLE')

    r,cx,cy=300,800//2,600//2
    
    for d in range(0,360,1):
      x=r*math.cos(math.radians(d))+cx
      y=r*math.sin(math.radians(d))+cy
      draw_boy(x,y)


while True:
    
    run_circle()
    run_rectangle()
    run_triangle()
    
close_canvas()
