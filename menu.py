import pygame
import sys
import random
import pygame_menu

pygame.init()

bg_image = pygame.image.load('maxresdefault.jpg')

SIZE_BLOCK = 20

BLUE = (204, 255, 255)

RED = (224, 0, 0)

FRAME_COLOR = (0, 255, 204)

HEADER_MARGIN = 70

HEADER_COLOR = (0,204,153)

SNAKE_COLOR = (0, 102, 0)

WHITE = (255, 255, 255)

MARGIN = 1

COUNT_BLOCKS = 20

size = [SIZE_BLOCK*COUNT_BLOCKS+2*SIZE_BLOCK+MARGIN*COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS + HEADER_MARGIN]

print(size)

screen = pygame.display.set_mode(size)

pygame.display.set_caption('Змейка')

timer = pygame.time.Clock()

courier = pygame.font.SysFont('courier', 36) # шрифт

class SnakeBlock:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0<=self.x<SIZE_BLOCK and 0<=self.y<SIZE_BLOCK

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK,
                                     SIZE_BLOCK])

def start_the_game():
    def get_random_empty_block():
        x = random.randint(0, COUNT_BLOCKS - 1)
        y = random.randint(0, COUNT_BLOCKS - 1)
        empty_block = SnakeBlock(x, y)

        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, COUNT_BLOCKS - 1)
            empty_block.y = random.randint(0, COUNT_BLOCKS - 1)

        return empty_block

    snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
    apple = get_random_empty_block()
    d_row = buf_row = 0
    d_col = buf_col = 1
    total = 0
    speed = 1


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col!=0:
                    buf_row = -1
                    buf_col = 0
                elif event.key == pygame.K_DOWN and d_col!=0:
                    buf_row = 1
                    buf_col = 0
                elif event.key == pygame.K_LEFT and d_row!=0:
                    buf_row = 0
                    buf_col = -1
                elif event.key == pygame.K_RIGHT and d_row!=0:
                    buf_row = 0
                    buf_col = 1

        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, [0,0,size[0], HEADER_MARGIN])
        text_total = courier.render(f"Total: {total}", 0, WHITE)
        text_speed = courier.render(f"Speed: {speed}", 0, WHITE)
        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
        screen.blit(text_speed, (SIZE_BLOCK+230, SIZE_BLOCK))


        for row in range(COUNT_BLOCKS):
            for column in range(COUNT_BLOCKS):
                if (row + column) % 2 == 0:
                    color = BLUE
                else:
                    color = WHITE
                draw_block(color, row, column)

        head = snake_blocks[-1]
        if not head.is_inside():
            # pygame.quit()
            # sys.exit()
            break
        draw_block(RED, apple.x, apple.y)
        for block in snake_blocks:
            draw_block(SNAKE_COLOR, block.x, block.y)

        if apple == head:
            total += 1
            speed = total//5 + 1
            snake_blocks.append(apple)
            apple = get_random_empty_block()

        d_row = buf_row
        d_col = buf_col

        new_head = SnakeBlock(head.x + d_row, head.y + d_col)
        if new_head in snake_blocks:
            # pygame.quit()
            # sys.exit()
            break
        snake_blocks.append(new_head)
        snake_blocks.pop(0)

        pygame.display.flip()
        timer.tick(3+speed)

main_theme = pygame_menu.themes.THEME_DARK.copy()
main_theme.set_background_color_opacity(0.8)


menu = pygame_menu.Menu('Snake', 400, 400,
                       theme=main_theme)

menu.add.text_input('Имя :', default=' Игрок 1')
menu.add.button('Играть', start_the_game)
menu.add.button('Выход', pygame_menu.events.EXIT)

while True:
    screen.blit(bg_image, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()