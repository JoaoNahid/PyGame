import pygame

WIN_WIDTH = 576
WIN_HEIGHT = 324

#COLORS
COLOR_TEXT_ORANGE = (255,128,0)
COLOR_TEXT_ORANGE_700 = (255,128,0, 0.7)
COLOR_TEXT_WHITE = (255,255,255)

# Speed
ENTITY_SPEED = {
    # Player
    'Player1': 3,
    'Player2': 3,
    # Enemy
    'Enemy1': 3,
    'Enemy2': 5,
    # Level 1
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
}

# Health
ENTITY_HEALTH = {
    'Level1Bg0': 9999,
    'Level1Bg1': 9999,
    'Level1Bg2': 9999,
    'Level1Bg3': 9999,
    'Level1Bg4': 9999,
    'Level1Bg5': 9999,
    'Level1Bg6': 9999,
    'Player1': 1000,
    'Player2': 1000,
    'Player1Shoot': 1000,
    'Player2Shoot': 1000,
    'Enemy1': 100,
    'Enemy2': 300,
}

# Delay
ENTITY_DELAY = {
    'shoot': 10
}
# Event
EVENT_ENEMY = pygame.USEREVENT + 1
