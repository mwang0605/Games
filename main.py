import time
import pyautogui
import pygame, sys
import random
from pygame_widgets import Slider, TextBox, Button
import Constants
from Crosshair_class import Crosshair
from pygame.locals import *
import pygame_gui

bg = pygame.image.load('pygame_background.png')
logo = pygame.image.load('logo_screen.png')
play_bg = pygame.image.load('Spidershot.png')
pygame.init()

font = pygame.font.SysFont(None, 20)
font1 = pygame.font.SysFont(None, 50)
# Assign FPS a value
FPS = 80
FramePerSec = pygame.time.Clock()

# Setting up color objects


screen = pygame.display.set_mode((500, 500))
screen.blit(logo, (0,0))
pygame.display.set_caption("Aim Practice")

slider = Slider(screen, 100, 100, 300, 20, min=0, max=10, step=2, colour=Constants.WHITE, handleColour=Constants.RED)
output = TextBox(screen, 235, 125, 33, 29, fontSize=20)
slider_line_length = Slider(screen, 100, 250, 300, 20, min=0, max=31, step=2, colour=Constants.WHITE,
                            handleColour=Constants.RED)
output_line_length = TextBox(screen, 235, 275, 33, 29, fontSize=20)

hits = 0
misses = 0
state = "menu"
circle = 0

crosshair = Crosshair()

def crosshair_color_change(crosshair_color):
    crosshair.color = crosshair_color
    print("working")

def state_changer():
    global state
    if state == 'settings':
        state = 'menu'
        menu_screen()
        screen.blit(logo, (0, 0))
        menu_screen()
    if state == 'play':
        state = 'end screen'




buttonback = Button(screen, 10, 10, 30, 10, text='BACK',
                    fontSize=10, margin=20,
                    inactiveColour=(225,0,0),
                    pressedColour=Constants.BLACK,
                    onClick=state_changer,
                    )

buttonwhite = Button(screen, 35, 350, 100, 45, text='White',
            fontSize=25, margin=20,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda :crosshair_color_change(Constants.WHITE))

buttonred = Button(screen, 145, 350, 100, 45, text='Red',
            fontSize=25, margin=20,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda :crosshair_color_change(Constants.RED))

buttongreen = Button(screen, 255, 350, 100, 45, text='Green',
            fontSize=25, margin=20,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda :crosshair_color_change(Constants.GREEN))

buttonblack = Button(screen, 365, 350, 100, 45, text='Black',
            fontSize=25, margin=20,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda :crosshair_color_change(Constants.BLACK))

def menu_screen():
    screen.blit(logo, (0, 0))
    play_button = font1.render("P L A Y", True, Constants.RED)
    screen.blit(play_button, (190, 190))
    pygame.draw.rect(screen, Constants.RED, (175, 176, 150, 60), 2)
    settings_button = font1.render("SETTINGS", True, Constants.RED)
    screen.blit(settings_button, (165, 280))
    pygame.draw.rect(screen, Constants.RED, (155, 265, 195, 60), 2)

def settings_screen():
    pass


def spawn_circle():
    global circle
    nothing = ""
    text = font.render("A C C U R A C Y : " + str(nothing) + "0.0%", True, Constants.RED)
    screen.blit(text, (0, 0))
    circle = pygame.draw.circle(screen, Constants.BLUE, [random.randint(20, 480), random.randint(40, 480)], 15)

def accuracy_counter(hit, miss):
    accuracy = 0
    accuracy_def = 0
    if hit == miss:
        pass
    if hit >= 1 and miss >= 1 and miss == hit:
        accuracy_def += 50
    elif hit > miss:
        accuracy_def = hit / (hit + miss) * 100
        accuracy_def = round(accuracy_def, 2)
    elif hit < miss:
        accuracy_def = hit/(hit + miss) * 100
        accuracy_def = round(accuracy_def, 2)
    if accuracy_def > 100:
        accuracy_def = accuracy_def - 100
    if accuracy_def < 0:
        accuracy_def = abs(accuracy_def)
    else:
        pass
    text = font.render("A C C U R A C Y : " + str(accuracy_def) + "%", True, Constants.RED)
    screen.blit(text, (0,0))
    return accuracy_def

def timer():
    global current_time
    end_time = current_time + 5
    time_remaining = end_time - time.time()
    time_remaining = round(time_remaining)
    text = font.render('T I M E   R E M A I N I N G : ' + str(time_remaining), True, Constants.RED)
    screen.blit(text, (175, 0))
    if time_remaining == 0:
        state_changer()




current_time = 0
menu_screen()
while True:
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
        if state == 'menu':
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(5)[0] == True:
                pos = pygame.mouse.get_pos()
                if 175 < pos[0] < 325 and 176 < pos[1] < 236:

                    state = 'play'
                    current_time = time.time()
                    pygame.mouse.set_visible(False)
                    screen.blit(play_bg, (0,0))
                    pygame.draw.rect(screen, Constants.RED, (pos[0], pos[1], 150, 60), 2)
                    spawn_circle()


                if 155 < pos[0] < 350 and 265 < pos[1] < 325:
                    state = 'settings'
                    screen.blit(bg, (0,0))
                    settings_screen()

        elif state == 'settings':
            screen.blit(bg, (0, 0))
            slider.listen(pygame.event.get())
            slider.draw()
            output.setText(slider.getValue()+1)
            output.draw()
            slider_line_length.listen(pygame.event.get())
            slider_line_length.draw()
            output_line_length.setText(slider_line_length.getValue())
            output_line_length.draw()

            pygame.draw.rect(screen, Constants.WHITE, (175, 25, 150, 60), 2)
            crosshair.basic_crosshair(screen, (250, 55))
            crosshair.line_thickness = slider.getValue()+1
            crosshair.line_length = slider_line_length.getValue()/2

            buttonwhite.listen(event)
            buttonwhite.draw()
            buttonred.listen(event)
            buttonred.draw()
            buttonblack.listen(event)
            buttonblack.draw()
            buttongreen.listen(event)
            buttongreen.draw()
            buttonback.listen(event)
            buttonback.draw()


        elif state == 'play':
            pos = pygame.mouse.get_pos()
            screen.blit(play_bg, (0, 0))

            accuracy_def = accuracy_counter(hits, misses)
            circle = pygame.draw.circle(screen, Constants.BLUE, [circle.center[0], circle.center[1]], 15)
            crosshair.basic_crosshair(screen, pos)
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(5)[0] == True:
                pos = pygame.mouse.get_pos()
                pygame.draw.rect(screen, Constants.RED, (pos[0], pos[1], 150, 60), 2)
                x = [circle.center[0] - pos[0], circle.center[1] - pos[1]]
                y = x[0]**2 + x[1]**2
                w = y**.5
                if w <= 15:
                    screen.blit(play_bg, (0,0))
                    circle = pygame.draw.circle(screen, Constants.BLUE, [random.randint(20, 480), random.randint(40, 480)], 15)
                    hits += 1
                if w >= 15:
                    screen.blit(play_bg, (0,0))
                    circle = pygame.draw.circle(screen, Constants.BLUE, [circle.center[0], circle.center[1]], 15)
                    misses += 1
                accuracy_def = accuracy_counter(hits, misses)
                print(accuracy_def)
                print(hits, misses)

    if state == 'play':
        white_rect = pygame.draw.rect(screen, Constants.WHITE, (0, 0, 500, 16))
        timer()
        accuracy_def = accuracy_counter(hits, misses)
    elif state == 'end screen':
        pygame.mouse.set_visible(True)
        screen.blit(logo, (0,0))
        play_button = font1.render("P L A Y", True, Constants.RED)
        screen.blit(play_button, (190, 190))
        pygame.draw.rect(screen, Constants.RED, (175, 176, 150, 60), 2)

        menu_button = font1.render("M E N U", True, Constants.RED)
        screen.blit(menu_button, (187.5, 280))
        pygame.draw.rect(screen, Constants.RED, (175, 265, 150, 60), 2)

        exit_button = font1.render('E  X  I  T', True, Constants.RED)
        screen.blit(exit_button, (187.5, 370))
        pygame.draw.rect(screen, Constants.RED, (175, 355, 150, 60), 2)

        accuracy_text = font.render("A C C U R A C Y : " + str(accuracy_def) + "%", True, Constants.RED)
        screen.blit(accuracy_text, (185,140))

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(5)[0] == True:
            pos = pygame.mouse.get_pos()
            if 175 < pos[0] < 325 and 176 < pos[1] < 236:
                state = 'play'
                current_time = time.time()
                pygame.mouse.set_visible(False)
                screen.blit(play_bg, (0, 0))
                spawn_circle()
            if 175 < pos[0] < 325 and 265 < pos[1] < 325:
                state = 'menu'
                screen.blit(logo, (0,0))
                menu_screen()

            if 175 < pos [0] < 375 and 355 < pos[1] < 415:
                exit()
