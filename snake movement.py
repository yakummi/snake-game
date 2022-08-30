    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col!=0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col!=0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row!=0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row!=0:
                d_row = 0
                d_col = 1

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0,0,size[0], HEADER_MARGIN])

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            draw_block(color, row, column)

    head = snake_blocks[-1]
    if not head.is_inside():
        pygame.quit()
        sys.exit()

    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)

    new_head = SnakeBlock(head.x + d_row, head.y + d_col)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    pygame.display.flip()
    timer.tick(2)