from pico2d import *

open_canvas()
tukorea = load_image('TUK_GROUND.png')
character = load_image('character_sheet.png')

def handle_events():
    global move, dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            move = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_UP:
                pass



close_canvas()