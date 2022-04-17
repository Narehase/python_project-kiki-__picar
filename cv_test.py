import os
import numpy as np
import cv2
import math
import time

def road_gift(w1,w2,y):

    if w1 > w2:
        x = w1 - w2
        ho = np.arctan(y/x) * (180/np.pi)
        ho = 180 - ho

    if w1 < w2:
        x = w2 - w1
        ho = np.arctan(y/x) * (180/np.pi)


    if w1 == w2:
        ho = 90

    return ho

def rain_input(canny_img):
    y,x = canny_img.shape

    t = t = canny_img[0,0]
    kit = []
    pit = []
    for i in range(x):
        ki = int(canny_img[0,i])
        if ki != int(t) :
            t = ki
            if ki == 255:
                pit.append(i)
                #print('cut')
                canny_img[0,i] = 128

    kit.append(min(pit))
    kit.append(max(pit))
    pit = []


    y -= 1
    t = t = canny_img[y,0]
    for i in range(x):
        ki = int(canny_img[y,i])
        if ki != int(t) :
            t = ki
            if ki == 255:
                pit.append(i)
                #print('cutq')
                canny_img[y,i] = 128

    kit.append(min(pit))
    kit.append(max(pit))
    pit = []

    cv2.imwrite('kiki_v2.png', canny_img)

    #print(y,x)

    return kit,x

def tyA(kit):
    if 4 != len(kit):
        try:
            raise Exception("tyA 리스트 개수를 확인하세요.")
        except Exception as e:
            print('예외가 발생했습니다.', e)

    a = int(kit[0])
    b = int(kit[2])
    c = int(kit[1])
    d = int(kit[3])

    al = (a + c)/2
    bl = (b + d)/2

    return al,bl

def pi_ui(r1,r2, g = 170):
    r = (r1 + r2)/2
    h = 45
    if r > g:
        i = r+g
    elif r < g:
        i = g - r

def ui_party(w,x,r):
    w = w/2


x = 120
w = 400
y = 120
h = 50




'''
a = cv2.imread('tet_1.png',cv2.IMREAD_GRAYSCALE)
'''

vivi = cv2.VideoCapture(0)
t1 = time.time()
while True:
    _, f = vivi.read()
    cf = f[y:y+h, x:x+w]
    cv2.imshow('kiki',cf)
    cv2.waitKey(16)
    t2 = time.time()
    print(int(t2 - t1))
    if(t2 - t1) > 3:
        break

while True:
    _, f = vivi.read()
    cf = f[y:y+h, x:x+w]
    a = cv2.cvtColor(cf,cv2.COLOR_BGR2GRAY)
    #a = cv2.flip(a,1)
    a = cv2.GaussianBlur(a,(3,3),0)
    a = cv2.Canny(a, 50,10)
    cv2.imshow('kiki',a)
    cv2.waitKey(16)
    #cv2.imwrite('kiki_v2.png', a)
    try:
        p,y = rain_input(a)
    except:
        print("경로이탈")
        continue
    #print(p)
    w1,w2 = tyA(p)
    #print(w1,w2)
    print(road_gift(w1,w2,y))
    print(f.shape)
    os.system('cls')