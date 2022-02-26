from PIL import Image, ImageDraw
import random
import math # Perlin Noise?

def col(brightness=0, darkness=0):
  r = (random.randint(0, 255) + brightness) - darkness
  g = (random.randint(0, 255) + brightness) - darkness
  b = (random.randint(0, 255) + brightness) - darkness

  return (r, g, b)

width = 1080
height = width

piece = Image.new('RGB', (width, height), col(brightness=20))
draw = ImageDraw.Draw(piece)

grid_dem = 3
x_space = round(width / grid_dem)
y_space = round(height / grid_dem)

# Draws X-Axis grid lines
for x in range(grid_dem):
  if x == 0: x = 1

  current_x = x_space * x
  draw.line((0, current_x, width, current_x))

# Draws Y-Axis grid line
for y in range(grid_dem):
  if y == 0: y = 1

  current_y = y_space * y
  draw.line((current_y, 0, current_y, height))

piece.save('grid.png')