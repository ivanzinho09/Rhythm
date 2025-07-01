import pygame
import sys

# Game settings
WIDTH, HEIGHT = 640, 480
FPS = 60
BEAT_INTERVAL = 1000  # milliseconds between beats
WINDOW_COLOR = (30, 30, 30)
BEAT_COLOR = (70, 150, 70)
TEXT_COLOR = (220, 220, 220)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rhythm Prototype")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

last_beat_time = pygame.time.get_ticks()
beat_active = False
score = 0
feedback = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            now = pygame.time.get_ticks()
            diff = abs(now - last_beat_time)
            if diff < 200:
                score += 1
                feedback = "Perfect!"
            else:
                feedback = "Miss"

    now = pygame.time.get_ticks()
    if now - last_beat_time >= BEAT_INTERVAL:
        last_beat_time = now
        beat_active = True
    if beat_active and now - last_beat_time > 200:
        beat_active = False

    screen.fill(WINDOW_COLOR)

    if beat_active:
        pygame.draw.circle(screen, BEAT_COLOR, (WIDTH // 2, HEIGHT // 2), 50)

    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    feedback_text = font.render(feedback, True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))
    screen.blit(feedback_text, (10, 60))

    pygame.display.flip()
    clock.tick(FPS)
