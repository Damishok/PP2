import pygame as pg

import sys, random




from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP

FPS = 60

TARGET_FPS = 60

WIN_WIDTH = 800

WIN_HEIGHT = 500

WHITE = (255, 255, 255)

ORANGE = (255, 150, 100)

BLACK = (0, 0, 0)

RED = (200, 0, 0)

GREEN = (0, 255, 0)

BLUE = (128, 128, 255)







pg.init()

pg.font.init()




screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

clock = pg.time.Clock()

pg.display.set_caption('hngry lin')




font = pg.font.Font('C:/Users/ktnrg/OneDrive/Документы/Python/pygame/hungry lion/dpcomic.ttf', 30)

player_x = WIN_WIDTH / 2

player_y = 400

player_speed = 3

red_block_list = []

green_block_list = []

cnt = 0

score = 0

is_touched = False




game_over_black = pg.Surface((WIN_WIDTH, WIN_HEIGHT), pg.SRCALPHA)

game_over_black.fill((0, 0, 0, 128))

game_over_surface = font.render('You lost', True, WHITE)

game_over_rect = game_over_surface.get_rect(center = (WIN_WIDTH / 2, WIN_HEIGHT - 200))




for _ in range(50):

    red_block_x = random.randint(0, WIN_WIDTH)

    red_block_y = random.randint(-WIN_HEIGHT / 2, WIN_HEIGHT / 2)

    red_block_rect = pg.Rect((red_block_x, red_block_y, 20, 15))

    red_block_list.append((screen, RED, red_block_rect))

for _ in range(10):

    green_block_x = random.randint(0, WIN_WIDTH)

    green_block_y = random.randint(0, WIN_HEIGHT / 2)

    green_block_rect = pg.Rect((green_block_x, green_block_y, 20, 15))

    green_block_list.append((screen, GREEN, green_block_rect))

while True:

    player_rect = pg.Rect(player_x, player_y, 15, 15)

    keys_pressed = pg.key.get_pressed()

    screen.fill(WHITE)

    for event in pg.event.get():

        if event.type == pg.QUIT:

            pg.quit()

            sys.exit()

    if keys_pressed[pg.K_UP]:

        player_y -= player_speed

    if keys_pressed[pg.K_DOWN]:

        player_y += player_speed

    if keys_pressed[pg.K_LEFT]:

        player_x -= player_speed

    if keys_pressed[pg.K_RIGHT]:

        player_x += player_speed

    for i in red_block_list:

        pg.draw.rect(i[0], i[1], i[2])

        i[2][1] += 1

        if i[2][1] > WIN_HEIGHT:

            i[2][1] = -20

            i[2][0] = random.randint(0, WIN_WIDTH)

        if player_rect.colliderect(i[2]):

            i[2][1] = 10000

            i[2][0] = 10000

            score -= 1

    for i in green_block_list:

        pg.draw.rect(i[0], i[1], i[2])

        if player_rect.colliderect(i[2]):

            score += 1

            i[2][1] = 10000

            i[2][0] = 10000

        else:

            i[2][1] += random.randint(-2, 2)

            i[2][0] += random.randint(-2, 2)

        # if cnt % 10 == 0 and cnt != 0:

        #     i[2][1] = random.randint(0, WIN_WIDTH)

        #     i[2][0] = random.randint(0, WIN_HEIGHT)

        #     cnt = 0

    if player_x < 0:

        player_x += player_speed

    if player_x > WIN_WIDTH - 15:

        player_x -= player_speed

    if player_y < 0:

        player_y += player_speed

    if player_y > WIN_HEIGHT - 15:

        player_y -= player_speed

    score_text = f'Score: {score}'

    score_surface = font.render(score_text, True, BLACK)

    score_rect = score_surface.get_rect(center = (50, 20))

    screen.blit(score_surface, score_rect)

    pg.draw.rect(screen, BLUE, player_rect)

    pg.display.update()

    clock.tick(FPS)