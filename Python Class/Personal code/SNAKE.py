import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 25
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Win & UI")

BG_COLOR = (20, 20, 25)
GRID_COLOR = (35, 35, 40)
SNAKE_HEAD = (0, 255, 140)
SNAKE_BODY = (0, 180, 110)
APPLE_RED = (255, 60, 60)
TEXT_COLOR = (0, 0, 0)
RESTART_COLOR = (120, 255, 120)
WIN_BG = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 60
MOVE_DELAY = 100
last_move_time = 0

font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 40, bold=True)
small_font = pygame.font.SysFont("Arial", 20)
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
MAX_APPLES = GRID_WIDTH * GRID_HEIGHT

next_directions = []
LEAWAY_QUEUE_LIMIT = 2
button_font = pygame.font.SysFont("Arial", 30)

snake = []
direction = (CELL_SIZE, 0)
next_direction = (CELL_SIZE, 0)
apples = []
score = 0
alive = True
apple_count = 0
running = True
waiting_screen = False
menu_flag = False

# ====================== Functions ======================

def get_free_positions(snake, apples):
    occupied = set(snake) | set(apples)
    free = [(x, y) for x in range(0, WIDTH, CELL_SIZE) for y in range(0, HEIGHT, CELL_SIZE) if (x, y) not in occupied]
    return free


def spawn_apples(count, snake):
    apples = []
    count = min(count, MAX_APPLES)
    free_positions = get_free_positions(snake, [])
    random.shuffle(free_positions)
    for i in range(min(count, len(free_positions))):
        apples.append(free_positions[i])
    return apples


def spawn_one_apple(snake, apples):
    free = get_free_positions(snake, apples)
    if not free:
        return None
    return random.choice(free)


def reset_game():
    global snake, direction, next_direction, apples, score, alive, next_directions
    snake = [(200, 200), (175, 200), (150, 200)]
    direction = (CELL_SIZE, 0)
    next_direction = direction
    apples = spawn_apples(apple_count, snake)
    score = 0
    alive = True
    next_directions = []


def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))


def draw_snake(snake):
    for segment in snake[1:]:
        x, y = segment
        rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, SNAKE_BODY, rect, border_radius=10)
        pygame.draw.rect(screen, (255, 255, 255), rect, 1, border_radius=10)
    head_x, head_y = snake[0]
    rect = pygame.Rect(head_x, head_y, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, SNAKE_HEAD, rect, border_radius=10)
    pygame.draw.rect(screen, (255, 255, 255), rect, 1, border_radius=10)
    pygame.draw.circle(screen, (0, 0, 0), (head_x + 7, head_y + 7), 4)
    pygame.draw.circle(screen, (0, 0, 0), (head_x + 18, head_y + 7), 4)


def draw_apples(apples):
    for x, y in apples:
        center = (x + CELL_SIZE // 2, y + CELL_SIZE // 2)
        r = CELL_SIZE // 2 - 2
        pygame.draw.circle(screen, APPLE_RED, center, r)


def draw_score():
    text = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(text, (10, 10))


def draw_fps():
    fps = int(clock.get_fps())
    text = small_font.render(f"FPS: {fps}", True, TEXT_COLOR)
    screen.blit(text, (WIDTH - 100, 10))


def button(text, x, y, w, h, color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rect = pygame.Rect(x, y, w, h)
    if rect.collidepoint(mouse):
        pygame.draw.rect(screen, hover_color, rect)
        if click[0] == 1 and action:
            pygame.time.wait(150)  # prevent multiple triggers
            action()
    else:
        pygame.draw.rect(screen, color, rect)
    txt_surf = button_font.render(text, True, (0, 0, 0))
    screen.blit(txt_surf, (x + w//2 - txt_surf.get_width()//2, y + h//2 - txt_surf.get_height()//2))


def exit_screen():
    global waiting_screen
    reset_game()
    waiting_screen = False


def menu_screen():
    global waiting_screen, menu_flag
    menu_flag = True
    waiting_screen = False  # exit any screen loop to return to menu


def game_over_screen():
    global waiting_screen
    waiting_screen = True
    while waiting_screen:
        screen.fill(BG_COLOR)
        text = big_font.render("GAME OVER", True, RESTART_COLOR)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//3))
        button("Restart", WIDTH//2 - 150, HEIGHT//2, 130, 50, (0,255,0), (0,200,0), exit_screen)
        button("Menu", WIDTH//2 + 20, HEIGHT//2, 130, 50, (200,200,0), (180,180,0), menu_screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def win_screen():
    global waiting_screen
    crown_font = pygame.font.SysFont("Arial", 80)
    waiting_screen = True
    while waiting_screen:
        screen.fill(WIN_BG)
        text = big_font.render("YOU WIN!", True, TEXT_COLOR)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//4))
        crown = crown_font.render("👑", True, TEXT_COLOR)
        screen.blit(crown, (WIDTH//2 - crown.get_width()//2, HEIGHT//2 - 40))
        button("Restart", WIDTH//2 - 150, HEIGHT//2 + 100, 130, 50, (0,255,0), (0,200,0), exit_screen)
        button("Menu", WIDTH//2 + 20, HEIGHT//2 + 100, 130, 50, (200,200,0), (180,180,0), menu_screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

# ====================== Apple Selection ======================
input_text = ""
selecting = True
while selecting:
    screen.fill(BG_COLOR)
    title = big_font.render("Choose Apple Count", True, TEXT_COLOR)
    screen.blit(title, (WIDTH // 2 - 180, HEIGHT // 3))
    prompt = font.render(f"Max apples: {MAX_APPLES}", True, TEXT_COLOR)
    screen.blit(prompt, (WIDTH // 2 - 150, HEIGHT // 2 - 40))
    prompt2 = font.render("Enter number:", True, TEXT_COLOR)
    screen.blit(prompt2, (WIDTH // 2 - 100, HEIGHT // 2))
    text_surface = big_font.render(input_text, True, APPLE_RED)
    screen.blit(text_surface, (WIDTH // 2 - 50, HEIGHT // 2 + 50))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and input_text.isdigit():
                apple_count = min(int(input_text), MAX_APPLES)
                selecting = False
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.unicode.isdigit():
                input_text += event.unicode

reset_game()

# ====================== Main Game Loop ======================
while running:
    if menu_flag:
        input_text = ""
        menu_flag = False
        selecting = True
        while selecting:
            screen.fill(BG_COLOR)
            title = big_font.render("Choose Apple Count", True, TEXT_COLOR)
            screen.blit(title, (WIDTH // 2 - 180, HEIGHT // 3))
            prompt = font.render(f"Max apples: {MAX_APPLES}", True, TEXT_COLOR)
            screen.blit(prompt, (WIDTH // 2 - 150, HEIGHT // 2 - 40))
            prompt2 = font.render("Enter number:", True, TEXT_COLOR)
            screen.blit(prompt2, (WIDTH // 2 - 100, HEIGHT // 2))
            text_surface = big_font.render(input_text, True, APPLE_RED)
            screen.blit(text_surface, (WIDTH // 2 - 50, HEIGHT // 2 + 50))
            pygame.display.update()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN and input_text.isdigit():
                        apple_count = min(int(input_text), MAX_APPLES)
                        reset_game()
                        selecting = False
                    elif e.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif e.unicode.isdigit():
                        input_text += e.unicode

    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
            if event.key == pygame.K_m:
                menu_flag = True
            if alive:
                if event.key == pygame.K_UP:
                    next_directions.append((0, -CELL_SIZE))
                elif event.key == pygame.K_DOWN:
                    next_directions.append((0, CELL_SIZE))
                elif event.key == pygame.K_LEFT:
                    next_directions.append((-CELL_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    next_directions.append((CELL_SIZE, 0))
                if len(next_directions) > LEAWAY_QUEUE_LIMIT:
                    next_directions = next_directions[-LEAWAY_QUEUE_LIMIT:]

    if alive and current_time - last_move_time > MOVE_DELAY:
        last_move_time = current_time
        if next_directions:
            nd = next_directions.pop(0)
            if nd[0] != -direction[0] or nd[1] != -direction[1]:
                direction = nd
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            alive = False
        else:
            snake.insert(0, new_head)
            eaten = [a for a in apples if a in snake]
            for a in eaten:
                apples.remove(a)
                new_a = spawn_one_apple(snake, apples)
                if new_a:
                    apples.append(new_a)
            if new_head not in eaten:
                snake.pop()

    if alive and not apples:
        win_screen()

    screen.fill(BG_COLOR)
    draw_grid()
    draw_apples(apples)
    draw_snake(snake)
    draw_score()
    draw_fps()
    if not alive:
        game_over_screen()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()