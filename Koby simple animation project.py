import pygame

pygame.init()

window_width = 480
window_height = 640
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('CSCI 1301 Simple Animation - Koby Willis')

background_image = pygame.image.load('Desertbackground.jpg')

cat_image = pygame.image.load('Fasticon-Cat-Cat-Brown.256.png')
cat_transform = pygame.transform.scale(cat_image, (150, 150))
cat_rect = pygame.Rect(200, 300, 150, 150)

font = pygame.font.Font(None, 17)
text_surface = font.render('Created by: Koby Willis 11/14/2024', True, (0, 255, 0))
text_rect = text_surface.get_rect(topright = (435, 50))

#rotation of the image in degrees
rotation_angle = -90

red = (255, 0, 0)
white = (255, 255, 255)

velocity = 20
circle_velocity_x = 1
circle_velocity_y = 1
circle_x = 300
circle_y = 0
circle_radius = 30

circle = pygame.draw.circle(window, red, (circle_x, circle_y), circle_radius, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cat_rect.x -= velocity
            if event.key == pygame.K_RIGHT:
                cat_rect.x += velocity
            if event.key == pygame.K_DOWN:
                cat_rect.y += velocity
            if event.key == pygame.K_UP:
                cat_rect.y -= velocity
    
    rotated_image = pygame.transform.rotate(background_image, rotation_angle)

    background_rect = rotated_image.get_rect(center = window.get_rect().center)
    cat_rect.clamp_ip(window.get_rect())

    window.blit(rotated_image, background_rect)
    window.blit(cat_transform, cat_rect)
    window.blit(text_surface, text_rect)

    circle_x += circle_velocity_x
    circle_y += circle_velocity_y
    if circle_x + circle_radius >= window_width:
        circle_x = window_width - circle_radius
        circle_velocity_x *= -1
    elif circle_x - circle_radius <= 0:
        circle_x = circle_radius
        circle_velocity_x *= -1
    
    if circle_y + circle_radius >= window_height:
        circle_y = window_height - circle_radius
        circle_velocity_y *= -1
    elif circle_y - circle_radius <= 0:
        circle_y = circle_radius
        circle_velocity_y *= -1

    circle = pygame.draw.circle(window, red, (circle_x, circle_y), circle_radius, 10)

    pygame.display.update()

pygame.quit()