from PIL import Image


def ChangeColor(index):
    colors = [(255,0,0),(100,255,0),(0,0,255),
          (230,230,20),(255,0,255),(0,0,0)]
    im = Image.new('RGB',(2,2),colors[index])
    im.save('images/ray.png')
