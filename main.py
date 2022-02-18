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
r1 = random.randint(70, 255)
r2 = random.randint(70, 255)
r3 = random.randint(70, 255)
r4 = random.randint(70, 255)
r5 = random.randint(70, 255)

colsel = 1 # random.randint(0, 2)
monosel = random.randint(0, 1)

if colsel == 0:
  cols = [(r1, r2, r3), (r3, r1, r2), (r2, r1, r3), (r3, r1, r2), (r5, r5, r5)]
elif colsel == 1:
  cols = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))]
elif colsel == 2:
  cols = [(115, 38, 38), (51, 23, 87), (212, 219, 66), (96, 147, 189), (48, 48, 48)]
  # Red: 0, Purple: 1, Yellow: 2, Blue: 3, Gray: 4

if monosel == 0:
  monos = [(0, 0, 0), (255, 255, 255), (33, 33, 33), (112, 112, 112)]
  # Black: 0, White: 1, Dark Gray: 2, Light Gray: 3
elif monosel == 1:
  monos = [(r1, r1, r1), (r2, r2, r2), (r3, r3, r3), (r4, r4, r4)]


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
shapes = 90
# Looks good with 90 too. Experiment with different shape counts.
# Shape count randomization would be perfect
# Shape count => rarity and value
# The more the shapes, the cooler it looks
# More shapes could pose an issue to GIFs (maybe animations)
# Medium shape count VS High/Very High shape count

# If you set it to a really low number like 1-3-5 you could probably get some cool results.
# Further experimentation is required.


count = 1
shapewidth = random.randint(1, 20)

art = Image.open('back.png')
draw = ImageDraw.Draw(art)
width, height = art.size

# --- Traits --- #
def glitchbranch():
  for _ in range(1):
    branch_count = random.randint(5, 15)
    for _ in range(branch_count):
      branch_pos = random.randint(0, width)
      draw.rectangle((0, branch_pos, width + 20, height + 20), outline=0, width=10)

def shards():
  shard_count = random.randint(0, 5)
  for _ in range(shard_count):
    x_1 = random.randint(0, width)
    y_1 = random.randint(0, height)
    x_2 = x_1 + random.randint(5, 50)
    y_2 = y_1 + random.randint(5, 50)
    draw.rectangle((x_1, y_1, x_2, y_2), outline=0, width=10)

def censorship():
  for _ in range(1):
    censor_count = random.randint(0, 5)
    for _ in range(censor_count):
      x_1 = random.randint(0, width)
      y_1 = random.randint(0, height)
      x_2 = x_1 + random.randint(200, 300)
      y_2 = y_1 + random.randint(200, 300)
      draw.line((x_1, y_1, x_2, y_1), width=random.randint(40, 80), fill=0)

def shape_drag():
  dirchangeinterval = random.randint(10, 60)
  isstair = random.randint(1, 2)
  if isstair == 1:
    draglen = random.randint(3, 10)
  elif isstair == 2:
    draglen = 100

  start_x = random.randint(0, width)
  start_y = random.randint(0, height)
  size = 200

  dirval = random.randint(1, 5)
  dirval2 = random.randint(1, 5)

  dirlist = [(dirval * 10), (dirval2 * -10)]

  dirlistrand = [random.randint(1, 5) * 10, random.randint(1, 5) * -10]

  altdirlist = [20, -20, 10, -10]

  x_dir =  dirlist[random.randint(0, 1)]
  y_dir = dirlist[random.randint(0, 1)]

  for f in range(draglen):
    if f < 1:
      draw.rectangle((start_x, start_y, start_x + size, start_y - size), fill=schemealt(), outline=0, width=shapewidth)
    else:
      mathtype1 = random.randint(1, 2)
      mathtype2 = random.randint(1, 2)
      if f < dirchangeinterval:
        draw.rectangle((start_x, start_y, start_x + size, start_y - size), fill=schemealt(), outline=0, width=shapewidth)
        start_x += x_dir
        start_y -= y_dir
      elif f >= dirchangeinterval:
        draw.rectangle((start_x, start_y, start_x + size, start_y - size), fill=schemealt(), outline=0, width=shapewidth)
        start_x -= x_dir
        start_y += y_dir

def triangles():
  # Left: 1, Right: 2
  for _ in range(2):
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
  print(f"{tokenname} | {artfilter} | {shapewidth} | {colsel}")
  print(totalrarity)
  print(rotation)
# --- Generator End --- #