import pygame
import time
import random
import sys

pygame.init()
screen_w = 500
screen_l = 500
screen = pygame.display.set_mode((screen_w, screen_l), pygame.RESIZABLE)
pygame.display.set_caption('Blockz Snake By Tensa Zangetsu')
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)
red = (255, 0, 0)
lime = (39, 213, 7)
white = (255, 255, 255)
pink = (255, 192, 203)
yellow = (255, 255, 0)
black = (0, 0, 0)
font_style = pygame.font.SysFont("bahnschrift", 50)
score_font = pygame.font.SysFont("Helvetica", 50)


snake_block = 10
food_block = 10
snake_speed = 15
x1 = 300
y1 = 300
foodx = round(random.randrange(0, screen_w - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, screen_l - snake_block) / 10.0) * 10.0

x_change = 0
y_change = 0
def bg(image):
    size = pygame.transform.scale(image, (screen_w,screen_l))
    screen.blit(size, (0,0))

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_w/2,screen_l/2])

def gameloop():
    global x1, y1, screen
    x_change = 0
    y_change = 0
    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, screen_w - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_l - snake_block) / 10.0) * 10.0
    run = True
    game_close = False
    fullscreen = False
    clock = pygame.time.Clock()
    
    while run:
        while game_close:
            screen.fill(white)
            message("You Lost! Press Q to Quit or C to play again", pink)
            Your_score(snake_length - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.VIDEORESIZE:
                if not fullscreen:
                    aspect_ratio = screen_w / screen_l
                    screen = pygame.display.set_mode((event.w, int(event.w / aspect_ratio)), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((screen_w, screen_l), pygame.FULLSCREEN)
                    else:
                        aspect_ratio = screen_w / screen_l
                        screen = pygame.display.set_mode((screen_w, int(screen_w / aspect_ratio)), pygame.RESIZABLE)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    x_change = 0
                    y_change = -snake_block
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    x_change = 0
                    y_change = snake_block

        if x1 < 0 or x1 > screen.get_width():
            game_close = True

        if y1 < 0 or y1 > screen.get_height():
            game_close = True
        x1 += x_change
        y1 += y_change
        screen.fill(lime)
        pygame.draw.rect(screen, white, [foodx, foody, food_block, food_block])
        pygame.draw.rect(screen, red, [x1, y1, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        Your_score(snake_length - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_w - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_l - snake_block) / 10.0) * 10.0
            snake_length += 1
        clock.tick(snake_speed)

    pygame.quit()

gameloop()
