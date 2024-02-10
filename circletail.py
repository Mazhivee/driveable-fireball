import pygame
import sys
import math

pygame.init()

# Schermgrootte en kleuren
screen_size = (400, 400)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Pixelclustergrootte
pixel_size = 16

# Cirkelinstellingen
circle_radius = min(screen_size) // 4  # Deel door 4 om binnen het scherm te blijven

# Staartinstellingen
tail_length = 10  # Maximale lengte van de staart in pixelclusters
tail_width = pixel_size  # Breedte van de staart

# Initialisatie scherm
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pixel Circular Movement with Tail")

# Startpositie in het midden van het scherm
x, y = screen_size[0] // 2, screen_size[1] // 2

angle = 0
angular_speed = 0.009  # Hoeksnelheid (pas dit aan voor de gewenste snelheid)

tail_positions = []

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()

    # Bewaar de vorige positie voordat de nieuwe wordt berekend
    prev_x, prev_y = x, y

    # Bereken de nieuwe positie op de cirkel
    x = int(screen_size[0] // 2 + circle_radius * math.cos(angle))
    y = int(screen_size[1] // 2 + circle_radius * math.sin(angle))

    # Ververs het scherm
    screen.fill(black)

    # Teken de staart in rode kleur zonder extra zwarte ruimte
    for i, (tail_x, tail_y) in enumerate(tail_positions):
        tail_size = tail_width - i * 1.5  # Staart wordt geleidelijk smaller
        pygame.draw.circle(screen, red, (tail_x, tail_y), int(tail_size / 2))

    # Verwijder de overtollige staartposities om binnen de maximale lengte te blijven
    if len(tail_positions) == tail_length:
        tail_positions.pop()

    # Bewaar de huidige positie in de staartpositieslijst
    tail_positions.insert(0, (prev_x, prev_y))

    # Teken het huidige pixelcluster als cirkel
    pygame.draw.circle(screen, white, (x, y), int(pixel_size / 2))

    # Incrementeer de hoek met de hoeksnelheid, rekening houdend met de tijd tussen frames
    angle += angular_speed * clock.get_time()

    pygame.display.flip()
    clock.tick(30)
