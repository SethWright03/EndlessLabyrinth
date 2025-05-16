import pygame
import random
import Rooms
import Objects
import math

walls = pygame.sprite.Group()
floors = pygame.sprite.Group()
traps = pygame.sprite.Group()
players = pygame.sprite.Group()
enemies = pygame.sprite.Group()

rooms_generated = 0
last_exit = 0

def generate_room():
    global rooms_generated
    global last_exit
    traps_placed = 0
    enemies_placed = 0
    walls.empty()
    floors.empty()
    traps.empty()
    enemies.empty()
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
            if room.traps == True and room.room_tiles[row][column] == 0 and traps_placed <= 4:
                trap_check = random.randint(1,20)
                if trap_check == 1:
                    tile = Objects.Floor_Trap()
                    tile.rect.topleft = (tilepos_x,tilepos_y)
                    tile.position.x = tilepos_x
                    tile.position.y = tilepos_y
                    traps.add(tile)
                    traps_placed += 1
            if room.enemies == True and room.room_tiles[row][column] == 0 and enemies_placed <= 2:
                enemy_check = random.randint(1,20)
                if enemy_check == 1:
                    enemy = Objects.Goblin()
                    enemy.rect.topleft = (tilepos_x,tilepos_y)
                    enemy.position.x = tilepos_x
                    enemy.position.y = tilepos_y
                    enemies.add(enemy)
                    enemies_placed += 1
        column = 0
    rooms_generated += 1
    last_exit = room.exit_type
    return(rooms_generated,last_exit)

def pass_turn():
    for tile in traps:
        tile.turn()
        trap_collisions = pygame.sprite.spritecollide(tile,players,False)
        if trap_collisions and tile.activity_state == True:
            player.damage()
            print('damaged! health remaining: ',player.health)
    for enemy in enemies:
        if enemy.dead == True:
            enemies.remove(enemy)
        else:
            enemy.turn(player_tilepos,walls)
            enemy_collisions = pygame.sprite.spritecollide(enemy,players,False)
            if enemy_collisions:
                result_string = enemy.attack(player)
                add_line(result_string)
                enemy.undo_move()

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS',30)
screen = pygame.display.set_mode((1280,720))

# setting up console display for RPG mechanics
console_font = pygame.font.SysFont('Courier New',15)
line_height = console_font.get_height()
max_lines = screen.get_height() // (2 * line_height)
console_lines = []
console_lines.append('Game started')

def add_line(console_text):
    if len(console_lines) >= max_lines:
        console_lines.pop(0)
    console_lines.append(console_text)

def draw_console():
    console_surface = pygame.Surface((screen.get_width() // 3, screen.get_height() // 2), pygame.SRCALPHA)
    console_surface.fill((0, 0, 0, 16))
    for i, line in enumerate(console_lines):
        text_surface = console_font.render(line, True, (0, 0, 0))
        console_surface.blit(text_surface, (10, i * line_height))
    screen.blit(console_surface, (0, screen.get_height() // 2))

clock = pygame.time.Clock()
running = True
player_tilepos = pygame.Vector2(160,480)
player = Objects.Player()
players.add(player)
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
                enemy_collisions = pygame.sprite.spritecollide(player,enemies,False)
                for enemy in enemy_collisions:
                    if enemy.dead == False:
                        player.attack(enemy)
                        result_string = player.attack(enemy)
                        add_line(result_string)
                        player_tilepos.x -= 80
                        player.rect.topleft = player_tilepos
                pass_turn()
            if event.key == pygame.K_LEFT:
                player_tilepos.x -= 80
                player.rect.topleft = player_tilepos
                wall_collisions = pygame.sprite.spritecollide(player,walls,False)
                if wall_collisions:
                    player_tilepos.x += 80
                    player.rect.topleft = player_tilepos
                for enemy in enemy_collisions:
                    if enemy.dead == False:
                        player.attack(enemy)
                        result_string = player.attack(enemy)
                        add_line(result_string)
                        player_tilepos.x += 80
                        player.rect.topleft = player_tilepos
                pass_turn()
            if event.key == pygame.K_UP:
                player_tilepos.y -= 80
                player.rect.topleft = player_tilepos
                wall_collisions = pygame.sprite.spritecollide(player,walls,False)
                if wall_collisions:
                    player_tilepos.y += 80
                    player.rect.topleft = player_tilepos
                for enemy in enemy_collisions:
                    if enemy.dead == False:
                        player.attack(enemy)
                        result_string = player.attack(enemy)
                        add_line(result_string)
                        player_tilepos.y += 80
                        player.rect.topleft = player_tilepos
                pass_turn() 
            if event.key == pygame.K_DOWN:
                player_tilepos.y += 80
                player.rect.topleft = player_tilepos
                wall_collisions = pygame.sprite.spritecollide(player,walls,False)
                if wall_collisions:
                    player_tilepos.y -= 80
                    player.rect.topleft = player_tilepos
                for enemy in enemy_collisions:
                    if enemy.dead == False:
                        player.attack(enemy)
                        result_string = player.attack(enemy)
                        add_line(result_string)
                        player_tilepos.y -= 80
                        player.rect.topleft = player_tilepos
                pass_turn() 
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
    if pygame.time.get_ticks() - player.damage_time >= player.damage_duration:
        player.image.fill('blue')
    health_counter = font.render(f'Health: {player.health}',True,'red')
    floors.draw(screen)
    walls.draw(screen)
    traps.draw(screen)
    enemies.draw(screen)
    screen.blit(player.image,player.rect.topleft)
    draw_console()
    screen.blit(health_counter,(0,0))
    pygame.display.flip()
    if player.health <= 0:
        running = False
        print('GAME OVER')