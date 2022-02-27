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

GRID_DEM = random.randint(2, 20)
IS_BLACK = True
GRID_WIDTH = 10
OUTLINE_COLOR = (255, 255, 255)

x_space = round(width / GRID_DEM)
y_space = round(height / GRID_DEM)


# Creates array for grid
grid = []
placeholder = 0

for _ in range (1, GRID_DEM * GRID_DEM):
  grid.append([placeholder, placeholder])

# Draws X-Axis grid lines
dash_color = [255, 255, 255]

if IS_BLACK:
  dash_color = (0, 0, 0)
elif not IS_BLACK:
  dash_color = tuple(dash_color)

for x in range(GRID_DEM):
  if x == 0: x = 1

  current_x = x_space * x
  draw.rectangle((0, current_x + GRID_WIDTH, width, current_x), fill=dash_color, outline=OUTLINE_COLOR)

# Draws Y-Axis grid line
for y in range(GRID_DEM):
  if y == 0: y = 1

  current_y = y_space * y
  draw.rectangle((current_y + GRID_WIDTH, 0, current_y, height), fill=dash_color, outline=OUTLINE_COLOR)

draw.rectangle((490, 50, 600, 3), fill=0, outline=(255, 255, 255))

piece.save('grid.png')
print(GRID_DEM, len(grid))