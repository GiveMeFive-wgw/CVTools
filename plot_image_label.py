import os
import cv2

path_img = r"./datasets/car_dataset/images/Image51.jpg"
path_label = r"./runs/val/exp2/labels/Image51.txt"
out_img_path = r"./Image51_out.jpg"

f = open(path_label, 'r+')
if os.path.exists(path_label) == True:

    img = cv2.imread(path_img)
    w = img.shape[1]
    h = img.shape[0]
    new_lines = []
    img_tmp = img.copy()            
    while True:
        line = f.readline()
        if line:
            msg = line.split(" ")
            # print(x_center,",",y_center,",",width,",",height)
            x1 = int((float(msg[1]) - float(msg[3]) / 2) * w)  # x_center - width/2
            y1 = int((float(msg[2]) - float(msg[4]) / 2) * h)  # y_center - height/2
            x2 = int((float(msg[1]) + float(msg[3]) / 2) * w)  # x_center + width/2
            y2 = int((float(msg[2]) + float(msg[4]) / 2) * h)  # y_center + height/2
            print(x1,",",y1,",",x2,",",y2)
            label = int(msg[0])
            if(label == 0): 
                color = (0, 0, 255)
            elif(label == 1):
                color = (0, 0, 255)
            elif(label == 2):
                color = (255, 0, 0)
            elif(label == 3):
                color = (255, 255, 0)
            else: color = (0, 255, 0)
            cv2.rectangle(img_tmp,(x1,y1),(x2,y2),color,5)
        else :
            break
# cv2.imshow("show", img_tmp)
cv2.imwrite(out_img_path, img_tmp)