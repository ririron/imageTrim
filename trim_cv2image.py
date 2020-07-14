import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

path = './../../resource/manualTrim'  #input("input path:")
target = input("targetIMG:") #'CNV2000002057140_1_13_trimV.jpg' 
print("cutintg [" + target + "]")
name = input("input cutting image name:")
img = cv2.imread(path + '/' + target)

x_ul, x_dr = map(int, input("input X [upLeft downRight]:").split())
y_ul, y_dr = map(int, input("input Y [upLeft downRight]:").split())

cut_img = img[y_ul:y_dr, x_ul:x_dr]

cv2.imwrite(path + '/' + name + target, cut_img)