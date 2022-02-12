from PIL import Image, ImageDraw, ImageFont
import random
import os

# Name rarity? (Common adjectives/titles, rare ones, etc.) More adjectives and titles needed.
adjectives = [
  'Sublime', 'Abhorrent', 'Introverted', 'Mind of', 'Ceasing', 'The', 'Ostracized', 'Modular', 'Weirdcore', 'Hash'
]

titles = [
  'Thoughts', 'Problems', 'Malware', 'Mess', 'Philiographia', 'Terminality', 'Malignancy', 'Perfection', 'Impurity', 'Compiler'
]

tokenname = f"{adjectives[random.randint(0, len(adjectives)-1)]} {titles[random.randint(0, len(titles)-1)]}"

photo = Image.open('back.jpg')
draw = ImageDraw.Draw(photo)
width, height = photo.size

def randcolor():
  r = random.randint(50, 200)
  g = random.randint(50, 200)
  b = random.randint(50, 200)
  return r, g, b

# Filter Selector
artfilter = random.randint(1, 5)
if artfilter > 5: #20% chance of Monochrome
  artfilter = 'col'
  colrange = 4
else:
  artfilter = 'mono' #80% chance of Color
  colrange = 3

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
  secondcolsel = cols[secondcolsel]
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


draw.rectangle((0, 0, width, height), fill=(255, 255, 255))
draw.rectangle((0, 0, width, height), fill=(0, 0, 0))
photo.save('back.jpg')

count = 1
shapes = 60

def glitchbranch():
  branch_count = random.randint(5, 15)
  for _ in range(branch_count):
    fillcol = schemealt()
    branch_pos = random.randint(10, 500)
    draw.rectangle((0, branch_pos, width, height), outline=schemealt())

def shards():
  shard_count = random.randint(0, 5)
  for _ in range(shard_count):
    fillcol = schemealt()
    x_1 = random.randint(0, width)
    y_1 = random.randint(0, height)
    x_2 = x_1 + random.randint(5, 20)
    y_2 = y_1 + random.randint(5, 20)
    draw.line((x_1, y_1, x_2, y_2), width=random.randint(20, 40), fill=fillcol)

def censorship():
  censor_count = random.randint(0, 5)
  for _ in range(censor_count):
    x_1 = random.randint(0, width)
    y_1 = random.randint(0, height)
    x_2 = x_1 + random.randint(200, 300)
    y_2 = y_1 + random.randint(200, 300)
    draw.line((x_1, y_1, x_2, y_1), width=random.randint(40, 80), fill=0)

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
      draw.rectangle((start_x, start_y, start_x + size, start_y - size), fill=schemealt(), outline=0, width=5)
    else:
      draw.rectangle((start_x, start_y, start_x + size, start_y - size), fill=schemealt(), outline=0, width=5)
      start_x += x_dir
      start_y -= y_dir

for f in range(count):
  photo = Image.open('back.jpg')
  draw = ImageDraw.Draw(photo)

  for _ in range(shapes):
    shape_drag()
    glitchbranch()

  shape_drag()
  censorship()
  photo.save(f'nft{f + 1}.png')
  print(width, height)
  print(rerollspecialty, firstcol, secondcol)
  print(tokenname)