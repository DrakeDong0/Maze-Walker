import pgzrun
import time
import random



#NOTES:
#ADD GUARDS
WIDTH = 1000
HEIGHT = 1500

#background actors
background = Actor('background')
background2 = Actor('background2')
start_screen = Actor('start_screen')
death_screen = Actor('death')
start_screen.y = 350

#game states
fog = False
fog_status = "ӨFF"
walls = []
game = 1
total_score = 0
volume_num = 135
timer = 0
alarmed = False

#actors for all other images
wall = Actor('wall')
coin = Actor('coin')
portal = Actor('portal')
player = Actor('player_down')
guard1 = Actor('guard_down')
guard2 = Actor('guard_up')
guard3 = Actor('guard_right')
guard4 = Actor('guard_left')
guard5 = Actor('guard_right')
guard6 = Actor('guard_left')
guard7 = Actor('guard_down')
air = Actor('air')
pressure_plate1 = Actor('pressure_plate1')
iron_door_open = Actor('iron_door_open')
iron_door_closed = Actor('iron_door_closed')
wooden_door_open = Actor('wooden_door_open')
wooden_door_closed = Actor('wooden_door_closed')
alarm = Actor('alarm')
map = Actor('map')
map1 = Actor('map1')
map2 = Actor('map2')
map3 = Actor('map3')
map4 = Actor('map4')

#sets custom colors
sky_blue = "#33CCFF"
dark_green = "#005618"
stone_gray = "#7c8279"

#players initial spawn location
player.x = 85
player.y = 185

alarmed = False
#guard spawn locations
guard1.x = 370
guard1.y = 275
guard2.x = 440
guard2.y = 401
guard3.x = 330
guard3.y = 367
guard4.x = 410
guard4.y = 297

guard5.x = 537
guard5.y = 472
guard6.x = 375
guard6.y = 220

guard7.x = 590
guard7.y = 420
#guard walking directions
directg1 = 1
directg2 = 1
directg3 = 1
directg4 = 1
directg5 = 1
directg6 = 1
directg7 = 1
xy = 1500

alarm.x = 0
alarm.y = 0
guards = [guard1, guard2, guard3, guard4, guard5, guard6, guard7]
# 10 billion shapes
message_box = Rect(10, 10, 100, 60)
retry = Rect (310, 550, 200, 50)
retry_bg = Rect(305,545, 210, 60)
black_rect = Rect(0,0,770, 150)
start_box = Rect(250, 120, 300, 150)
end_box = Rect(30, 300, 200, 100)
end_timer_box = Rect(500, 300, 300, 150)
faq = Rect(590,360, 175, 50)
faq_background = Rect(585,355, 185, 60)
begin = Rect(300, 450, 200, 50)
start_bg = Rect(295, 445, 210, 60)
music_box = Rect(40, 360, 200,50 )
music_box_bg = Rect(35, 355, 210, 60)
middle = Rect(150, 100,500,600)
menu = Rect(310, 500, 200, 50)
menu2 = Rect(310,395, 200, 50)
menu_bg = Rect(305,295, 210, 60)
menu2_bg = Rect(305,495, 210, 60)
timer_box = Rect(150, 10, 60, 60)
volume_box = Rect(40, 450, 200, 10)
volume_box2 = Rect(volume_num, 435, 15, 40) #variable because volume is adjustable
volume_hitbox = Rect(40, 435,200,40)
fog_box = Rect(590, 435, 175, 40)
fog_box_bg = Rect(585, 430, 185, 50)
#map location when player hits map icon
map.x = 400
map.y = 400
map_status = False


#sets background music
background_music = True
custom_volume = 0.5
music.set_volume(custom_volume)
if background_music == True:
  music.play_once('bg_music')

#sets more variables
music_status = "ON"
score = 0
game_clock = 0
door1 = False
door2 = False

#Levels! Each letter in the arrays stands for a different type of object (E = portal, M = map, G for gold)
level1 = [
"WWWWWWWWWWWWWWWWWWWW",
"W    M    W        W",
"W         WWWWWW   W",
"W   WWWW       W   W",
"W   W        WWWWW W",
"W WWW  WWWW        W",
"W   W     W W      W",
"W   W     W   WWW WW",
"W   WWW WWW   W W  W",
"W     W   W   W W  W",
"WWW   W   WWWWW W  W",
"W W      WW        W",
"W W   WWWW   WWW   W",
"W     W E      W   W",
"WWWWWWWWWWWWWWWWWWWW",
]

level2 = [
"WWWWWWWWWWWWWWWWWWWW",
"W   GW            EW",
"W WWWWDW  WWWWWWWWWW",
"W   W  W     D  WG W",
"W      WWWWWWWW WW W",
"W WWWWWW   MW    W W",
"W           WMW    W",
"WWWW   WWWW WWWWWW W",
"W       WG         W",
"W  WWW  W W    W   W",
"W             WWWWWW",
"W   W  W    W  WG  W",
"WWWWW  WWWWWW  WW  W",
"WP      W          W",
"WWWWWWWWWWWWWWWWWWWW",
]
level3 = [
"WWWWWWWWWWWWWWWWWWWW",
"W                  W",
"WWGWWWWWWW WWWWW WWW",
"W  W       K   W   W",
"WGWW WWWWWWW   K WGW",
"W  W WE      WWWWWDW",
"WWPWDWWWWWWWWWG    W",
"W  WQ        WWWWW W",
"WGWWWWWWWWW  W   W W",
"W  W               W",
"WWGW  WWWWWWWW  W  W",
"W  W   G  WM    W  W",
"WGWWWWWWWWWWWWWWWW W",
"W                  W",
"WWWWWWWWWWWWWWWWWWWW",
]
level4 = [
"WWWWWWWWWWWWWWWWWWWW",
"WG    WQ       W   W",
"W         WWWW W WWW",
"WWWPWWWWW   W  W   W",
"W   W       W      W",
"W WWW WWWWWWWWWWW  W",
"W   W WGGW  MW     W",
"WWWDW WGG  W W   WWW",
"W   W WWWWWW WWW   W",
"W WWW        WG    W",
"W   WWWWWWWWWWWWWWKW",
"W                  W",
"WWWWWWWWWWWWWWWWWWDW",
"WE        G        W",
"WWWWWWWWWWWWWWWWWWWW",
]
level5 = [
"WWWWWWWWWWWWWWWWWWWW",
"W   W QW  E  W    GW",
"W W W WWWWKWWW WWWWW",
"W W    WG   GW     W",
"WDWWWWWW     WWWWWDW",
"W         P        W",
"WDWWWWWW     WWWWWDW",
"W  G   WG   GW  MW W",
"WWWWWW WWW WWW WWW W",
"WG W     W W    GW W",
"WW WW WW W W WWWWW W",
"W      WGW W       W",
"WWWWWWWWWW WWWWWWWWW",
"W     G   G   G    W",
"WWWWWWWWWWWWWWWWWWWW",
]
#sets which level the game starts at
level = level1
level_num = 1
#enters username, returns invalid if user inputs funny characters
user = str(input("Enter your username: "))
if user.isascii() == False:
  print("Invalid username. Your username is now joe")
  user = "joe"
#timer
def start_clock():
  global timer
  timer += 0.015
  return

def alarmed(p):
  global xy, alarm
  alarm.x = p.x
  alarm.y = p.y-30
  alarm.draw()
  if xy > 0:
    xy -= 1

#clickable buttons on the mouse
def on_mouse_down(pos, button):
  global game, music_color, music_status, background_music, custom_volume, fog, fog_status, map, level_num, door1, door2, score,xy
  #button only works if they're on the correct screen
  if game == 1:
    if button == mouse.LEFT and begin.collidepoint(pos): 
      game = 2 #starts game
    elif button == mouse.LEFT and volume_hitbox.collidepoint(pos): #volume bar
      x = pos[0]
      volume_box2.x = x
      custom_volume = x/200
      music.set_volume(custom_volume)
      
    elif button == mouse.LEFT and music_box.collidepoint(pos):
      if background_music: #turns music on/off
        background_music = False
        music.fadeout(0.5)
        music_color = "red"
        music_status = "ӨFF"
      elif background_music == False:
        background_music = True
        music.play_once('bg_music')
        music_status = "ӨП"
    #different info pages
    elif button == mouse.LEFT and faq.collidepoint(pos):
      game = 0
    elif button == mouse.LEFT and fog_box.collidepoint(pos): #fog setting, turns fog on/off by setting it True/False
      if fog:
        fog = False
        fog_status = "ӨFF"
      elif fog == False:
        fog = True
        fog_status= "ӨП" 
  #return to menu page
  elif game == 0:
    if button == mouse.LEFT and menu.collidepoint(pos):
      game = 1 
  #retry button if player dies
  elif game == 4:
    if button == mouse.LEFT and retry.collidepoint(pos):
      #resets level
      screen.clear()
      level = level1
      level_num = 1
      player.x = 130
      player.y = 180
      walls.clear()
      door1 = False
      door2 = False
      score = 0
      build_walls(level)
      game = 1
      xy = 1500
            
#every function that adds icons/walls to the map  
def add_wall(x,y):
  global walls
  wall = Actor('wall')
  wall.x = x
  wall.y = y
  walls.append(wall)
def add_portal(x,y):
  global portal, walls
  portal = Actor('portal')
  portal.x = x
  portal.y = y
  walls.append(portal)
def add_coin(x,y):
  global walls
  coin = Actor('coin')
  coin.x = x
  coin.y = y
  walls.append(coin)
def add_door(x,y):
  global walls
  door = Actor('iron_door_closed')
  door.x = x 
  door.y = y
  walls.append(door)
def add_pressure_plate(x,y):
  global walls
  pressure_plate = Actor("pressure_plate1")
  pressure_plate.x = x
  pressure_plate.y = y
  walls.append(pressure_plate)
def add_single_door(x,y):
  global walls
  wood_door = Actor('wooden_door_closed')
  wood_door.x = x 
  wood_door.y = y
  walls.append(wood_door)
def add_stone_pressure_plate(x,y):
  global walls
  stone_pressure_plate = Actor('stone_pressure_plate')
  stone_pressure_plate.x = x
  stone_pressure_plate.y = y
  walls.append(stone_pressure_plate)
def add_map(x,y):
  global walls
  map = Actor('map')
  map.x = x
  map.y = y
  walls.append(map)
  
  
#player moveement function
def move(player, dx, dy):
  if dx != 0:
    move_single_axis(player, dx, 0)
  if dy != 0:
   move_single_axis(player, 0, dy)
#1D player movement to ensure wall collision works    
def move_single_axis(player, dx, dy):
  global level, level1, level2, walls, score, door1, door2, level_num, game, total_score, map_status, map, map_status
  player.x += dx
  player.y += dy
  for m in walls:
    if player.colliderect(m): # checks if player collides with a thing, subsequent if statement checks what type of object it is and respondes accordingly
      if (m.image == 'air'):
        continue
      if (m.image == 'pressure_plate1'):
        door1 = True
        continue
      if (m.image == 'stone_pressure_plate'):
        door2 = True
        continue
      if (m.image == 'iron_door_open'):
        continue
      if (m.image == 'wooden_door_open'):
        continue
      if (m.image == 'map') != True:
        map_status = False
      if (m.image == 'map'):
        if fog == True: #if fog is on, show the corresponding map for that level
          map_status = True
          if level_num == 1:
            map.image = 'map1'
            map_status = True
            continue
          elif level_num == 2:
            map.image = 'map2'
            map_status = True
            continue
          elif level_num == 3:
            map.image = 'map3'
            map_status = True
            continue
          elif level_num == 4:
            map.image = 'map4'
            map_status = True
            continue
          elif level_num == 5:
            map_status = True
            continue
        else: 
          continue
          
           
      else: #collects coin, replaces it with air so it can't be collected again
        if (m.image=='coin'):
          m.image = 'air'
          music.fadeout(0.2)
          music.play_once('coin')
          music.queue('bg_music')
          score += 1
          total_score += 1
          continue

          
        if (m.image=='portal'): #takes player to next level via portal
          if level == level1:
            #rebuilds level by resetting all variable and calling build_walls function
            level = level2
            level_num = 2
            player.x = 85
            player.y = 600
            walls.clear()
            door1 = False
            door2 = False
            score = 0
            build_walls(level)
          elif level == level2:
            level = level3
            level_num = 3
            walls.clear()
            build_walls(level)
            score = 0
            door1 = False
            door2 = False
          elif level == level3:
            level = level4
            level_num = 4
            walls.clear()
            build_walls(level)
            score = 0
            door1 = False
            door2 = False
          elif level == level4:
            level = level5
            level_num = 5
            walls.clear()
            score = 0
            build_walls(level)
            door1 = False
            door2 = False
          elif level == level5:
            game = 3
          
        #moves player
        if dx > 0: 
          player.right = m.left
        elif dx < 0: 
          player.left = m.right
        elif dy > 0: 
          player.bottom = m.top
        elif dy < 0: 
          player.top = m.bottom

#reads and builds the walls from the arrays. Stored as function because it is frequently called
def build_walls(lvl):
  global level1, level2, level3
  x = 0
  y = 150
  #reads each column and row to check for objects. If it encounters an object, call it's function to place the thing there
  for row in lvl:
    for column in row:
        if column == "W":
          add_wall(x+50,y)
        if column == "E":
          add_portal(x+50,y)
        if column == "G":
          add_coin(x+50,y)
        if column == "D":
          add_door(x+50,y)
        if column == "P":
          add_pressure_plate(x+50, y)
        if column == "K":
          add_single_door(x+50,y)
        if column == "Q":
          add_stone_pressure_plate(x+50,y)
        if column == "M":
          add_map(x+50,y)
        x += 36
    y += 36
    x = 0

build_walls(level1)

def update():
  global game,dy, dx, door1, directg1, directg2, directg3, directg4, directg5, directg6, directg7
  if xy <= 0:
    game = 4
  if level_num == 5:
    #guard movement, flips when it hits boundary 
    if guard1.y == 402 or guard1.y == 240:
      directg1 *= -1
    if guard2.y == 402 or guard2.y == 240:
      directg2 *= -1
    if guard3.x == 323 or guard3.x == 490:
      directg3 *= -1
    if guard4.x == 323 or guard4.x == 490:
      directg4 *=  -1
  if level_num == 4:
    if guard5.x == 535 or guard5.x == 712:
      directg5 *= -1
    if guard6.x == 383 or guard6.x == 68:
      directg6 *= -1
  if level_num == 3:
    if guard7.y == 419 or guard7.y == 560:
      directg7 *= -1


  #keyboard input for player movement
  if player.y <= HEIGHT and player.x <= WIDTH:
    if keyboard.w:
      move(player, 0, -5)
      player.image ="player_up"

    elif keyboard.s:
      move(player, 0, 5)
      player.image = "player_down"

    elif keyboard.a:
      move(player, -5, 0)
      player.image = "player_left"

    elif keyboard.d:
      move(player, 5, 0)
      player.image = "player_right"

def draw():
  global game, timer, alarm, background_music, directg1, directg2, directg3, directg4, directg5, directg6, directg7, guard1, guard2, guard3, guard4, guard5, guard6, guard7,xy
  if game == 0: #Tutorial screen
    screen.clear()
    start_screen.draw()
    screen.draw.textbox("""Goal:
==============================================
1. Reach the Door to proceed to the next level
----------------------------------------------
2. Collect coins to tally bonus score
----------------------------------------------
3. Reach the end in the fastest time
----------------------------------------------
RECOMMENDED: PLAY WITH FOG 
==============================================
                        """, middle, color = "red")
    screen.draw.filled_rect(menu2_bg, dark_green)
    screen.draw.filled_rect(menu, stone_gray)
    screen.draw.textbox("BΛCK TӨ MΣПЦ", menu, color = "black")
    
  elif game == 1: # Main menu, puts all the shapes and text onto screen
    start_screen.draw()
    #title
    screen.draw.textbox("MΛZΣ ЩΛLKΣЯ", start_box, color = "red")
    #tutorial box
    screen.draw.filled_rect(faq_background, dark_green)
    screen.draw.filled_rect(faq, stone_gray )
    screen.draw.textbox("ΉӨЩ TӨ PLΛY", faq, color = "black")
    #start button
    screen.draw.filled_rect(start_bg, dark_green)
    screen.draw.filled_rect(begin, stone_gray)
    screen.draw.textbox("STΛЯT", begin, color = "black")
    #music box
    screen.draw.filled_rect(music_box_bg, dark_green)
    screen.draw.filled_rect(music_box, stone_gray)
    screen.draw.textbox(("MЦSIC: "+ music_status), music_box, color = "black")
    #volume bar
    screen.draw.filled_rect(volume_box, dark_green)
    screen.draw.filled_rect(volume_box2, stone_gray)
    #fog setting
    screen.draw.filled_rect(fog_box_bg, dark_green)
    screen.draw.filled_rect(fog_box, stone_gray)
    screen.draw.textbox(("FӨG: "+ fog_status),fog_box,color ="black")
    


  elif game == 2: #Main game loop
    score_level = 0 #sets the score per level
    if level_num == 1:
      score_level = 0
    elif level_num == 2:
      score_level = 4
    elif level_num == 3:
      score_level = 8
    elif level_num == 4:
      score_level = 7
    elif level_num == 5:
      score_level = 15
    if alarmed:
      alarm.draw()
      
    clock.schedule(start_clock, 1) #calls the start_clock function to start a timer 
    
    screen.clear()
    background.draw()

    #draws everything inside the walls array 
    for w in walls:
      #checks to see if door is open or closed
      if (w.image == 'iron_door_closed') and door1 == False:
        w.image = 'iron_door_closed'
      elif (w.image == 'iron_door_closed') and door1:
        w.image = 'iron_door_open'
        music.fadeout(0.2)
        music.play_once('door')
        music.queue('bg_music')
      #second door. Changes image depending on if it's open/closed, plays a sound
      if (w.image == 'wooden_door_closed') and door2 == False:
        w.image = 'wooden_door_closed'
      elif (w.image == 'wooden_door_closed') and door2:
        w.image = 'wooden_door_open'
        music.fadeout(0.2)
        music.play_once('wood_door')
        music.queue('bg_music')


      portal.draw()
      w.draw()
      #checks for guard collision 
      
      if level_num == 3:
        if player.colliderect(guard7):
          alarmed(guard7)
      elif level_num == 4:
        if player.colliderect(guard5):
          alarmed(guard5)
        if player.colliderect(guard6):
          alarmed(guard6)
      elif level_num == 5:
        if player.colliderect(guard1):
          alarmed(guard1)      
        if player.colliderect(guard2):
          alarmed(guard2)
        if player.colliderect(guard3):
          alarmed(guard3)
        if player.colliderect(guard4):
          alarmed(guard4)
            

    #guard movement for final level 
    if level_num == 3:
      guard7.y += directg7
      if directg7 > 0:
        guard7.image = 'guard_down'
        guard7.draw()
      elif directg7 < 0:
        guard7.image = 'guard_up'
        guard7.draw()
    if level_num == 4:
      guard5.x += directg5
      guard6.x += directg6
      if directg5 > 0:
        guard5.image = 'guard_right'
        guard5.draw()
      elif directg5 <0:
        guard5.image = 'guard_left'
        guard5.draw()
      if directg6 > 0:
        guard6.image = 'guard_right'
        guard6.draw()
      elif directg6 < 0:
        guard6.image = 'guard_left'
        guard6.draw()
    if level_num == 5:
      guard1.y += directg1
      guard2.y += directg2
      guard3.x += directg3
      guard4.x += directg4
    #changes the image to the correct direction 
      if directg1 > 0:
        guard1.image = 'guard_down'
        guard1.draw()
      elif directg1 < 0:
        guard1.image = 'guard_up'
        guard1.draw()
      if directg2 < 0:
        guard2.image = 'guard_up'
        guard2.draw()
      elif directg2 > 0:
        guard2.image = 'guard_down'
        guard2.draw()
      if directg3 > 0: 
        guard3.image = 'guard_right'
        guard3.draw()
      elif directg3 < 0:
        guard3.image = 'guard_left'
        guard3.draw()
      if directg4 > 0:
        guard4.image = 'guard_right'
        guard4.draw()
      elif directg4 < 0:
        guard4.image = 'guard_left'
        guard4.draw()
      
    player.draw()

    #fog (just 4 rectangles that cover the map and moves with the player)
    if fog == True:
      fog_bottom = Rect(player.x-2000, player.y+80, 4000, 2000)
      screen.draw.filled_rect(fog_bottom, "black")
      fog_top = Rect(player.x-2000, player.y-2000, 4000, 1920)
      screen.draw.filled_rect(fog_top, "black")
      fog_left = Rect(player.x-2000, player.y-80, 1920, 2000)
      screen.draw.filled_rect(fog_left, "black")
      fog_right = Rect(player.x+80, player.y-80, 2000, 2000)
      screen.draw.filled_rect(fog_right, "black")
      
    screen.draw.textbox(("Level "+str(level_num) + ": Coins: "+ str(score) + "/"+ str(score_level)), message_box, color=("white"))
    screen.draw.textbox(str(round(timer,1)), timer_box, color = "white")
    
    if map_status == True:
      map1.x = 160
      map1.y = 200
      map.draw()
    
  elif game == 3: #victory screen, prints timer and score
    screen.clear()
    background2.draw()
    timer = round(timer,2)
    screen.draw.textbox(("Total Score: " + str(total_score)+"/34"), end_box, color = "white")
    screen.draw.textbox(("Your final time was: "+str(timer)), end_timer_box, color = "white")
    print("Congradulations ", user, " for finishing the game!")
  elif game == 4:
    screen.clear()
    death_screen.draw()
    screen.draw.filled_rect(retry_bg, color = 'red')
    screen.draw.filled_rect(retry, color = 'black')
    screen.draw.textbox("PLΛY ΛGΛIП", retry, color = "red")
    

    
#def on_mouse_move(pos, buttons): #mouse coordinate debugger
  #print(pos)
pgzrun.go()