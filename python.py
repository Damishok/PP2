import pygame as pg 
import sys 
from settings import * 
from sprites.sprites import * 
import os 
import json 
 
 
class Game: 
    def __init__(self): 
        pg.init() 
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
        pg.display.set_caption(TITLE) 
        self.clock = pg.time.Clock() 
        pg.key.set_repeat(500, 100) 
        self.load_data() 
        self.playing = True 
        self.stop = False 
        self.timer = 0 
        self.game_difficulty = "easy" 
 
    def move(self): 
        self.snake.move() 
        self.second_snake.move() 
 
 
    def load_game(self): 
        self.all_sprites = pg.sprite.Group() 
        self.walls = pg.sprite.Group() 
        with open("saves/save.txt", "r") as f: 
            data = json.loads(f.read()) 
            self.game_difficulty = data["game_difficulty"] 
            self.speed = data["speed"] 
            self.stop = True 
            self.score = data["score"] 
            self.snake.body = pg.sprite.Group() 
            for (x, y) in data["snake_1"]: 
                self.snake.head = SnakeTile(self, x, y) 
                self.snake.body.add(self.snake.head) 
                self.snake.x, self.snake.y = x, y 
            self.second_snake.body = pg.sprite.Group() 
            for (x, y) in data["snake_2"]: 
                self.second_snake.head = SnakeTile(self, x, y) 
                self.second_snake.body.add(self.second_snake.head) 
                self.second_snake.x, self.second_snake.y = x, y 
            self.snake.change_dir() 
            self.second_snake.change_dir() 
            for y, tiles in enumerate(self.maps[self.game_difficulty + "_map.txt"]): 
                for x, tile in enumerate(tiles): 
                    if tile == "1": 
                        self.walls.add(Wall(self, x, y)) 
            self.food = Food(self) 
            self.food.x, self.food.y = data["food"] 
 
 
    def save_game(self): 
        game_state = { 
            "score": self.score, 
            "snake_1": [(snake_tile.x, snake_tile.y) for snake_tile in self.snake.body], 
            "snake_2": [(snake_tile.x, snake_tile.y) for snake_tile in self.second_snake.body], 
            "game_difficulty": self.game_difficulty, 
            "speed": self.speed, 
            "food": (self.food.x, self.food.y) 
        } 
        with open("saves/save.txt", "w+") as f: 
            f.write(json.dumps(game_state)) 
        self.snake.change_dir() 
        self.second_snake.change_dir() 
 
    def load_data(self): 
        self.maps = {} 
        for map_name in os.listdir(os.getcwd() + "/tile_maps"): 
            with open(f"tile_maps/{map_name}", "r") as f: 
                self.maps[map_name] = f.readlines() 
        print(self.maps) 
 
    def new(self): 
        self.all_sprites = pg.sprite.Group() 
        self.walls = pg.sprite.Group() 
        for y, tiles in enumerate(self.maps[self.game_difficulty + "_map.txt"]): 
            for x, tile in enumerate(tiles): 
                if tile == "1": 
                    self.walls.add(Wall(self, x, y)) 
                if tile == "S": 
                    self.snake = Snake(self, x, y) 
                if tile == "P": 
                    self.second_snake = Snake(self, x, y) 
        self.food = Food(self) 
 
    def run(self): 
        self.game_difficulty = "easy" 
        self.new() 
        self.speed = EASY_GAME_SPEED 
        self.playing = True 
        self.timer = 0 
        self.score = 0 
        self.stop = False 
 
        while self.playing: 
            if not self.stop: 
                if self.score == MEDIUM_LEVEL_SCORE and self.game_difficulty == "easy": 
                    self.game_difficulty = "medium" 
                    self.speed = MEDIUM_GAME_SPEED 
                    self.new() 
                if self.score == HARD_LEVEL_SCORE and self.game_difficulty == "medium": 
                    self.game_difficulty = "hard" 
                    self.speed = HARD_GAME_SPEED 
                    self.new() 
                self.timer += 1 
                self.timer %= self.speed 
                if self.timer == 0: 
                    self.move() 
                self.dt = self.clock.tick(FPS) / 1000 
            self.events() 
            self.update() 
            self.draw() 
 
 
    def quit(self): 
        pg.quit() 
        sys.exit() 
 
    def update(self): 
        self.all_sprites.update() 
 
    def draw_grid(self): 
        for x in range(0, SCREEN_WIDTH, TILE_SIZE): 
            pg.draw.line(self.screen, BLUE, (x, 0), (x, SCREEN_HEIGHT)) 
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE): 
            pg.draw.line(self.screen, BLUE, (0, y), (SCREEN_WIDTH, y)) 
 
    def draw(self): 
        self.screen.fill(BGCOLOR) 
        self.draw_grid() 
        self.all_sprites.draw(self.screen) 
        pg.display.flip() 
 
    def events(self): 
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                self.save_game() 
                self.quit() 
            if event.type == pg.KEYDOWN: 
                if event.key == pg.K_ESCAPE: 
                    self.save_game() 
                    self.quit() 
                if event.key == pg.K_LEFT: 
                    self.snake.change_dir(dx=-1) 
                if event.key == pg.K_RIGHT: 
                    self.snake.change_dir(dx=1) 
                if event.key == pg.K_UP: 
                    self.snake.change_dir(dy=-1) 
                if event.key == pg.K_DOWN: 
                    self.snake.change_dir(dy=1) 
                if event.key == pg.K_a: 
                    self.second_snake.change_dir(dx=-1) 
                if event.key == pg.K_d: 
                    self.second_snake.change_dir(dx=1) 
                if event.key == pg.K_w: 
                    self.second_snake.change_dir(dy=-1) 
                if event.key == pg.K_s: 
                    self.second_snake.change_dir(dy=1) 
                if event.key == pg.K_1: 
                    self.save_game() 
                if event.key == pg.K_2: 
                    self.load_game() 
 
 
g = Game() 
while True: 
    g.run()
