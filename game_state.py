import pygame
import pygame.sprite

from pygame import Rect
from random import randint
from random import randrange
from state import State
from snake_segment import SnakeSegment

class GameState(State):


    def __init__(self, main):  
        super().__init__()         
        self.app = main
        self.boundary = Rect(0, 0, self.app.width, self.app.height)

        self.dirX = 0
        self.dirY = 0
        self.tileWidth = 50
        self.food = Rect( (randint(round(self.app.width * 0.05), round(self.app.width * 0.95)), randint(round(self.app.height * 0.05), round(self.app.height * 0.95)), self.tileWidth, self.tileWidth))

        self.snakeLength = 1
        self.snakeSegments = []
        self.snakeSegments.append( SnakeSegment(100, 100, self.tileWidth, self._generate_color()) )
        self.snakeHead = self.snakeSegments[0]
        self.snakeSprites = pygame.sprite.Group()
        self.speed = 5


        print(self.food)
        print(self.snakeHead.rect)

        return


    def update(self):
        super().update()
        for snake in self.snakeSegments:
            snake.rect.x += self.dirX
            snake.rect.y += self.dirY

        if(self.food.colliderect(self.snakeHead.rect)):
            x = self.food.x
            while(x == self.food.x):
                x = randint( round(self.app.width * 0.05), round(self.app.width * 0.95) )
                
            y = self.food.y
            while(y == self.food.y):
                y = randint( round(self.app.height * 0.05), round(self.app.height * 0.95) )
        
            self.food = Rect(x, y, self.tileWidth, self.tileWidth)
            self.snakeLength += 1
            self.snakeSegments.append( SnakeSegment(self.snakeHead.rect.x, self.snakeHead.rect.y, self.tileWidth, self._generate_color()) )

        return


    def render(self):
        super().render()
        pygame.draw.rect(self.app.screen, (0,127,0), self.food)

        for snake in self.snakeSegments:
            pygame.draw.rect(self.app.screen, snake.color, snake.rect)

        return


    def key_down(self, key):
        super().key_down(key)
        if(key == pygame.K_w or key == pygame.K_UP):
            self.dirY = -self.speed
            self.dirX = 0

        elif(key == pygame.K_a or key == pygame.K_LEFT):
            self.dirX = -self.speed
            self.dirY = 0

        elif(key == pygame.K_s or key == pygame.K_DOWN):
            self.dirY = +self.speed
            self.dirX = 0

        elif(key == pygame.K_d or key == pygame.K_RIGHT):  
            self.dirX = +self.speed
            self.dirY = 0

        elif(key == pygame.K_ESCAPE):
            self.app.running = False

        else:
            return 


    def _generate_color(self):
        return pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))
