import cv2
import pyautogui as pag
import numpy as np
from PIL import ImageGrab
from PIL.Image import Image
import time
from para import Para, Variable

var = Variable()
cv2.namedWindow('paras')
cv2.resizeWindow('paras', 640, 240)
cv2.createTrackbar('hl', 'paras', var.hl, 180, var.hl_call)
cv2.createTrackbar('hh', 'paras', var.hh, 180, var.hh_call)
cv2.createTrackbar('sl', 'paras', var.sl, 255, var.sl_call)
cv2.createTrackbar('sh', 'paras', var.sh, 255, var.sh_call)
cv2.createTrackbar('vl', 'paras', var.vl, 255, var.vl_call)
cv2.createTrackbar('vh', 'paras', var.vh, 255, var.vh_call)
cv2.namedWindow('size')
cv2.resizeWindow('size', 640, 480)
cv2.createTrackbar('x', 'size', var.pos_exclamation_mark[0], 1920, var.pos_x_call)
cv2.createTrackbar('y', 'size', var.pos_exclamation_mark[1], 1080, var.pos_y_call)
cv2.createTrackbar('l', 'size', var.left_offset, 30, var.left_offset_call)
cv2.createTrackbar('t', 'size', var.top_offset, 30, var.top_offset_call)
cv2.createTrackbar('r', 'size', var.right_offset, 30, var.right_offset_call)
cv2.createTrackbar('b', 'size', var.bottom_offset, 30, var.bottom_offset_call)

fishing_flag = False
window_active = False
while(True):
    window = pag.getActiveWindow()
    if (window is None):
        print(window)
        continue
    if(window.title == Para.window_name):
        window_active = True
    else :
        window_active = False
    if not fishing_flag and window_active:
        fishing_flag = True
        time.sleep(0.3)
        pag.doubleClick(var.pos_fishing[0], var.pos_fishing[1])
    ss_img : Image = ImageGrab.grab(var.area_exclamation_mark())
    #ss_img.show()
    #ss_img.save('mark_area.png')
    num = 0
    width = ss_img.size[0]
    height = ss_img.size[1]
    cv2_img = cv2.cvtColor(np.asarray(ss_img), cv2.COLOR_RGB2BGR)
    gus_img = cv2.GaussianBlur(cv2_img, (5, 5), 0)
    hsv_img = cv2.cvtColor(gus_img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(
        hsv_img,
        np.array([var.hl, var.sl, var.vl]),
        np.array([var.hh, var.sh, var.vh]))
    im_result = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)
    cv2.namedWindow('Mask')
    cv2.resizeWindow('Mask', 240, 120)
    cv2.imshow('Mask', mask)
    cv2.imshow('cv_img', cv2_img)
    h, w = mask.shape
    for i in range(h):
        for j in range(w):
            if mask[i, j] > 127:
                num += 1
    print('num :{}'.format(num))
    if num > 80:
        time.sleep(0.3)
        pag.click(var.pos_fishing[0], var.pos_fishing[1])
        time.sleep(1)
        pag.click(var.pos_confirm[0], var.pos_confirm[1])
        time.sleep(1.3)
        fishing_flag = False
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == 13:
        fishing_flag = False
    