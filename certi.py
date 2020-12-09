from PIL import Image,ImageDraw,ImageFont
import pandas as pd
import os
df = pd.read_csv('Book1.csv')
font = ImageFont.truetype('arial.ttf',50)
for index,j in df.iterrows():
    img = Image.open('Certificate11024_1.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(400,420),text='{}'.format(j['name']),fill=(0,0,0,),font=font)
    draw.text(xy=(200,600),text='{}'.format(j['project manager']),fill=(0,0,0,),font=font)
    draw.text(xy=(600,600),text='{}'.format(j['month']),fill=(0,0,0,),font=font)
    img.save('pictures/{}.jpg'.format(j['name'].format(j['project manager']).format(j['month'])))
