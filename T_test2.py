import pygame
from pygame.locals import *
import sys
import copy
import DD

p_size = 20
p_position_1 = [[0, - p_size], [0, 0],[0, p_size],[0, p_size*2]]
p_position_2 = [[0, - p_size*2], [0, -p_size],[0, 0],[p_size, 0]]
T_field_w = 10
T_field_h = 20
TETRIS = []



red = (200, 0, 0)
blue = (0, 0, 200)

#def draw_rect(s, x, y, c,):
#    pygame.draw.rect(s, c, Rect(x - (p_size/2), y - (p_size/2), p_size, p_size), 5)

def draw_piece(s, x, y, r, p_position, c):
    global p_size
    ppp = rot90(p_position, r)
    for i in range(len(ppp)):
        DD.draw_rect(s, x + ppp[i][0], y + ppp[i][1], c,p_size)


def rot90(p, r):
    p_out = copy.deepcopy(p)
    for j in range(r):
        for i in range(len(p_out)):
            p_out[i][0], p_out[i][1] = - p_out[i][1], p_out[i][0]
#    print("r={} p={} p_out={}position={}".format(r, p, p_out,p_position_2))
    return p_out

def put_piece(s, n, i, j, r):
    global p_size, p_position_1, p_position_2
    x = p_size*i + p_size/2
    y = p_size*j + p_size/2
    if n == 1:
        draw_piece(s, x, y, r, p_position_1, red)
    elif n == 2:
        draw_piece(s, x, y, r, p_position_2, blue)

def T_new():
    global TETRIS
    TETRIS = []
    for x in range(0, T_field_w + 2):
        row =[]
        if 0 < x < T_field_w +1:
            for y in range(0, T_field_h + 2):
                if y == T_field_h + 1:
                    row.append(8)
                else:
                    row.append(0)
        else:
            for y in range(0, T_field_h + 2):
                row.append(8)
        TETRIS.append(row)


def get_current_position(current_p_i, current_p_j, p_position, r):
    c_position =  rot90(p_position,r)
    POINTS = []
    for x in range(len(c_position)):
        row =[current_p_i + c_position[x][0], current_p_j + c_position[x][1]]
        POINTS.append(row)
    return POINTS



def main():
    global p_size
    pygame.init()
    screen = pygame.display.set_mode((p_size*10, p_size*20))
    pygame.display.set_caption("test")

    pygame.time.set_timer(pygame.USEREVENT, 1000)
    rrr = 0
    p_i = 0
    p_j = 0
    while (1):
        screen.fill((0, 0, 0))
        put_piece(screen, 2, p_i, p_j, rrr)



        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_LEFT:
                    p_i = (p_i - 1)%10
                elif event.key == K_RIGHT:
                    p_i = (p_i + 1)%10
                elif event.key == K_UP:
                    rrr = (rrr + 1)%4
                    print("K_UP{}".format(rrr))
            elif event.type == pygame.USEREVENT:
                p_j = (p_j+ 1)%20
                

if __name__ == "__main__":
    main()