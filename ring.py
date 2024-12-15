from PIL import Image
from math import pi, sin
from random import random
import numpy as np

A = 2
B = 0.5
C = pi/2
D = 2.5

def makeLinedDrawing(img: Image, rgb: tuple[int, int, int], tolerance: int, scaledHeight: int, radii: int):
  return

def getSine(x: int):
  return A * sin(B * (x + C)) + D

def randomSines(a: int, am: int, h: int):
  l = []
  for i in range(a):
    l.append((am, random() * pi * 2, random() * pi * 2, h))
  def newSine(x: int):
    num = 0
    for i in l:
      num += i[0] * sin(i[1] * (x + i[2])) + i[3]
    return num
  return newSine

def generate_rings(siz: tuple[int, int], thickness: int, randomness: float):
  size = [i * 100 for i in siz]
  img = Image.new('RGB', size, (255, 255, 255))
  layer = np.array([0 for i in range(0, size[0])])
  c = 0
  while True:
    newlayer = np.array([0 for i in range(0, size[0])])
    sinewave = randomSines(10, 100 * (D - A), 0)
    for z in range(siz[0]):
      for j in range(100):
        i = z * 100 + j
        newlayer[i] = layer[i] + round(getSine(layer[j]) * 100 + 100 * sin(i))
        print(newlayer[i], c)
        if(newlayer[i] > size[1]):
          return img
    for i in range(size[0]):
      img.putpixel((i, newlayer[i]), (0, 0, 0))
    layer = newlayer
    c += 1

generate_rings((100, 100), 100, 9).show()