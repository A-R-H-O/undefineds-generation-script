from PIL import Image, ImageDraw, ImageFont
import random

# Name rarity? (Common adjectives/titles, rare ones, etc.) More adjectives and titles needed.
adjectives = [
  'Sublime', 'Abhorrent', 'Introverted', 'Mind of', 'Ceasing', 'The', 'Ostracized', 'Modular', 'Weirdcore', 'Hash'
]

titles = [
  'Thoughts', 'Problems', 'Malware', 'Mess', 'Philiographia', 'Terminality', 'Malignancy', 'Perfection', 'Impurity', 'Compiler'
]

name = f"{adjectives[random.randint(0, len(adjectives)-1)]} {titles[random.randint(0, len(titles)-1)]}"

photo = Image.open('back.jpg')
draw = ImageDraw.Draw(photo)
width, height = photo.size

def randcolor():
  r = random.randint(50, 200)
  g = random.randint(50, 200)
  b = random.randint(50, 200)
  return r, g, b

def randcolorover():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(250, 255)
  return r, g, b

draw.rectangle((0, 0, width, height), fill=(0, 0, 0))
draw.rectangle((0, 0, width, height), fill=randcolor())
photo.save('back.jpg')

count = 1
shapes = 60
top_images = 0

def glitchbranch():
  branch_count = random.randint(2, 5)
  for _ in range(branch_count):
    fillcol = randcolor()
    branch_pos = random.randint(10, 500)
    draw.rectangle((0, branch_pos, width, height), outline=randcolor())

def shards():
  shard_count = random.randint(0, 5)
  for _ in range(shard_count):
    fillcol = 0
    x_1 = random.randint(0, width)
    y_1 = random.randint(0, height)
    x_2 = x_1 + random.randint(5, 20)
    y_2 = y_1 + random.randint(5, 20)
    draw.line((x_1, y_1, x_2, y_2), width=random.randint(20, 40), fill=fillcol)

def censorship():
  censor_count = random.randint(0, 5)
  for _ in range(censor_count):
    fillcol = 0
    x_1 = random.randint(0, width)
    y_1 = random.randint(0, height)
    x_2 = x_1 + random.randint(200, 300)
    y_2 = y_1 + random.randint(200, 300)
    draw.line((x_1, y_1, x_2, y_1), width=random.randint(40, 80), fill=fillcol)

def randshapes():
  x_1 = random.randint(0, width - 10)
  y_1 = random.randint(x_1, height - 10)
  x_2 = random.randint(y_1, width - 10)
  y_2 = random.randint(x_2, height - 10)
  shape_width = 5
  draw.rectangle ((x_1, y_1, x_2, y_2), fill=randcolor(), width=shape_width, outline=0)

def shape_drag():
  draglen = random.randint(3, 10)
  start_x = random.randint(0, width)
  start_y = random.randint(0, height)
  size = 200

  dirlist = [10, -10]
  x_dir =  dirlist[random.randint(0, 1)]
  y_dir = dirlist[random.randint(0, 1)]

  for f in range(draglen):
    if f < 1:
      draw.rectangle((start_x, start_y, start_x + size, start_y - size), fill=randcolor(), outline=0, width=5)
    else:
      draw.rectangle((start_x, start_y, start_x + size, start_y - size), fill=randcolor(), outline=0, width=5)
      start_x += x_dir
      start_y -= y_dir

for f in range(count):
  photo = Image.open('back.jpg')
  draw = ImageDraw.Draw(photo)

  for _ in range(shapes):
    shape_drag()
    glitchbranch()

  shape_drag()
  photo.save(f'nft{f + 1}.png')
  print(width, height)
  print(name)