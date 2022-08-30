import pygame

SIZE_BLOCK = 20

BLUE = (204, 255, 255)

FRAME_COLOR = (0, 255, 204)

HEADER_MARGIN = 70

WHITE = (255, 255, 255)

MARGIN = 1

COUNT_BLOCKS = 20

size = [SIZE_BLOCK*COUNT_BLOCKS+2*SIZE_BLOCK+MARGIN*COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS + HEADER_MARGIN]

print(size)

screen = pygame.display.set_mode(size)

pygame.display.set_caption('Змейка')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_MARGIN, [0,0,size[0], HEADER_MARGIN])

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column+1),
                                             HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row+1),
                                             SIZE_BLOCK,
                                             SIZE_BLOCK])
    pygame.display.flip()