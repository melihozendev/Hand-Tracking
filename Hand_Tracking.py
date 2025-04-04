import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

# Initialize variables
prev_x , prev_y = None,None
tracked_center = None
previous_direction = None
direction = None
current_option = 0
option_colors = [(0,255,0),(0,255,0),(0,255,0)]
selection_locked = False
hand_open = False

while True:
    İsTrue, frame = video.read()
    if not İsTrue:
        break
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    minimum_black = np.array([0, 0, 0])
    maximum_black = np.array([180, 255, 50])

    mask = cv.inRange(hsv, minimum_black, maximum_black)
    mask = cv.morphologyEx(mask,cv.MORPH_OPEN,np.ones((7,7),np.uint8))
    mask = cv.dilate(mask,np.ones((7,7),np.uint8),iterations=1)
    contours,_ = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    obj_center_x,obj_center_y = None,None
  
    if contours:
        # Select the largest contour (presumably the hand)
        max_contour = max(contours,key=cv.contourArea)

        # Draw bounding box and center point
        x,y,w,h = cv.boundingRect(max_contour)
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        obj_center_x = x + w//2
        obj_center_y = y + h//2
        cv.circle(frame,(obj_center_x,obj_center_y),3,(0,255,0),-1)
       
    # Calculate direction of movement   
    if obj_center_x is not None and obj_center_y is not None:
        if prev_x is not None and prev_y is not None:
            dx = obj_center_x - prev_x
            dy = obj_center_y - prev_y

            if abs(dx) > 3:
                if dx > 0:
                    direction = 'Right'                   
                else:
                    direction = 'Left'                  
            elif abs(dy) > 3:
                if dy > 0:
                    direction = 'Down'                  
                else:
                    direction = 'Up'                  
            else:
                direction = 'Not moving'

            cv.putText(frame,direction,(25,50),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    
        prev_x,prev_y = obj_center_x,obj_center_y

         # Determine if hand is open or closed by contour area
        area = cv.contourArea(max_contour)
        if area < 14000:
            hand_stand = 'Close'
            selection_locked = True
            hand_open = False
        else:
            hand_stand = 'Open'
            selection_locked = False
            hand_open = True
        
        # Navigate options if hand is open
        if hand_open:
            if direction == 'Up' and current_option > 0: 
                current_option -= 1
                option_colors = [(0,255,0),(0,255,0),(0,255,0)]
                option_colors[current_option-1] = (255,0,0)
            elif direction == 'Down' and current_option < 3:
                current_option += 1
                option_colors = [(0,255,0),(0,255,0),(0,255,0)]
                option_colors[current_option-1] = (255,0,0)
        elif direction == 'Not moving' and not hand_open:
                option_colors = [(0,255,0),(0,255,0),(0,255,0)]
                option_colors[current_option-1] = (255,0,0)
                selection_locked = True
      
        # Display hand state and menu options
        cv.putText(frame,hand_stand,(25,90),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        cv.putText(frame,'Start',(30,350),cv.FONT_HERSHEY_SIMPLEX,1, option_colors[0],2)
        cv.putText(frame,'Settings',(30,390),cv.FONT_HERSHEY_SIMPLEX,1,option_colors[1],2)
        cv.putText(frame,'Exit',(30,430),cv.FONT_HERSHEY_SIMPLEX,1,option_colors[2],2)   
    
    cv.imshow('Video',frame)
  
    if cv.waitKey(1) & 0xFF == ord("d"):
        break

video.release()
cv.destroyAllWindows()