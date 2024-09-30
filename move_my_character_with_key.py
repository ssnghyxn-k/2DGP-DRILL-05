from pico2d import *

open_canvas(800,600)
tukorea = load_image('TUK_GROUND.png')
character = load_image('character_sheet_2.png')

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
y = 600 // 2
frame = 0
dir_x = 0
dir_y = 0
w = 800
h = 600
frame_w = 75
frame_h = 75

while move:
    clear_canvas()
    tukorea.draw(500,90)
    frame_x = (frame % 3) * frame_w
    frame_y = (3 - (frame // 3) - 1) * frame_h
    character.clip_draw(frame_x, frame_y, frame_w, frame_h, x, y)
    update_canvas()
    handle_events()

    frame = (frame + 1) % 12
    x += dir_x * 10
    y += dir_y * 10

    if x < 0:
        x = 0
    elif x > w:
        x = w - 100

    if y < 0:
        y = 0
    elif y > h:
        y = h - 100

    delay (0.05)

close_canvas()