import pygame
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Leevin Khärmespeli")

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 20

font_style = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

food_image = pygame.image.load("mörök.png")


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 5, dis_height / 5])


def mrk(x, y):
    dis.blit(food_image, (x, y))


def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - (snake_block + 30)) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - (snake_block + 30)) / 10.0) * 10.0
    while not game_over:

        while game_close:
            dis.fill(white)
            message("Hävisit pelin! C = Uusi peli Q = Quit", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        mrk(foodx, foody)
        snake_head = [x1, y1]
        snake_List.append(snake_head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1+4 == foodx+4 and y1+4 == foody+4:
            foodx = round(random.randrange(0, dis_width - (snake_block + 30)) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - (snake_block + 30)) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
