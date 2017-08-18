#import os
#os.chdir("/Users/tenzinwangpo/anaconda/lib/python2.7/site-packages")

###DAte: August 12th I try to get Roi which i am thinking make this
## a image hwere shape_recog can able to predict the shape.

import cv2
import numpy as np

def shape_recog(img):
    main = img.copy()
    height, width = main.shape[:2]
    left_height = height/4
    left_width = width/4
    right_height = (height/4)+(height/2)
    right_width = (width/4)+(width/2)
    image = main[left_height:left_width, right_height:right_width]

    #First let convert the image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # switching image color to fully balck and white will more easier for us
    #detect contours
    ret, thresh = cv2.threshold(img_gray, 127,255,1)

    #now, lets extract the contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:

        #let use function which can guess the polygon
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True), True)

        if len(approx) == 3:
            shape_name = "Triangle"
            cv2.drawContours(image,[cnt],0,(0,255,0),-1)
            
 
            cv2.putText(img, shape_name, points(img),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)

        elif len(approx) == 4:
            x,y,w,h = cv2.boundingRect(cnt)

            #Check to see if 4 side ploygon is square or rectangle
            #cv2.boundingRect return the top left and then width and height
            if abs(w-h) <= 3:
                shape_name = "Square"
 
                #Find contour center to place text at the center
                cv2.drawContours(image, [cnt], 0,(0,125,255), -1)#draw whole inside
                cv2.putText(img,shape_name, points(img), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0),1)
            else:
                shape_name = "Rectangle"

                #Find contour center to place text at the center
                cv2.drawContours(image, [cnt], 0,(0,0,255), -1)
                cv2.putText(img,shape_name, points(img), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
        elif len(approx) == 10:
            shape_name = "Star"
            cv2.drawContours(image,[cnt],0,(255,255,0),-1)
            cv2.putText(img,shape_name, points(img), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0),1)

        elif len(approx) >= 15:
            shape_name = "Circle"
            cv2.drawContours(image, [cnt], 0, (0, 255, 255), -1)
            cv2.putText(img, shape_name, points(img), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
        
    return img

cap = cv2.VideoCapture(0)

def points(img):
    height, width = img.shape[:2]
    start_height, start_width = int(height*0.75), int(width*0.5)
    return start_height, start_width

#def Roi(frame):
 #   image = frame.copy()
  #  height, width = image.shape[:2]
   # left_height = height/4
 #   left_width = width/4
  #  right_height = (height/4)+(height/2)
   # right_width = (width/4)+(width/2)
   # cv2.rectangle(image,(left_width,left_height),(right_width,right_height),(127,50,127),3)
   # main = image[left_width:left_height,right_width:right_height]
    


while True:
    ret, frame = cap.read()
    image = frame.copy()
    height, width = image.shape[:2]
    left_height = height/4
    left_width = width/4
    right_height = (height/4)+(height/2)
    right_width = (width/4)+(width/2)
    cv2.rectangle(frame,(left_width,left_height),(right_width,right_height),(127,50,127),3)
    cv2.imshow("image Recognition", shape_recog(frame))
    if cv2.waitKey(1) == 13:
        break
 #       cv2.imshow("Identifying Shapes", image)
#        cv2.waitKey(0)

#cv2.destroyAllWindows()
cap.release()
cv2.destroyAllWindows()
        
