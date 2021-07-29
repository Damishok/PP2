import pygame as pg 
import sys 
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

g = Game() 
while True: 
    g.run()