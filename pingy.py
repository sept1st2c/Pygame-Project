import pygame,sys,random

def ball_animation():
    global ball_speed_x,ball_speed_y,player_score,opponent_score,score_timer
     # ball movement
    ball.x+=ball_speed_x
    ball.y+=ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
       pygame.mixer.Sound.play(pong_sound)
       ball_speed_y *= -1
    
    # Player score
    if ball.left <=0 :
       pygame.mixer.Sound.play(score_sound)
       player_score +=1
       score_timer = pygame.time.get_ticks()

    # Opponent score
    if ball.right >= screen_width:
       pygame.mixer.Sound.play(score_sound)
       opponent_score +=1
       score_timer = pygame.time.get_ticks()
    
    # ball collision with bricks
    if ball.colliderect(player) and ball_speed_x > 0:
     pygame.mixer.Sound.play(pong_sound)
     if abs(ball.right - player.left) < 10:
        ball_speed_x *= -1
     elif abs(ball.bottom - player.top) <10 and ball_speed_y > 0:
        ball_speed_y *= -1
     elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
        ball_speed_y *= -1
        
       
    if ball.colliderect(opponent) and ball_speed_x < 0:
      pygame.mixer.Sound.play(pong_sound)
      if abs(ball.left - opponent.right) < 10:
         ball_speed_x *= -1
      elif abs(ball.bottom - opponent.top) <10 and ball_speed_y > 0:
        ball_speed_y *= -1
      elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
        ball_speed_y *= -1

def player_animation():
  player.y += player_speed
  if player.top <= 0:
       player.top = 0
  if player.bottom >= screen_height:
       player.bottom = screen_height

def opponet_ai():
   if opponent.top < ball.y:
      opponent.top += opponent_speed
   if opponent.bottom > ball.y:
      opponent.bottom -= opponent_speed
   if opponent.top <= 0:
       opponent.top = 0
   if opponent.bottom >= screen_height:
       opponent.bottom = screen_height

def ball_restart():
   global ball_speed_x,ball_speed_y,current_time,score_timer
   
   current_time = pygame.time.get_ticks()
   ball.center = (screen_width/2, screen_height/2)

   if current_time-score_timer < 700:
      num_three = game_font.render("3",False, light_grey)
      screen.blit(num_three,(screen_width/2 -10, screen_height/2 +20))
   
   if 700<current_time-score_timer < 1400:
      num_two = game_font.render("2",False, light_grey)
      screen.blit(num_two,(screen_width/2 -10, screen_height/2 +20))
   
   if 1400<current_time-score_timer < 2100:
      num_one = game_font.render("1",False, light_grey)
      screen.blit(num_one,(screen_width/2 -10, screen_height/2 +20))

   if current_time-score_timer < 2100:
      ball_speed_x,ball_speed_y = 0,0
   else:
       ball_speed_y = 7*random.choice((1,-1))
       ball_speed_x = 7*random.choice((1,-1))
       score_timer = None

   
  

#General Setup
pygame.mixer.pre_init(44100,-16,2,)
pygame.init()
clock = pygame.time.Clock()

#Setting up main window
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

# Game rectangles
ball = pygame.Rect(screen_width/2-15, screen_height/2-15,30,30)
player = pygame.Rect(screen_width-20,screen_height/2-70,10,140)
opponent = pygame.Rect(10,screen_height/2-70,10,140)

bg_color = pygame.Color('grey12')
light_grey = (255, 223, 0)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7

# Text
player_score = 0
opponent_score = 0
game_font = pygame.font.Font('freesansbold.ttf',32)

# Sound
pong_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")

# Timer
score_timer = True

while True:
    #Handling input
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_DOWN:
          player_speed += 7
         if event.key == pygame.K_UP:
          player_speed -= 7
      if event.type == pygame.KEYUP:
         if event.key == pygame.K_DOWN:
          player_speed -= 7
         if event.key == pygame.K_UP:
          player_speed += 7    
    
    # calling function for animation of ball,player,opponent
    ball_animation()
    player_animation()
    opponet_ai()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen, light_grey,(screen_width/2,0),(screen_width/2,screen_height))
    if score_timer:
       ball_restart()
    player_text = game_font.render(f"{player_score}",False,light_grey) 
    screen.blit(player_text,(550,340))

    opponent_text = game_font.render(f"{opponent_score}",False,light_grey) 
    screen.blit(opponent_text,(320,340))
    # Updating the window
    pygame.display.flip()
    clock.tick(60)