class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
        
    for row in level:
    ...

total_level_width  = len(level[0])*32 # calculate size of level in pixels
total_level_height = len(level)*32    # maybe make 32 an constant
camera = Camera(*to_be_implemented*, total_level_width, total_level_height)

entities.add(player)
... 

# draw background
for y in range(32):
    ...

camera.update(player) # camera follows player. Note that we could also follow any other sprite

# update player, draw everything else
player.update(up, down, left, right, running, platforms)
for e in entities:
    # apply the offset to each entity.
    # call this for everything that should scroll,
    # which is basically everything other than GUI/HUD/UI
    screen.blit(e.image, camera.apply(e)) 

pygame.display.update()
