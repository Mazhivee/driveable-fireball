import pygame
import sys
import math
import random

# Initialisatie
pygame.init()

# Schermgrootte
screen_size = (800, 400)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Stip Ronde 8 Beweging met Staart")

# Kleuren
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 165, 0)

# Stipgrootte en positie
stip_grootte = 5
stip_positie = [400, 200]

# Staart parameters
staart_lengte = 500
staart_breedte_start = stip_grootte + 2  # Oversized staart aan het begin
staart_breedte_einde = 1

# Cirkelparameters
amplitude = 150
frequentie_x = 0.05  # Aangepaste frequentie voor horizontale beweging
frequentie_y = 0.02
hoek = 0
omtrek_aanpassing_snelheid = 0.1
snelheid_aanpassing_snelheid = 0.01
frequentie_aanpassing_snelheid = 0.0005

# Staartposities
staart_posities = []

# Sterretjes
num_sterretjes = 3
sterretjes = []

for _ in range(num_sterretjes):
    ster_grootte = random.randint(2, 5)
    ster_verdwijn_timer = 0  # Initialize disappearance timer to 0

    sterretjes.append([ster_grootte, ster_verdwijn_timer])

# Debug-informatie font
font_debug = pygame.font.Font(None, 24)
font_opsomming = pygame.font.Font(None, 12)

# Hoofdloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                amplitude += 10
            elif event.key == pygame.K_e:
                amplitude = max(10, amplitude - 10)
            elif event.key == pygame.K_a:
                stip_grootte = max(1, stip_grootte - 1)
                staart_breedte_start = stip_grootte + 2
            elif event.key == pygame.K_s:
                stip_grootte += 1
                staart_breedte_start = stip_grootte + 2
            elif event.key == pygame.K_w:
                omtrek_aanpassing_snelheid += snelheid_aanpassing_snelheid
            elif event.key == pygame.K_z:
                omtrek_aanpassing_snelheid = max(0, omtrek_aanpassing_snelheid - snelheid_aanpassing_snelheid)
            elif event.key == pygame.K_r:
                staart_lengte = max(1, staart_lengte - 10)
            elif event.key == pygame.K_t:
                staart_lengte += 10
            elif event.key == pygame.K_f:
                frequentie_x += frequentie_aanpassing_snelheid
            elif event.key == pygame.K_g:
                frequentie_x = max(0, frequentie_x - frequentie_aanpassing_snelheid)
            elif event.key == pygame.K_v:
                frequentie_y += frequentie_aanpassing_snelheid
            elif event.key == pygame.K_b:
                frequentie_y = max(0, frequentie_y - frequentie_aanpassing_snelheid)
            elif event.key == pygame.K_x:
                running = False

    # Bereken nieuwe positie op ronde 8
    stip_positie[0] = int(400 + amplitude * pygame.math.Vector2(math.sin(frequentie_x * hoek), math.sin(frequentie_y * hoek))[0])
    stip_positie[1] = int(200 + amplitude * pygame.math.Vector2(math.sin(frequentie_x * hoek), math.sin(2 * frequentie_y * hoek))[1])

    # Bewaar de positie van de staart
    staart_posities.insert(0, list(stip_positie))
    staart_posities = staart_posities[:staart_lengte]

    # Scherm opschonen
    screen.fill(black)

    # Sterretjes bijwerken
    for ster in sterretjes:
        pygame.draw.circle(screen, white, (int(ster[1][0]), int(ster[1][1])), ster[0])

    # Staart bijwerken
    for i, pos in enumerate(staart_posities):
        staart_breedte = int(staart_breedte_start - (i / staart_lengte) * (staart_breedte_start - staart_breedte_einde))
        # Bereken gradient kleur
        gradient_color = (
            int(red[0] - (i / staart_lengte) * (red[0] - orange[0])),
            int(red[1] - (i / staart_lengte) * (red[1] - orange[1])),
            int(red[2] - (i / staart_lengte) * (red[2] - orange[2]))
        )
        pygame.draw.circle(screen, gradient_color, pos, staart_breedte)

    # Stip weergeven
    pygame.draw.circle(screen, red, stip_positie, stip_grootte)

    # Debug-informatie weergeven
    debug_info_amplitude = f"Amplitude: {amplitude}"
    debug_info_hoek = f"Hoek: {hoek:.2f} graden"
    debug_info_grootte = f"Grootte van de stip: {stip_grootte}"
    debug_info_snelheid = f"Snelheid: {omtrek_aanpassing_snelheid:.2f}"
    debug_info_staart_lengte = f"Staartlengte: {staart_lengte}"
    debug_info_frequentie_x = f"Frequentie X: {frequentie_x}"
    debug_info_frequentie_y = f"Frequentie Y: {frequentie_y}"
    text_amplitude = font_debug.render(debug_info_amplitude, True, white)
    text_hoek = font_debug.render(debug_info_hoek, True, white)
    text_grootte = font_debug.render(debug_info_grootte, True, white)
    text_snelheid = font_debug.render(debug_info_snelheid, True, white)
    text_staart_lengte = font_debug.render(debug_info_staart_lengte, True, white)
    text_frequentie_x = font_debug.render(debug_info_frequentie_x, True, white)
    text_frequentie_y = font_debug.render(debug_info_frequentie_y, True, white)

    screen.blit(text_amplitude, (10, 10))
    screen.blit(text_hoek, (10, 30))
    screen.blit(text_grootte, (10, 50))
    screen.blit(text_snelheid, (10, 70))
    screen.blit(text_staart_lengte, (10, 90))
    screen.blit(text_frequentie_x, (10, 110))
    screen.blit(text_frequentie_y, (10, 130))

    # Opsomming van besturing weergeven
    opsomming_info = [
        "Besturingsmogelijkheden:",
        "Q: Verhoog de amplitude van de liggende 8 beweging",
        "E: Verlaag de amplitude van de liggende 8 beweging",
        "A: Verklein de grootte van de stip",
        "S: Vergroot de grootte van de stip",
        "W: Verhoog de snelheid van de liggende 8 beweging",
        "Z: Verlaag de snelheid van de liggende 8 beweging",
        "R: Verkort de staartlengte",
        "T: Verleng de staartlengte",
        "F: Verhoog de frequentie X",
        "G: Verlaag de frequentie X",
        "V: Verhoog de frequentie Y",
        "B: Verlaag de frequentie Y",
        "X: Stop het programma",
        " ",
        "Druk op X om te stoppen"
    ]

    for i, line in enumerate(opsomming_info):
        text_opsomming = font_opsomming.render(line, True, white)
        screen.blit(text_opsomming, (screen_size[0] - 50 - text_opsomming.get_width(), 10 + i * 20))

    # Scherm updaten
    pygame.display.flip()

    # Sterretjes bijwerken
    for ster in sterretjes:
        if ster[1][0] > 0 and ster[1][1] > 0:
            ster[1][0] -= 1  # Move stars towards the tail
            ster[1][1] -= 1
        else:
            # Reset star position and disappearance timer if star is outside the screen
            ster[1][0] = random.randint(int(stip_positie[0] - staart_breedte_start), int(stip_positie[0] + staart_breedte_start))
            ster[1][1] = random.randint(int(stip_positie[1] - staart_breedte_start), int(stip_positie[1] + staart_breedte_start))
            ster[0] = random.randint(2, 5)

# Afsluiten
pygame.quit()
sys.exit()
