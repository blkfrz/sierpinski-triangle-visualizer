'''
This is a simple Sierpinski Triangle fractal visualization.
Pygame is used in order to display points in the screen.
At first a particular point inside the area of a predefined triangle is selected.
After that, one of the three vertices will be chosen at random. A new point will
be drawn at the midpoint between the current point and the chosen vertex.
If this process happens enough times, a triangular pattern will emerge.

I may improve on this later.
'''
#Import needed modules.

import pygame
import random
import math
 
#Initializing pygame screen and fonts.
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Arial',30)

#All messages at initial state. TAB for toggling command view not included.
points_displayed = myfont.render('Points: 0', False, (255, 255, 255))
auto_toggle = myfont.render('Auto: False', False, (255, 255, 255))
resetcommand = myfont.render('r - reset', False, (255, 255, 255))
autocommand = myfont.render('a - auto', False, (255, 255, 255))
plotcommand = myfont.render('space - plot', False, (255, 255, 255))
tickspeed = myfont.render('Tick: 10', False, (255, 255, 255))
show_info = True


#Constants to simplify code. Modifying this should be ok.
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
WIDTH = 1000
HEIGHT = 1000

TRIANGLE_SIZE = 500

STARTING_POINT = [-50,-50] #Could be any point inside the area described by points in TRIANGLE_POINTS.
#There's no verification, so make sure the selected point is valid.


MAX_TICK = 5000
MIN_TICK = 10
tick = 10 # Be careful changing the tick speed. This shouldn't be too high nor should it be 0, otherwise it's costful.

TRIANGLE_POINTS = [[TRIANGLE_SIZE/2,0],[-TRIANGLE_SIZE/2,0],[0,-TRIANGLE_SIZE]] #Vertices of an equilateral triangle.

NORMALIZED_POINTS = []
normalize = lambda a : [int(a[0] + WIDTH/2), int(a[1]+ HEIGHT/1.5)]
# Basically center points, could be more clear.


STARTING_POINT = normalize(STARTING_POINT)
for triangle in TRIANGLE_POINTS:
    NORMALIZED_POINTS.append(normalize(triangle))


size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sierpinski Triangle")
 

done = False
clock = pygame.time.Clock()
i = 10000
finished_iteration = True

drawn_points = []

''' It is necessary to store all points drawn at a given moment, they all need to be drawn one by one for EVERY
iteration. I didn't find a way to permanently change a point without doing this so if you get enough points
this WILL be costful.'''

current_point = STARTING_POINT
auto = False
while not done:
 
    clock.tick(tick)
    
    #Check for keys pressed or program closing.
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE :
                if not auto:
                    finished_iteration = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE :
                finished_iteration = False
            elif event.key == pygame.K_r:
                drawn_points.clear()
            elif event.key == pygame.K_a:
                if not auto:
                    auto = True
                    finished_iteration = False
                else:
                    auto = False
                    finished_iteration = True
            elif event.key == pygame.K_r:
                drawn_points.clear()
            elif event.key == pygame.K_UP:
                if tick < MAX_TICK:
                    tick+=5
            elif event.key == pygame.K_DOWN:
                if tick > MIN_TICK:
                    tick-=5
            elif event.key == pygame.K_TAB:
                if show_info:
                    show_info = False
                else:
                    show_info = True
                
    screen.fill(BLACK)

    for triangles in NORMALIZED_POINTS:
        #pygame.draw.circle(screen, RED, triangles, 3)
        screen.set_at(triangles, RED)
    

    if not finished_iteration:
        selected_vertex = NORMALIZED_POINTS[random.randint(0,2)]
        midpoint = [math.floor((current_point[0]+selected_vertex[0])/2),math.floor((current_point[1]+selected_vertex[1])/2)]
        current_point = midpoint
        drawn_points.append(current_point)
        pygame.draw.circle(screen, RED, current_point, 3)
    for point in drawn_points:
        screen.set_at(point,GREEN)
    if show_info == True:
        points_displayed = myfont.render(f'Points: {len(drawn_points)}', False, (255, 255, 255))
        auto_toggle = myfont.render(f'Auto: {auto}', False, (255, 255, 255))
        tickspeed = myfont.render(f'Tick: {tick}     UP↑     DOWN↓', False, (255, 255, 255))
        screen.blit(points_displayed,((WIDTH/2)-50,(HEIGHT/2)+200))
        screen.blit(auto_toggle,((WIDTH/2)-70,(HEIGHT/2)+250))
        screen.blit(resetcommand,((WIDTH/2)-50,(HEIGHT/2)+300))
        screen.blit(autocommand,((WIDTH/2)-50,(HEIGHT/2)+350))
        screen.blit(plotcommand,((WIDTH/2)-70,(HEIGHT/2)+400))
        screen.blit(tickspeed,(0,0))
    pygame.display.flip()
    
    '''if len(drawn_points)>i and not finished_iteration:
        finished_iteration = True
        print("Finished execution")'''

pygame.quit()

