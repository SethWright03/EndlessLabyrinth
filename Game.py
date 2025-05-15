import pygame
import random
import Rooms
import Objects

walls = pygame.sprite.Group()
floors = pygame.sprite.Group()
rooms_generated = 0
last_exit = 0

def generate_room():
    global rooms_generated
    global last_exit
    walls.empty()
    floors.empty()
    match last_exit:
        case 1:
            random_number = random.randint(1,4)
            match random_number:
                case 1:
                    room = Rooms.NorthEastHallway()
                case 2:
                    room = Rooms.NorthEastSmallRoom()
                case 3:
                    room = Rooms.NorthNorthHallway()
                case 4:
                    room = Rooms.NorthNorthSmallRoom()
        case 2:
            random_number = random.randint(1,3)
            match random_number:
                case 1:
                    room = Rooms.EastNorthHall()
                case 2:
                    room = Rooms.EastEastCrookedHall()
                case 3:
                    room = Rooms.EastNorthLargeRoom()
        case 0:
            room = Rooms.StarterRoom()
    row = 0
    column = 0
    for row in range(9):
        for column in range(16):
            tilepos_x = (column * 80)
            tilepos_y = (row * 80)
            if room.room_tiles[row][column] == 1:
                tile = Objects.Wall_Tile(tilepos_x,tilepos_y)
                walls.add(tile)
            if room.room_tiles[row][column] == 0:
                tile = Objects.Floor_Tile(tilepos_x,tilepos_y)
                floors.add(tile)
        column = 0
    rooms_generated += 1
    last_exit = room.exit_type
    return(rooms_generated,last_exit)

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

player_tilepos = pygame.Vector2(160,480)
player = Objects.Player()

generate_room()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_tilepos.x += 80
                player.rect.topleft = player_tilepos
                wall_collisions = pygame.sprite.spritecollide(player,walls,False)
                if wall_collisions:
                    player_tilepos.x -= 80
                    player.rect.topleft = player_tilepos
            if event.key == pygame.K_LEFT:
                player_tilepos.x -= 80
                player.rect.topleft = player_tilepos
                wall_collisions = pygame.sprite.spritecollide(player,walls,False)
                if wall_collisions:
                    player_tilepos.x += 80
                    player.rect.topleft = player_tilepos
            if event.key == pygame.K_UP:
                player_tilepos.y -= 80
                player.rect.topleft = player_tilepos
                wall_collisions = pygame.sprite.spritecollide(player,walls,False)
                if wall_collisions:
                    player_tilepos.y += 80
                    player.rect.topleft = player_tilepos
            if event.key == pygame.K_DOWN:
                player_tilepos.y += 80
                player.rect.topleft = player_tilepos
                wall_collisions = pygame.sprite.spritecollide(player,walls,False)
                if wall_collisions:
                    player_tilepos.y -= 80
                    player.rect.topleft = player_tilepos
    if last_exit == 1 and player_tilepos.y <= -1:
        generate_room()
        player_tilepos.y = 640
        player_tilepos.x = 80
    if last_exit == 2 and player_tilepos.x >= 1201:
        generate_room()
        player_tilepos.y = 560
        player_tilepos.x = 0
    player.rect.topleft = player_tilepos
    screen.fill('black')

    # figure out turn pass logic later, worry about room generation for now;
    # movement goes in for event loop until I figure that out

    floors.draw(screen)
    walls.draw(screen)
    screen.blit(player.image,player.rect.topleft)
    pygame.display.flip()