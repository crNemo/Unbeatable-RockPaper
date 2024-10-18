import cv2
import mediapipe as mp
#FUNCTIONS FOR LOGICS
def rock(tp,tt,ip,it,mp,mt,rp,rt,pp,pt):
    if(tp>tt) and (ip<it) and (mp<mt) and (rp<rt) and (pp<pt):
        return True
    else:
        return False

def paper(tp,tt,ip,it,mp,mt,rp,rt,pp,pt):
    if (tp>tt) and (ip>it) and (mp>mt) and (rp>rt) and (pp>pt):
        return True
    else:
        return False

def scissor(tp,tt,ip,it,mp,mt,rp,rt,pp,pt):
    if(tp>tt) and (ip>it) and (mp>mt) and (rp<rt) and (pp<pt):
        return True
    else:
        return False

video_capture=cv2.VideoCapture(0)
mp_hands=mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

#FIXED VALUES FOR CV2 PUT TEXT
font = cv2.FONT_HERSHEY_SIMPLEX
bottom = (10, 100)
fontcolor = (0,128,0)

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5) as hands:

        while video_capture.isOpened():
            _,frame=video_capture.read()
            frame=cv2.flip(frame,1)
            rgbframe=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            results=hands.process(rgbframe)

            if results.multi_hand_landmarks:
                for hl in results.multi_hand_landmarks:
                    #Thumb-Finger Landmark
                    tp=hl.landmark[2].y #THUMB-PIP
                    tt=hl.landmark[4].y #THUM-TIP

                    #Index-Finger Landmark
                    ip=hl.landmark[6].y #INDEX_FINGER_PIP
                    it=hl.landmark[8].y #INDEX_FINGER_TIP

                    #Middle-Finger Landmark
                    mp=hl.landmark[10].y #MIDDLE_FINGER_PIP
                    mt=hl.landmark[12].y #MIDDLE_FINGER_TIP

                    #Ring-Finger Landmark
                    rp=hl.landmark[14].y #RING_FINGER_PIP
                    rt=hl.landmark[16].y #RING_FINGER_TIP

                    #Pinky-Finger Landmark
                    pp=hl.landmark[18].y #PINKY_FINGER_PIP
                    pt=hl.landmark[20].y #PINKY_FINGER_TIP
                    out=''

                    if (rock(tp,tt,ip,it,mp,mt,rp,rt,pp,pt)):
                        out="Rock"
                        cv2.putText(frame, out, bottom, font, 1, fontcolor, 2)
                    elif (scissor(tp,tt,ip,it,mp,mt,rp,rt,pp,pt)):
                        out = "Scissor"
                        cv2.putText(frame, out, bottom, font, 1, fontcolor, 2)
                    elif (paper(tp,tt,ip,it,mp,mt,rp,rt,pp,pt)):
                        out = "Paper"
                        cv2.putText(frame, out, bottom, font, 1, fontcolor, 2)
                    if out=="Rock":
                        comp="Paper"
                        cv2.putText(frame, "Computer Response:", (300,50), font, 1, (0,0,0), 2)
                        cv2.putText(frame, comp, (400,85), font, 1, (0,0,0), 2)
                    if out=="Paper":
                        comp="Scissor"
                        cv2.putText(frame, "Computer Response:", (300,50), font, 1, (0,0,0), 2)
                        cv2.putText(frame, comp, (400,85), font, 1, (0,0,0), 2)
                    if out=="Scissor":
                        comp="Rock"
                        cv2.putText(frame, "Computer Response:", (300,50), font, 1, (0,0,0), 2)
                        cv2.putText(frame, comp, (400,85), font, 1, (0,0,0), 2)


                    mp_drawing.draw_landmarks(frame,hl, mp_hands.HAND_CONNECTIONS)
            cv2.imshow('Rock Paper Scissor',frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

video_capture.release()
cv2.destroyAllWindows()