import os
import glob
from PIL import Image

path = './../../resource/ColonImage'
folders = os.listdir(path)  #各フォルダをリストで保持
slidePx = int(input('slidePx:')) #スライドするピクセル数 既存手法　8px
windowSize = int(input('windowSize:')) #切り出しサイズ 既存手法128*128
dest = './../../resource/trimImage_' + 'slidePx' + str(slidePx) + '_' + 'windowSize' + str(windowSize) #保存先

if 'trimImage_' + 'slidePx' + str(slidePx) + '_' + 'windowSize' + str(windowSize) not in os.listdir('./../../resource'):
    os.mkdir(dest)

for fl in folders:
    files = glob.glob(path + '/' + fl + '/*.JPG')  #フォルダ内のJPGファイルのみ取り出し

    for im in files:
        target = Image.open(im)
        wid, hei = target.size #画像サイズ
        originName = im.split('\\')[-1].split('.')[0]#元のファイル名
        print(originName)
        if originName not in os.listdir(dest):
            os.mkdir(dest + '/' + originName)
        for x in range(0, hei, slidePx):
            for y in range(0, wid, slidePx):
                croppedTar = target.crop((x, y, x + windowSize, y + windowSize))
                index = 'X' + str(x) + '_' + 'Y' + str(y) 
                saveName = dest + '/' + originName + '/' + index + '.JPG'
                croppedTar.save(saveName, quality=95)
        

