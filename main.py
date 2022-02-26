from PIL import Image, ImageDraw
import random
import math # Perlin Noise?

def col(brightness=0, darkness=0, black=False):
  if black:
    r = 0
    g = 0
    b = 0
  elif not black:
    r = (random.randint(0, 255) + brightness) - darkness
    g = (random.randint(0, 255) + brightness) - darkness
    b = (random.randint(0, 255) + brightness) - darkness
  return (r, g, b)

width = 1080
height = width

piece = Image.new('RGB', (width, height), col(darkness=40))
draw = ImageDraw.Draw(piece)

grid_dem = 10
x_space = round(width / grid_dem)
y_space = round(height / grid_dem)


IS_BLACK = True

# Draws X-Axis grid lines
dash_color = [255, 255, 255]

if IS_BLACK:
  dash_color = tuple([0, 0, 0])
elif not IS_BLACK:
  dash_color = tuple(dash_color)

for x in range(grid_dem):
  if x == 0: x = 1

  current_x = x_space * x
  draw.line((0, current_x, width, current_x), fill=dash_color)

# Draws Y-Axis grid line
for y in range(grid_dem):
  if y == 0: y = 1

  current_y = y_space * y
  draw.line((current_y, 0, current_y, height), fill=dash_color)

piece.save('grid.png')