from pico2d import *

open_canvas()
tukorea = load_image('TUK_GROUND.png')
character = load_image('character_sheet.png')

def handle_events():
    global move, dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            move = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                move = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

move = True
x = 800 // 2
y = 90
frame = 0
dir_x = 0
dir_y = 0

while move:
    clear_canvas()
    tukorea.draw(500,90)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 4
    x += dir_x * 20
    y += dir_y * 20
    delay (0.05)

close_canvas()