from gasp import *          # import everything from the gasp library

begin_graphics(background=color.YELLOW)                # open the graphics canvas
 
def draw_house(x, y):

    Box((x, y), 100, 100, filled=True, color=color.RED)     # the house
    Box((x + 35, y), 30, 50, filled=True, color=color.BLUE)       # the door
    Box((x + 20, y + 60), 20, 20, filled=True, color=color.WHITE)       # the left window
    Box((x + 60, y + 60), 20, 20, filled=True, color=color.WHITE)       # the right window
    Line((x, y + 100), (x + 50, y + 140))  # the left roof
    Line((x + 50, y + 140), (x + 100, y + 100)) # the right roof

draw_house(20, 20)
draw_house(140, 20)
draw_house(20, 180)

update_when('key_pressed')  # keep the canvas open until a key is pressed
end_graphics()              # close the canvas (which would happen
                            # anyway, since the script ends here, but it
                            # is better to be explicit).

#pretty sure there's nothing wrong with my code; this graphics module sux
