import pygame as py
from pygame.constants import MOUSEBUTTONDOWN
 
py.init()
 
width, height = 600, 600
background_colour = (200, 225, 225)
py.display.set_caption('Tic-Tac-Toe')
win = py.display.set_mode((width, height))
win.fill(background_colour)
font = py.font.Font('freesansbold.ttf', 32)
py.display.flip()

rect_colour = (255,255,255)
x = 13
y = 13
boxes = [
py.draw.rect(win, rect_colour, (13,13, 176, 176)),
py.draw.rect(win, rect_colour, (213,13, 176, 176)),
py.draw.rect(win, rect_colour, (413,13, 176, 176)),
py.draw.rect(win, rect_colour, (13,213, 176, 176)),
py.draw.rect(win, rect_colour, (213,213, 176, 176)),
py.draw.rect(win, rect_colour, (413,213, 176, 176)),
py.draw.rect(win, rect_colour, (13,413, 176, 176)),
py.draw.rect(win, rect_colour, (213,413, 176, 176)),
py.draw.rect(win, rect_colour, (413,413, 176, 176))
]
boxes_index = [[0,1,2],[3,4,5],[6,7,8]]

text_colour = (0,0,0)
green = (0,255,0)
red = (255,0,0)
colour = [green,red,green,red,green,red,green,red,green]
colour_index = -1
 
x_and_o = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8}
 
def winner(colour):
    # win.fill(background_colour)
    text = font.render('You Win!', True, text_colour)
    # text = font.render('You Win! Press R to Restart', True, colour)
    textRect = text.get_rect()
    textRect.center = (width // 2, height // 2)
    win.blit(text, textRect)
    if py.K_r:
        py.init()

py.display.flip()
 
running = True
while running:
 
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
 
        if event.type == py.MOUSEBUTTONUP:
            pos = py.mouse.get_pos()
            colour_index += 1
            for box in boxes:
                if box.collidepoint(pos) == True:
                    def positions(boxes_index, v):
                        for i, a in enumerate(boxes_index):
                            if v in a:
                                return (i, a.index(v))
 
                    n,m = (positions(boxes_index, boxes.index(box)))
                    x = 13+(200*m)
                    y = 13+(200*n)
                    py.draw.rect(win, colour[colour_index], (x,y, 176, 176))
                    x_and_o[boxes.index(box)] = colour[colour_index]
                    print(x_and_o, colour_index)
 
                    if x_and_o[0] == x_and_o[1] == x_and_o[2]:
                        winner(x_and_o[0])
                    elif x_and_o[3] == x_and_o[4] == x_and_o[5]:
                        winner(x_and_o[3])
                        running = False
                    elif x_and_o[6] == x_and_o[7] == x_and_o[8]:
                        winner(x_and_o[6])
                        running = False
                    elif x_and_o[0] == x_and_o[3] == x_and_o[6]:
                        winner(x_and_o[0])
                        running = False
                    elif x_and_o[1] == x_and_o[4] == x_and_o[7]:
                        winner(x_and_o[1])
                        running = False
                    elif x_and_o[2] == x_and_o[5] == x_and_o[8]:
                        winner(x_and_o[2])
                        running = False
                    elif x_and_o[0] == x_and_o[4] == x_and_o[8]:
                        winner(x_and_o[0])
                        running = False
                    elif x_and_o[2] == x_and_o[4] == x_and_o[6]:
                        winner(x_and_o[2])
                        running = False
       
        if event.type == py.KEYDOWN:
            print("Clicked")
            x_and_o = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8}
            colour_index = -1
            print(x_and_o, colour_index)
                        # running = False
        py.display.update()
 
py.quit()

