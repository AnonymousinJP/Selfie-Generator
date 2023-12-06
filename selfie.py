from rembg import remove
from PIL import Image

inputImg="XXX.png"
outputImg="new.png"
input=Image.open(inputImg)

output=remove(input)
imgW,imgH=output.width,output.height

genBg=Image.new("RGB",size=(imgW, round(float(imgW*1.33))),color="#0099FF")
genBg.paste(output,(0,90),output) #x,y
genBg.save(outputImg)

"""
・横幅を1(基準)とした時、縦は 3:4=1:x
・x=4/3=1.33...となる
"""