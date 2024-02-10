import pygame
import sys

# Initialisatie
pygame.init()

# Schermgrootte
screen_size = (400, 400)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Stip Cirkelbeweging met Staart")

# Kleuren
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 165, 0)

# Stipgrootte en positie
stip_grootte = 5
stip_positie = [200, 200]

# Staart parameters
staart_lengte = 500
staart_breedte_start = stip_grootte + 2  # Oversized staart aan het begin
staart_breedte_einde = 1

# Cirkelparameters
straal = 150
hoek = 0
omtrek_aanpassing_snelheid = 0.1
snelheid_aanpassing_snelheid = 0.01

# Staartposities
staart_posities = []

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
                straal += 5
            elif event.key == pygame.K_e:
                straal = max(5, straal - 5)
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
            elif event.key == pygame.K_x:
                running = False

    # Bereken nieuwe positie op cirkel
    stip_positie[0] = int(200 + straal * pygame.math.Vector2(1, 0).rotate(hoek)[0])
    stip_positie[1] = int(200 + straal * pygame.math.Vector2(1, 0).rotate(hoek)[1])

    # Bewaar de positie van de staart
    staart_posities.insert(0, list(stip_positie))
    staart_posities = staart_posities[:staart_lengte]

    # Scherm opschonen
    screen.fill(black)

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
    debug_info_straal = f"Straal: {straal}"
    debug_info_hoek = f"Hoek: {hoek:.2f} graden"
    debug_info_grootte = f"Grootte van de stip: {stip_grootte}"
    debug_info_snelheid = f"Snelheid: {omtrek_aanpassing_snelheid:.2f}"
    text_straal = font_debug.render(debug_info_straal, True, white)
    text_hoek = font_debug.render(debug_info_hoek, True, white)
    text_grootte = font_debug.render(debug_info_grootte, True, white)
    text_snelheid = font_debug.render(debug_info_snelheid, True, white)

    screen.blit(text_straal, (10, 10))
    screen.blit(text_hoek, (10, 30))
    screen.blit(text_grootte, (10, 50))
    screen.blit(text_snelheid, (10, 70))

    # Opsomming van besturing weergeven
    opsomming_info = [
        "Besturingsmogelijkheden:",
        "Q: Verhoog de straal van de cirkel",
        "E: Verklein de straal van de cirkel",
        "A: Verklein de grootte van de stip",
        "S: Vergroot de grootte van de stip",
        "W: Verhoog de snelheid van de cirkelbeweging",
        "Z: Verlaag de snelheid van de cirkelbeweging",
        "X: Stop het programma",
        " ",
        "Druk op X om te stoppen"
    ]

    for i, line in enumerate(opsomming_info):
        text_opsomming = font_opsomming.render(line, True, white)
        screen.blit(text_opsomming, (220, 10 + i * 20))

    # Scherm updaten
    pygame.display.flip()

    # Cirkelbeweging parameters bijwerken
    hoek += omtrek_aanpassing_snelheid

# Afsluiten
pygame.quit()
sys.exit()
