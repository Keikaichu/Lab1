import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройка экрана
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Класс Змеи
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
    
    def move(self):
        head = self.body[0]
        x = (head[0] + self.direction[0]) % GRID_WIDTH
        y = (head[1] + self.direction[1]) % GRID_HEIGHT
        new_head = (x, y)
        if new_head in self.body[1:] or new_head in walls:
            return False
        self.body.insert(0, new_head)
        if new_head == food.position:
            food.spawn()
        else:
            self.body.pop()
        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

# Класс Еды
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn()

    def spawn(self):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake.body and (x, y) not in walls:
                self.position = (x, y)
                break

# Границы поля
walls = [(0, i) for i in range(GRID_HEIGHT)] + [(GRID_WIDTH - 1, i) for i in range(GRID_HEIGHT)] + \
        [(i, 0) for i in range(GRID_WIDTH)] + [(i, GRID_HEIGHT - 1) for i in range(GRID_WIDTH)]

# Игровые переменные
snake = Snake()
food = Food()
score = 0
level = 1
speed = 10

# Главный игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))

    # Движение змеи
    if not snake.move():
        running = False

    # Отрисовка змеи
    for segment in snake.body:
        pygame.draw.rect(screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Отрисовка еды
    pygame.draw.rect(screen, RED, (food.position[0] * GRID_SIZE, food.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Обработка столкновений
    if snake.body[0] == food.position:
        score += 1
        if score % 3 == 0:  # Увеличение уровня каждые 3 еды
            level += 1
            speed += 1  # Увеличение скорости
        snake.body.append(snake.body[-1])  # Увеличение длины змеи
        food.spawn()

    # Отображение счета и уровня
    font = pygame.font.SysFont(None, 25)
    text = font.render(f"Счет: {score}   Уровень: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

# Выход из Pygame
pygame.quit()
