# -*- coding:utf-8

import PIL.Image as Image
import sys
import os

class IconModel:

    def __init__(self,prefixName,multiples,pixel,needPixelName):
        self.prefixName = prefixName
        self.multiples = multiples
        self.pixel = pixel
        self.needPixelName = needPixelName

iconModelList = [
IconModel(prefixName="Icon",multiples=[1,2],pixel=[72,76],needPixelName=True),
IconModel(prefixName="Icon",multiples=[1,2,3],pixel=[40,],needPixelName=True),
IconModel(prefixName="Icon",multiples=[2,3],pixel=[60,],needPixelName=True),
IconModel(prefixName="Icon",multiples=[2,],pixel=[83.5,],needPixelName=True),

IconModel(prefixName="Icon",multiples=[1,2,],pixel=[57,],needPixelName=False),

IconModel(prefixName="Icon-Small",multiples=[1,2],pixel=[50,],needPixelName=True),
IconModel(prefixName="Icon-Small",multiples=[1,2,3],p`ixel=[29,],needPixelName=False),

IconModel(prefixName="NotificationIcon",multiples=[2,3,],pixel=[20,],needPixelName=False),
IconModel(prefixName="NotificationIcon~ipad",multiples=[1,2,],pixel=[20,],needPixelName=False),
]

def createAPPIcon(name):
    im = Image.open(name)

    path = r"appIcon/"
    os.mkdir(path)

    for model in iconModelList:
        for size in model.pixel:
            for multiple in model.multiples:

                trueSize = (int(size * multiple), int(size * multiple))
                newIm = im.resize(trueSize)
                imName = model.prefixName

                if model.needPixelName:
                    imName = imName + "-" + str(size)

                if multiple != 1:
                    imName = imName + "@" + str(multiple) + "x"

                imName = path + imName + ".png"
                newIm.save(imName)
    print("Create Success!")

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("请输入图标源文件名称")
    else:
        originImageName = sys.argv[1]
        createAPPIcon(originImageName)
