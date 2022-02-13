from PIL import Image, ImageDraw
import random
import os

totalrarity = 0

adjectives = [
  'Sublime', 'Abhorrent', 'Introverted', 'Mind of', 'Ceasing', 'The', 'Ostracized', 'Modular', 'Weirdcore', 'Hash'
]

titles = [
  'Thoughts', 'Problems', 'Malware', 'Mess', 'Philiographia', 'Terminality', 'Malignancy', 'Perfection', 'Impurity', 'Compiler'
]

tokenname = f"{adjectives[random.randint(0, len(adjectives)-1)]} {titles[random.randint(0, len(titles)-1)]}"

# Filter Selector
artfilter = random.randint(1, 5)
if artfilter != 5: 
  artfilter = 'col' #80% for Color
  colrange = 4
  totalrarity += 10
else:
  artfilter = 'mono' #20% for Monochrome
  colrange = 3
  totalrarity += 50

# --- Scheme Selector --- #
cols = [(115, 38, 38), (51, 23, 87), (212, 219, 66), (96, 147, 189), (48, 48, 48)] 
# Red: 0, Purple: 1, Yellow: 2, Blue: 3, Gray: 4

monos = [(0, 0, 0), (255, 255, 255), (33, 33, 33), (112, 112, 112)]
# Black: 0, White: 1, Dark Gray: 2, Light Gray: 3

rerollspecialty = 0
firstcolsel = random.randint(0, colrange)
secondcolsel = random.randint(0, colrange)
# Reroll Specialty grants special attribuite depending on the number of rerolls.

while True:
  if firstcolsel == secondcolsel:
   secondcolsel = random.randint(0, colrange)
   rerollspecialty += 1 
  else:
    break

if artfilter == 'col':
  firstcol = cols[firstcolsel]
  secondcol = cols[secondcolsel]
elif artfilter == 'mono':
  firstcol = monos[firstcolsel]
  secondcol= monos[secondcolsel]

def schemealt():
  c = random.randint(0, 1)
  if c == 0:
    return firstcol
  elif c == 1:
    return secondcol
# --- Scheme Selector End --- #

# -- Trait Selector --- #

# Build trait selector when done with all the traits

# --- Trait Selector End --- #
shapes = 60
count = 1
shapewidth = random.randint(1, 30)

art = Image.open('back.png')
draw = ImageDraw.Draw(art)
width, height = art.size

# --- Traits --- #
def glitchbranch():
  branch_count = random.randint(5, 15)
  for _ in range(branch_count):
    fillcol = schemealt()
    branch_pos = random.randint(0, width)
    draw.rectangle((0, branch_pos, width, height), outline=schemealt())

def shards():
  shard_count = random.randint(0, 5)
  for _ in range(shard_count):
    fillcol = schemealt()
    x_1 = random.randint(0, width)
    y_1 = random.randint(0, height)
    x_2 = x_1 + random.randint(5, 20)
    y_2 = y_1 + random.randint(5, 20)
    draw.rectangle((x_1, y_1, x_2, y_2), outline=schemealt())

def censorship():
  censor_count = random.randint(0, 5)
  for _ in range(censor_count):
    x_1 = random.randint(0, width)
    y_1 = random.randint(0, height)
    x_2 = x_1 + random.randint(200, 300)
    y_2 = y_1 + random.randint(200, 300)
    draw.line((x_1, y_1, x_2, y_1), width=random.randint(40, 80), fill=0)

def shape_drag():
  isstair = random.randint(1, 2)
  if isstair == 1:
    draglen = random.randint(3, 10)
  elif isstair == 2:
    draglen = 100

  start_x = random.randint(0, width)
  start_y = random.randint(0, height)
  size = 200

  dirlist = [10, -10]
  x_dir =  dirlist[random.randint(0, 1)]
  y_dir = dirlist[random.randint(0, 1)]

  for f in range(draglen):
    if f < 1:
      draw.rectangle((start_x, start_y, start_x + size, start_y - size), fill=schemealt(), outline=0, width=shapewidth)
    else:
      draw.rectangle((start_x, start_y, start_x + size, start_y - size), fill=schemealt(), outline=0, width=shapewidth)
      start_x += x_dir
      start_y -= y_dir

def triangles():
  # Left: 1, Right: 2
  side = random.randint(1, 2)
  if side == 1:
    x_1 = 0
    y_1 = random.randint(0, height)

    x_2 = 0
    y_2 = random.randint(0, height)

    x_3 = random.randint(20, (height - random.randint(50, 200)))
    y_3 = random.randint(0, (height - random.randint(50, 200)))

    draw.polygon(((x_1, y_1), (x_2, y_2), (x_3, y_3)),fill=schemealt(), outline=0, width=shapewidth)
  elif side == 2:
    x_1 = width
    y_1 = random.randint(0, height)

    x_2 = width
    y_2 = y_1 - random.randint(50, 200)

    x_3 = random.randint(20, (height + random.randint(50, 200)))
    y_3 = random.randint(width, (height + random.randint(50, 200)))

    draw.polygon(((x_1, y_1), (x_2, y_2), (x_3, y_3)),fill=schemealt(), outline=0, width=shapewidth)

def rotate():
  global art
  global rotation
  # Left: 0, Down: 1, Right: 2, Up: 3
  rotation = random.randint(0, 3)
  art = art.rotate(rotation * 90)

# --- Traits End --- #

# --- Generator --- #
for f in range(count):
  art = Image.open('back.png')
  draw = ImageDraw.Draw(art)

  for _ in range(shapes):
    shape_drag()
    glitchbranch()
    censorship()
    shards()
    triangles()
    

  rotate()
  shape_drag()
  art.save(f'nft{f + 1}.png')

  print(width, height)
  print(rerollspecialty, firstcol, secondcol)
  print(tokenname)
  print(totalrarity)
  print(rotation)
# --- Generator End --- #