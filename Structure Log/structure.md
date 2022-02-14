# NFT Structure
## **UNDEFINEDs:**
Explanation here.
## **Code:**
Code related stuff here.
## **Selling/OpenSea:**
Selling/OpenSea related stuff here.
## **Presentation/Execution:**
Weakpoints in script (ETH part)
## **Advertising:**
Advertising related stuff here.
## **Design:**
Design related stuff here.
### _102 (R, G, B) Range:_
Quite nice. Looks very weirdcore-ish, color scheme just fits very nicely with the whole glitch theme. Could need a little adjusting, may look good darker, but we're in the ballpark.
### _Drip Effect:_
Explanation + Sketch + Code (start putting code on here e.g. randcolor function, or for the drip effect. You should do the thing with finding the range of all the points, drawing the lines, etc.)

# Development Log
## Day 1:
Made a pretty fair amount of progress today. I got the foundations down for building an NFT with Pillow, and I really think I can do it. I have all the Python knowledge, maybe I'll need a little more Pillow knowledge, but I'm ready. With the right design choices, my code, and this log, I'll be able to create my long awaited NFT.

Basically I followed a YouTube tutorial (here: https://www.youtube.com/watch?v=oYuM7ljiQZM) which explains how to draw lines and shape on screen with Pillow. I mixed up the code and redesigned it so it generated a set number of images with random shapes on them. Not exactly my NFT, but its a really darn good start. I guess you could call it part of the foundations of it.

On the other note, I decided to create this log to keep track of my ideas, code, and journery creating my NFT. I'll make sure to work on this project, along with its design and log, everyday.

Anyways, my laptops going to die and thats all I have for today. Here's todays code.
```
from PIL import Image, ImageDraw, ImageFont
import random

def randcolor():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return r, g, b

photo = Image.open('test_blank.jpg')
width, height = photo.size
count = 10
shapes = 10

for f in range(count):
  photo = Image.open('test_blank.jpg')
  draw = ImageDraw.Draw(photo)
  for _ in range(shapes):
    draw.rectangle((random.randint(0, width), random.randint(0, height), random.randint(0, width), random.randint(0, height)), fill=randcolor(), width=random.randint(1, 10), outline=randcolor())
  photo.save(f'inter{f + 1}.png')
  ```
## Day 2:
I was pretty busy today, but I got a really good amount done today. Created a few attributes, reformatted the code into functions, and did some other small tweaks to the code so it generates better art.

I consumed close to 354ml of caffeine today, which is why I was able to get so much done today for being busy. 8)

I experimented with having my code on a GitHub repository, and boy was it a headache.

I guess if I wanted to work on this in school I could email the code back in fourth, but I doubt the computer could run it so there isn't much of a point.

Overall, I'm really happy with the work that I got done today. I look forward to seeing what I'll be adding tomorrow. I think tomorrow I'll focus more on the idea of randomization and attributes, and changing the random shape generation. I had an interesting shape repeating pattern in my head. I think I'll also be working on different background colors and things. I should also tidy up some of the attributes, and incorporate the rarity point system I had in mind. One last thing, I should format it like some sort of card. So, neater design, card, and background colors + maybe other background stuff. Top effects could maybe overlay it? Transparancy should be used too (like with the glithced branches)!

Man, I have a lot to work on.

But hey, maybe we can release this NFT in a few weeks. I look forward to presenting.

But anyways its already 2:25 AM and I have school tomorrow. That's all folks! Here's the code:

```
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
width, height = photo.size
count = 1
shapes = 40
top_images = 0
draw = ImageDraw.Draw(photo)

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

def glitchbranch():
  # Looks cool inside shape look with censorship. Background stuff maybe?

  branch_count = random.randint(2, 5)
  for _ in range(branch_count):
    fillcol = randcolor()
    branch_pos = random.randint(10, 500)
    draw.line((0, branch_pos, random.randint(5, 200), branch_pos), width=random.randint(20, 40), fill=fillcol)

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
  # Looks pretty cool inside shape look with glitchbranch. Background stuff maybe?

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
  shape_width = 10
  draw.rectangle ((x_1, y_1, x_2, y_2), fill=randcolor(), width=shape_width, outline=0)

for f in range(count):
  photo = Image.open('back.jpg')
  draw = ImageDraw.Draw(photo)

  for _ in range(shapes):
    randshapes()
    glitchbranch()
    censorship()
  photo.save(f'nft{f + 1}.png')
  print(width, height)
  print(name)
```
## Day ??? (Gonna count it was day 3):
Wow. Here I am, on a sunday evening. I haven't exactly written in my log, but wow. My code has improved so much. I looked back at what my NFT looked like in its infancy (when it was about 20 lines), compared to now (which is 180 lines). I stopped logging my code in this journal and created a GitHub repository for it instead. I'm really glad I started this NFT project. This NFT is going to be big. People are going to buy it. Not only is my NFT going to be a huge success, but I've learned so much while creating it. I've learned about VSCode, Python, GitHub, and so much. I'm so excited to release my NFTs. In a few weeks, it could even be ready. I definetly have a lot to work on and add, but it could possibly be ready soon. The development speed of this NFT has been extremely fast. I started from a crappy shape generator with 20 lines of code about 1-2 weeks ago, to an incredible NFT generator with 180 lines of code. God, I'm so excited and happy right now. I'm proud of myself. This project is going so good, and its the first actual programming project I've stuck with and done. I think I've found something I love doing with programming: creating programs to generate art and sell them as NFTs. Its profitable, fun, and theres so much to do in learn. Who knows maybe for my next project I can do some sort of generative art NFT with machine learning! The possibilties are endless. After this I kinda wanna dig into things like Machine Learning and App Development (specifically iOS or cross-platform). Maybe if my NFT gets big, I could purchase my own Macbook. At its maximumly best, I could make close to 70k with my NFT... thats crazy. Thats absurd for a 13 almost 14 year old. Im only in 8th grade. Thats enough to buy a tesla for crying out loud. But thats in theory. I could make even more since I plan to boost the price if my NFTs get popular and start selling rapidly. Who knows. I have 10k NFTs, and when its popular its assume theres 2k left, and they're selling for an average of 100$ each. THATS 200K DOLLARS. Thats what a lot of high prefessional people make in a year. I made that in a month to a few months. If you feel like you aren't making any money, and assuming that we can make around 200k if they sell out, thats close to 1784$ a day. Thats crazy. I could buy the Macbook I wanted in an entire day. You could buy a pretty solid house. You could buy a the corvette your want. Expensive watches, nice things, everything. All for selling this NFT. Always wanted to pull up to school in a luxury car? No problem! Come in your corvette. Jealous people you knows dads have Teslas? No need to frett. They paid for that over time, and you paid for your corvette up front. No worries! I'll try to update you again tomorrow. I still have a lot to do. Advertising, the website, social media, coding, a lot. Anyways, I'll talk to you later! Codes on my GitHub!

Correction: I could buy a lamborghini. Keep that in mind.

Lets do this.

Advertising could be an issue though.

# Day 4