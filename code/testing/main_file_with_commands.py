import cv2  # Helps to image processing
import mediapipe as mp  # Helps for Face Detection with lots of landmarks
import pyautogui  # Helps tp locate mouse pointer

# import camera as video capture
cam = cv2.VideoCapture(0)

# The face mesh is a 3D model of a face. we use refine landmarks for all differents lanmarks has unique
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# screen size
screen_w, screen_h = pyautogui.size()
while True:
    _, frame = cam.read()  # read camera as frame
    frame = cv2.flip(frame,1)  # filp the orignal cilp here 1 means vertically flip
    colur_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)  #covert video to different colour
    output = face_mesh.process(colur_frame)  # gives output
    landmarks_points = output.multi_face_landmarks  ## cheak face points
    #print(landmarks_points)
    frame_h , frame_w, _ = frame.shape
    if landmarks_points:  # I only want range of index 4 more landmarks
        landmarks = landmarks_points[0].landmark  # only need one face
        #for landmark in landmarks:
        #for landmark in landmarks[474:478]:
        for  id, landmark in enumerate(landmarks[474:478]): # enumerate is gives two output one is id & index and second is landmarks
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)    # no folt no
            cv2.circle(frame, (x,y), 3, (0,255,0))  # (draw, center, radius, colur(rgb))  face landmarks
            ##print(x, y)
            if id == 1: # I want to pick ether one of 4 to move couser
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x,screen_y)  # move on screen
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)     # two points on eye up and down
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        #print(left[0].y, left[1].y) # in vertically postion
        if (left[0].y - left[1].y) < 0.004:  # sign - is differance of two
            ## print('click')
            pyautogui.click()
            pyautogui.sleep(1) # wait for time at lest 1 sec

    cv2.imshow('Eye moues', frame)  ## here im means- image that imageshows i frame
    cv2.waitKey(1)