import pygame
import random
# Initialize pygame
pygame.init()
print("Pygame is working!")
# Set window dimensions
width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Loot and Danger")


current_screen = "loot and danger"

#menu background

#character selection background
character_background = pygame.image.load("createnew.png")
character_background = pygame.transform.scale(character_background, (width, height))

#gameplay tutorial background
tutorial_background = pygame.image.load("createnew.png")
tutorial_background = pygame.transform.scale(tutorial_background, (width, height))

#loot and danger background
loot_background = pygame.image.load("lootanddanger.png")
loot_background = pygame.transform.scale(loot_background, (width, height))

#game background
game_background = pygame.image.load("background.jpg")
game_background = pygame.transform.scale(game_background, (width, height))
font = pygame.font.SysFont("chiller", 36)


life = 100
score = 0

obstacle = pygame.Rect(500, 200, 50, 50)
obstacle_start_time = pygame.time.get_ticks()
obstacle_duration = 3000

player_x = 100
player_y = 100
item_x = 300
item_y = 300
player_speed = 1

item = pygame.Rect(item_x, item_y, 15, 15)
player = pygame.Rect(player_x, player_y, 115, 115)
player_image = pygame.image.load("pirate.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (120, 120))


    #game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#screen change controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if current_screen == "loot and danger":
                    current_screen = "Spooky Pirate Adventure"
    if current_screen == "loot and danger":
        screen.blit(loot_background, (0, 0))

    elif current_screen == "Spooky Pirate Adventure":
        screen.blit(game_background, (0, 0))
# in game key controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed
          # update player rectangle
        player.x = player_x
        player.y = player_y

        # check collision# if player.colliderect(item):
        if player.colliderect(item):
            score += 1
            item.x = random.randint(0, width - item.width)
            item.y = random.randint(0, height - item.height)


    #add obstacles
        current_time = pygame.time.get_ticks()

        if current_time - obstacle_start_time < obstacle_duration:
            pygame.draw.rect(screen, "red", obstacle)

            if player.colliderect(obstacle):
                life -= 10


                obstacle.x = random.randint(0, width - obstacle.width)
                obstacle.y = random.randint(0, height - obstacle.height)

                while player.colliderect(obstacle):
                    obstacle.x = random.randint(0, width - obstacle.width)
                    obstacle.y = random.randint(0, height - obstacle.height)
        else:
            #make a new obstacle
            obstacle.x = random.randint(0, width - obstacle.width)
            obstacle.y = random.randint(0, height - obstacle.height)

            # Start the 5-second timer again
            obstacle_start_time = current_time

        screen.blit(player_image, player)
        pygame.draw.rect(screen, "yellow", item)

        score_text = font.render(f"Treasure: {score}", True, "white")
        life_text = font.render(f"Life: {life}", True, "white")
        screen.blit(score_text, (20, 20))
        screen.blit(life_text, (20, 60))

        # Update Display
    pygame.display.update()




#Quit pygame
pygame.quit()