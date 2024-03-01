# import library
import pygame
import random
from pygame.locals import *

# initialize the game
pygame.init()
width, height = 1264, 632

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harry Potter's Battle")
a = 0
b = 0
z = 0
mark = 0
pause = False
running = True
clock = pygame.time.Clock()
badtimer = 100
badtimer1 = 0
anto = [[320, 600]]
cast = [[70, 70]]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
font_name = pygame.font.match_font('arial')
# loading images
spell = pygame.image.load("spell2.png")
villain = pygame.image.load("villain1.png")
player = pygame.image.load("hero7.png")
background = pygame.image.load("bg1.png")
# looping through
position_x = 100
position_y = 300
spell_x = position_x + 70
spell_y = position_y


def draw_text(surf, text, size, x, y):
    # selecting a cross-platform font to display the score
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)
    pygame.display.update()


def crashed():
    screen.fill(WHITE)
    draw_text(screen, "Game Over", 40, width / 2, height / 2)
    draw_text(screen, "score" + str(mark), 30, 650, 450)
    clock.tick(0.1)
    pygame.quit()


end_it = False
while not end_it:
    screen.fill(BLACK)
    myfont1 = pygame.font.Font(font_name, 40)
    myfont2 = pygame.font.Font(font_name, 20)
    nlabel = myfont1.render("HARRY POTTER's BATTLE ", 1, (255, 255, 255))
    olabel1 = myfont2.render("CONTROLS ", 0, (255, 255, 255))
    olabel2 = myfont2.render("Use arrows to move the hero", 0, (255, 255, 255))
    olabel3 = myfont2.render("Do not let the dementors past you", 0, (50, 150, 150))
    olabel4 = myfont2.render("Press SPACE to shoot", 1, (255, 255, 255))
    olabel5 = myfont2.render("press ESC to EXIT", 0, (255, 255, 255))
    olabel6 = myfont2.render("Click anywhere to start", 0, (100, 50, 55))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            end_it = True
    screen.blit(nlabel, (250, 200))
    screen.blit(olabel1, (100, 300))
    screen.blit(olabel2, (100, 350))
    screen.blit(olabel3, (600, 400))
    screen.blit(olabel4, (100, 400))
    screen.blit(olabel5, (100, 450))
    screen.blit(olabel6, (600, 300))
    pygame.display.flip()

while running:
    badtimer -= 1
    screen.blit(background, (0, 0))
    spell_x = position_x + 100
    spell_y = position_y

    screen.blit(spell, (spell_x + z, spell_y))
    screen.blit(player, (position_x, position_y))
    if badtimer == 0:
        v = anto.append([1200, random.randint(0, 500)])
        badtimer = 100 - (badtimer1 * 2)
        if badtimer1 >= 10:
            badtimer1 = 10
        else:
            badtimer1 += 5

    index2 = 0
    for badguy in anto:
        if badguy[0] < 100:
            anto.pop(index2)
            mark -= 2
        badguy[0] -= 7
        badrect = pygame.Rect(villain.get_rect())
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        badrect.bottom = badguy[1] + 210
        badrect.right = badguy[0] + 230
        for i in range(badrect.top, badrect.bottom):
            for j in range(badrect.left, badrect.right):
                if position_x == j and position_y == i:
                    crashed()
                if spell_x == j and spell_y == i:
                    mark += 1
                    anto.pop(index2)
        index2 += 1
        if mark <= -10:
            crashed()
    for badguy in anto:
        screen.blit(villain, badguy)
    draw_text(screen, "Score: " + str(mark + 2), 50, 750, 50)
    #  update the screen
    pygame.display.flip()
    # loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                a = -10
            if event.key == pygame.K_RIGHT:
                a = 10
            if event.key == pygame.K_UP:
                b = -10
            if event.key == pygame.K_DOWN:
                b = 10
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_SPACE:
                z = 500
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                a = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                b = 0
            if event.key == pygame.K_SPACE:
                z = 0

    position_x += a
    position_y += b
    pygame.draw.rect(screen, green, (150, 450, 100, 50))
    pygame.draw.rect(screen, green, (550, 450, 100, 50))
    if position_x <= 0 or position_x > 1200 or position_y < 0 or position_y > 632:
        crashed()
    if position_x == badguy[0] and position_y == badguy[1]:
        crashed()
    screen.fill(WHITE)
pygame.quit()
quit()
